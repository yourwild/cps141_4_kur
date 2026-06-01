import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

def run_notebook(path):
    with open(path) as f:
        nb = nbformat.read(f, as_version=4)
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    try:
        ep.preprocess(nb, {'metadata': {'path': 'assignments'}})
    except Exception as e:
        print(f"Error executing the notebook: {e}")
        # Find the cell that failed
        for cell in nb.cells:
            if 'outputs' in cell:
                for output in cell['outputs']:
                    if output.output_type == 'error':
                        print(f"Cell failed: {cell.source}")
                        print(f"Error: {output.ename}: {output.evalue}")
    
    # Check unit test results if possible, or just print outputs of problem 1
    for cell in nb.cells:
        if cell.cell_type == 'code' and '# Problem 1' in cell.source:
             print("Problem 1 output:")
             if 'outputs' in cell:
                 for output in cell['outputs']:
                     if output.output_type == 'stream':
                         print(output.text)

run_notebook('assignments/ProblemSet02Updated (1).ipynb')
