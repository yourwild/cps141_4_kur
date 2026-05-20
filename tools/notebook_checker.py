"""
notebook_checker.py
-------------------
Reads a Jupyter problemset notebook (.ipynb), extracts:
  - Expected outputs from yellow alert-warning boxes
  - Actual outputs from executed code cells

Then compares them problem by problem and prints a PASS/FAIL report.

Usage (from project root):
    python tools/notebook_checker.py assignments/dylankur_problemset_1.ipynb

Or import and call check_notebook() from another script or notebook cell.
"""

import json
import re
import os
import sys

# Allow running from any directory
sys.path.insert(0, os.path.dirname(__file__))
from checker_config import CONFIGS


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _strip_html(text):
    """Remove HTML tags and normalise <br> to newlines."""
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<[^>]+>', '', text)
    return text.strip()


def _normalize(text):
    """Collapse all whitespace runs to a single space for loose comparison."""
    return re.sub(r'\s+', ' ', text).strip()


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

def extract_expected_outputs(nb):
    """
    Walk notebook cells and collect text from every alert-warning markdown cell.
    Returns a list of plain-text strings, one per yellow box (in order).
    """
    expected = []
    for cell in nb['cells']:
        if cell['cell_type'] != 'markdown':
            continue
        source = ''.join(cell['source'])
        if 'alert-warning' not in source:
            continue
        expected.append(_strip_html(source))
    return expected


def _cell_stdout(cell):
    """Extract stdout text from a single code cell's outputs."""
    lines = []
    for output in cell.get('outputs', []):
        if output.get('output_type') == 'stream' and output.get('name') == 'stdout':
            lines.extend(output.get('text', []))
        elif output.get('output_type') in ('execute_result', 'display_data'):
            data = output.get('data', {})
            if 'text/plain' in data:
                lines.extend(data['text/plain'] if isinstance(data['text/plain'], list)
                             else [data['text/plain']])
    return ''.join(lines).strip()


def extract_actual_outputs(nb):
    """
    Walk notebook cells and for each alert-warning markdown cell find the
    most recent code cell that appeared before it. Returns a list of
    (output_str, source_str) tuples aligned 1-to-1 with the yellow boxes.
    """
    actual = []
    last_code_cell = None

    for cell in nb['cells']:
        if cell['cell_type'] == 'code' and ''.join(cell.get('source', [])).strip():
            last_code_cell = cell
        elif cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            if 'alert-warning' in source:
                if last_code_cell is not None:
                    actual.append((
                        _cell_stdout(last_code_cell),
                        ''.join(last_code_cell.get('source', []))
                    ))
                else:
                    actual.append(('', ''))
                last_code_cell = None  # consume it so it isn't reused

    return actual


# ---------------------------------------------------------------------------
# Annotation helpers
# ---------------------------------------------------------------------------

_SALUTATION_PATTERN = re.compile(
    r'(?i)\b(hello|hi|hey|greetings|dear|howdy)[,!]?\s+(\w+)'
)
_STUDENT_NAME = "Dylan"


def _check_input_required(source):
    """Return a warning string if the cell source contains an input() call."""
    if re.search(r'\binput\s*\(', source):
        return "⚠️  INPUT REQUIRED — this cell uses input(); run it interactively in Jupyter"
    return None


def _check_customization(output):
    """
    Return a warning string if the output contains a salutation (Hello, X)
    where X is not the student's name.
    """
    for match in _SALUTATION_PATTERN.finditer(output):
        name = match.group(2)
        if name.lower() != _STUDENT_NAME.lower():
            return (
                f"⚠️  CUSTOMIZE REQUIRED — output contains '{match.group(0)}' "
                f"but the name should be '{_STUDENT_NAME}'. "
                f"Update the greeting argument to use your own name."
            )
    return None


_GREETING_CALL_PATTERN = re.compile(
    r"""greeting\s*\(\s*["'](\w+)["']\s*\)"""
)


def _check_customization_in_source(source):
    """
    Return a warning string if the cell source calls greeting() with a name
    that is not the student's name.
    """
    for match in _GREETING_CALL_PATTERN.finditer(source):
        name = match.group(1)
        if name.lower() != _STUDENT_NAME.lower():
            return (
                f"⚠️  CUSTOMIZE REQUIRED — greeting() called with '{name}' "
                f"but should use your own name '{_STUDENT_NAME}'. "
                f"Change greeting(\"{name}\") to greeting(\"{_STUDENT_NAME}\")."
            )
    return None


