### Evidence from the notebook for Question 1

You can point directly to your `load_inventory` function in **Step 2** of `wild_suggestions_dylankurmidtermproject.ipynb` as the concrete proof that you applied this practice in your own code.

### Code evidence from `load_inventory` (Step 2)

```python
def load_inventory(filename):
    inventory = {}

    try:
        # open the file in read mode
        f = open(filename, 'r')
        reader = csv.reader(f)       # create a csv reader object
        next(reader)                 # skip the header row
        print(f"File '{filename}' opened successfully.")

        # First pass: read every row into the inventory dictionary.
        for row in reader:
            if not row:                  # skip any blank lines in the CSV
                continue
            product_name = row[0]
            quantity = int(row[1])       # convert string -> int
            price = float(row[2])        # convert string -> float
            inventory[product_name] = {'quantity': quantity, 'price': price}

        f.close()
        ...
        print(f"Inventory loaded successfully.")

    except FileNotFoundError:
        # if file doesn't exist, print error and return empty dictionary
        print(f"Error: File '{filename}' not found.")

    return inventory
```

### How this code backs up each claim in your answer

- **"The biggest one is `FileNotFoundError`..."** → Your function literally has `except FileNotFoundError:` wrapping the `open(filename, 'r')` call. If the CSV path is wrong, control jumps to the handler instead of crashing.
- **"...crashes with a weird error message that doesn't help the user at all."** → Instead of letting Python print a raw traceback, you print a clean, user-friendly message: `Error: File '{filename}' not found.` That is exactly the "graceful handling" you describe.
- **"...the program can handle those situations gracefully and let the user know what happened instead of just stopping."** → After the except branch runs, the function still returns a valid (empty) `inventory = {}` dictionary. That means the rest of the notebook (`if inventory:` check in the preview cell, and the `if inventory:` guard inside `main()`) can keep running without throwing a second error. This is direct evidence of "graceful degradation."
- **"...the data inside being formatted wrong so it can't be converted properly."** → The `int(row[1])` and `float(row[2])` lines inside the `try` block are exactly the spots where a `ValueError` would be raised if the CSV had bad data (e.g., `"abc"` in the quantity column). Because they live inside the `try`, they would not crash the whole program — though you could note as a "next improvement" that you'd add `except ValueError:` to specifically catch malformed-data cases.

### Real bug this prevented in your own project

You can also reference the actual debugging history from this notebook as lived evidence:

- Earlier in the project, the preview cell crashed with `FileNotFoundError: [Errno 2] No such file or directory: 'assignments/Data/inventory_data.csv'` because the working directory didn't match the hardcoded path.
- Because `load_inventory` was wrapped in `try/except FileNotFoundError`, when the same path issue hit the function call it printed a clean error instead of halting the whole notebook — which is exactly the user-friendly behavior your answer describes.

### Suggested one-line addition to your written answer

If you want to tie the answer back to your code explicitly, add a sentence like:

> "You can see this in my `load_inventory` function in Step 2, where I wrap the `open()` call in a `try` block and catch `FileNotFoundError` so the program prints `Error: File '<name>' not found.` and returns an empty dictionary, letting the rest of the notebook keep running instead of crashing."

That single sentence turns the answer into a code-backed response, which is what the question is asking you to demonstrate.

