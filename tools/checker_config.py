# checker_config.py
# Per-file configuration for the notebook checker tool.
# Add an entry here for each problemset notebook.

CONFIGS = {
    "dylankur_problemset_1.ipynb": {
        # Problem numbers to skip exact match (e.g. random output)
        "skip_problems": [7],
        # Custom validation functions for specific problems
        # Function receives the actual output string, returns True/False
        "range_checks": {
            7: lambda out: (
                "randomDigit" in out or
                any(line.strip().isdigit() or
                    "returns" in line.lower() or
                    "hello," in line.lower()
                    for line in out.splitlines())
            )
        },
        # Problems that use input() — provide a mock value
        "input_mocks": {
            5: "5"
        }
    },
    # Template for future problemsets — copy and customize
    # "dylankur_problemset_2.ipynb": {
    #     "skip_problems": [],
    #     "range_checks": {},
    #     "input_mocks": {}
    # },
}