# ---------------------------------------------------------------------------
# Checker
# ---------------------------------------------------------------------------

def check_notebook(notebook_path, config=None):
    """
    Compare expected vs actual outputs for every problem in the notebook.

    Parameters
    ----------
    notebook_path : str
        Full or relative path to the .ipynb file.
    config : dict, optional
        Override config (defaults to CONFIGS lookup by filename).

    Returns
    -------
    dict  { 'problem_1': '✅ PASS', 'problem_2': '❌ FAIL', ... }
    """
    notebook_path = os.path.abspath(notebook_path)
    filename = os.path.basename(notebook_path)

    if config is None:
        config = CONFIGS.get(filename, {"skip_problems": [], "range_checks": {}, "input_mocks": {}})

    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    expected_list = extract_expected_outputs(nb)
    actual_pairs  = extract_actual_outputs(nb)

    results = {}
    pairs = list(zip(expected_list, actual_pairs))

    for i, (exp, (act, src)) in enumerate(pairs, start=1):
        key = f"problem_{i}"

        # Check for input() usage and greeting customization in the code cell source
        input_warning = _check_input_required(src)
        source_custom_warning = _check_customization_in_source(src)

        if i in config.get("skip_problems", []):
            status = "⏭  SKIPPED (non-deterministic output)"
            custom_warning = _check_customization(act) or source_custom_warning
            if custom_warning:
                status += f"\n    {custom_warning}"
            results[key] = status

        elif i in config.get("range_checks", {}):
            ok = config["range_checks"][i](act)
            status = "✅ PASS" if ok else f"❌ FAIL\n    Expected pattern not found in:\n    {act!r}"
            custom_warning = _check_customization(act) or source_custom_warning
            if custom_warning:
                status += f"\n    {custom_warning}"
            results[key] = status

        elif input_warning:
            status = input_warning
            if source_custom_warning:
                status += f"\n    {source_custom_warning}"
            results[key] = status

        else:
            norm_act = _normalize(act)
            norm_exp = _normalize(exp)

            if not norm_act:
                status = "❌ FAIL (cell not run or no output produced)"
                if source_custom_warning:
                    status += f"\n    {source_custom_warning}"
                results[key] = status
            elif norm_act in norm_exp or norm_exp in norm_act:
                status = "✅ PASS"
                custom_warning = _check_customization(act) or source_custom_warning
                if custom_warning:
                    status += f"\n    {custom_warning}"
                results[key] = status
            else:
                # Strip "Expected Output:" header and check each token appears in actual
                exp_value = re.sub(r'(?i)expected output\s*[:\-]?\s*', '', norm_exp).strip()
                tokens = exp_value.split()
                if exp_value and exp_value in norm_act:
                    status = "✅ PASS"
                elif tokens and all(t in norm_act for t in tokens):
                    status = "✅ PASS"
                else:
                    status = (
                        f"❌ FAIL\n"
                        f"    Expected : {norm_exp[:120]}\n"
                        f"    Got      : {norm_act[:120]}"
                    )
                custom_warning = _check_customization(act) or source_custom_warning
                if custom_warning:
                    status += f"\n    {custom_warning}"
                results[key] = status

    # Report problems that have expected output but no actual output yet
    for i in range(len(pairs) + 1, len(expected_list) + 1):
        results[f"problem_{i}"] = "❌ FAIL (cell not run or no output produced)"

    return results


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/notebook_checker.py <path/to/notebook.ipynb>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.exists(path):
        print(f"File not found: {path}")
        sys.exit(1)

    print(f"\n{'='*60}")
    print(f"  Notebook Checker")
    print(f"  File: {os.path.basename(path)}")
    print(f"{'='*60}\n")

    results = check_notebook(path)

    for problem, status in results.items():
        print(f"  {problem.replace('_', ' ').title():12s}  {status}")

    total   = len(results)
    passed  = sum(1 for v in results.values() if v.startswith("✅"))
    skipped = sum(1 for v in results.values() if v.startswith("⏭"))
    failed  = total - passed - skipped

    print(f"\n{'='*60}")
    print(f"  Results: {passed} passed  |  {failed} failed  |  {skipped} skipped  |  {total} total")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
