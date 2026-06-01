# CPS 141 — Introduction to Programming Using Python
### Dylan Kur | Washtenaw Community College

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![JupyterLab](https://img.shields.io/badge/JupyterLab-latest-orange?style=flat-square&logo=jupyter)
![Go Blue](https://img.shields.io/badge/Go-Blue!-00274C?style=flat-square)

---

## What Is This?

This is your personal coding workspace for CPS 141. Every assignment lives here — organized, version-controlled, and yours. You'll use this repo to write code, save data, and track your progress across the entire course.

This isn't just a folder of homework files. It's your first real developer project. Treat it that way.

---

## Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/cps141-python.git
cd cps141-python
```

### 2. Run Setup
This creates your virtual environment and installs everything you need:
```bash
python setup.py
```
If `python` points to Python 2 on your machine, use `python3 setup.py` instead.

Optional wrappers:
```bash
./setup.sh
```

```powershell
.\setup.ps1
```

`setup.py` detects whether it is running on Windows, macOS, or Linux and prints the right activation command for that machine.

### 3. Configure Your API Keys
```bash
cp .env.sample .env
```
If `.env.sample` exists, copy it to `.env`, then fill in your API keys. **Never share this file. Never commit this file.**

### 4. Launch JupyterLab
```bash
source venv/bin/activate  # macOS/Linux
# or
source venv/Scripts/activate  # Git Bash on Windows
python start_jupyter.py
```

On Windows PowerShell, use:
```powershell
.\venv\Scripts\Activate.ps1
py start_jupyter.py
```

`start_jupyter.py` prints the exact local JupyterLab URL in the terminal before the server starts, so it is easy to paste into a browser.

Or open the project in PyCharm — it will detect the notebooks automatically.

---

## Repo Structure

```
cps141-python/
├── README.md                   ← you are here
├── .gitignore                  ← keeps secrets and junk out of GitHub
├── .env                        ← your API keys (never committed)
├── .env.sample                 ← template showing what keys are needed
├── requirements.txt            ← all Python dependencies
├── start_jupyter.py            ← starts JupyterLab and prints the browser URL
├── setup.sh                    ← one-command environment setup
├── prompt_template.md          ← how to ask AI for help on assignments
├── custom.css                  ← Michigan-themed notebook styling
├── tools/
│   ├── notebook_checker.py     ← automated output checker
│   └── checker_config.py       ← per-problemset checker config
└── assignments/
    ├── dylankur_problemset_1.ipynb  ← Problem Set 1 notebook
    └── Dylan Kur- Problem Set 1     ← original instructor notebook
```

---

## How Assignments Work
1. A new assignment folder gets added to `/assignments/`
2. Read the assignment `README.md` first
3. Work in the `.ipynb` notebook
4. Use `prompt_template.md` when asking AI for help
5. Save your work, commit, and push

---

## Notebook Checker Tool

The `tools/` folder contains a checker that automatically compares your notebook's actual output against the yellow **Expected Output** boxes — no manual eyeballing required.

### How it works

1. It reads your `.ipynb` file
2. For each yellow warning box it finds the code cell directly above it
3. It compares the actual output to the expected output and prints `✅ PASS`, `❌ FAIL`, `⚠️ NOT RUN`, or `⏭ SKIPPED`

### Run the checker

From the project root (activate your virtual environment first):

```powershell
python tools/notebook_checker.py assignments/dylankur_problemset_1.ipynb
```

Example output:

```
============================================================
  Notebook Checker
  File: dylankur_problemset_1.ipynb
============================================================
  Problem 1     ✅ PASS
  Problem 2     ❌ FAIL (cell not run or no output produced)
  Problem 3     ✅ PASS
  Problem 4     ✅ PASS
  Problem 5     ❌ FAIL
    Expected : Expected Output: Enter an integer: 5 10
    Got      : <class 'str'> 8
  Problem 6     ✅ PASS
  Problem 7     ⏭  SKIPPED (non-deterministic output)
  Problem 8     ✅ PASS
  Problem 9     ✅ PASS
============================================================
  Results: 6 passed  |  2 failed  |  1 skipped  |  9 total
============================================================
```

### Status meanings

| Status | Meaning |
|--------|---------|
| ✅ PASS | Your output matches the expected output |
| ❌ FAIL | Output doesn't match — re-read the problem and fix your code |
| ❌ FAIL (cell not run) | Cell was never run or produced no output — complete and run it in Jupyter first, then save |
| ⏭ SKIPPED | Problem uses random numbers — exact match not possible |
| ⚠️ INPUT REQUIRED | Cell uses `input()` — run it interactively in Jupyter, it can't be checked automatically |
| ⚠️ CUSTOMIZE REQUIRED | A greeting uses a placeholder name instead of yours — update the argument to use your own name |

### Use it inside a notebook cell

You can also call the checker directly from a notebook cell:

```python
import sys
sys.path.insert(0, '../tools')
from notebook_checker import check_notebook

results = check_notebook('dylankur_problemset_1.ipynb')
for problem, status in results.items():
    print(f"{problem}: {status}")
```

### Adding a new problemset

1. Open `tools/checker_config.py`
2. Copy the template comment block at the bottom and fill in the filename
3. Set `skip_problems` for any problems with random output
4. Set `input_mocks` for any problems that use `input()`
5. Run the checker — it works automatically for any `.ipynb` with `alert-warning` boxes

---

## Git Basics — The Only Commands You Need Right Now

```bash
# See what's changed
git status

# Stage your changes
git add .

# Commit with a message
git commit -m "completed assignment 01"

# Push to GitHub
git push
```

---

## Course Objectives

By the end of this course you will be able to:

- Write programs using loops, conditionals, and functions
- Work with strings, lists, and dictionaries
- Build and use custom classes
- Read and write files (text and CSV)
- Call REST APIs and parse JSON
- Analyze and visualize data using Python libraries

---

## How This Course Works — Notes from the Instructor

A few things worth knowing upfront so nothing surprises you:

**All work happens in Jupyter Notebooks.**
You will write and run every line of Python in a `.ipynb` notebook. No command line, no running scripts from a terminal. If you're in the notebook, you're in the right place.

**Datasets are provided.**
For almost every assignment, the data file will be given to you — just drop it in the `data/` folder and you're ready. The one exception: REST API assignments require you to get your own API key. When you hit that unit, check the assignment README for instructions.

**What this course does NOT cover.**
This is a foundations course. You won't be building web apps or deploying servers. Specifically off the table: Flask, Django, running Python via command line, and any server-side development. If you find AI suggesting those approaches, redirect it — see `prompt_template.md` for how.

**Transfer credit.**
This course is approved for transfer to the University of Michigan. 💛💙

---

## Assessment

Your grade comes from two things:
- **Departmental final exam** — covers all core concepts
- **Project portfolio** — your collected notebooks, including source code, reports, and charts

The standard: 70% of students must score 75% or higher. You're going to clear that easily.

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python 3.11+ | Primary language |
| JupyterLab | Interactive notebooks |
| PyCharm Pro | Full IDE experience |
| pandas | Data manipulation |
| matplotlib | Basic visualization |
| seaborn | Statistical visualization |
| plotly | Interactive charts |
| python-dotenv | Environment variable management |
| anthropic / openai | AI API integrations |

---

## A Note on AI Tools

You have access to AI assistants (Claude, ChatGPT). Use them. Knowing how to work with AI is a real skill. But use them to **learn**, not to skip learning. If AI writes code you don't understand, you haven't learned anything yet.

Use `prompt_template.md` to get the most out of every AI interaction.

---

## The "Comment-First & Refine" Method

To get the most out of your coding journey, follow the **Comment-First & Refine** method. This ensures you master the logic, not just the syntax.

1.  **Draft Descriptive Comments:** Write your intent in plain English before writing code.
2.  **Implementation:** Use code completion to write the code, but verify it against your comment.
3.  **Intermediate Printing:** Use `print()` to verify your logic at every step.
4.  **Refinement:** After success, update your comments to explain *why* the code works.

See [README.CodeCompletion.md](./README.CodeCompletion.md) for the full guide and examples.

---

*Built with Dylan — Go Blue! 💛💙*

---