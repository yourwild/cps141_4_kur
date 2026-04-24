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
chmod +x setup.sh
./setup.sh
```

### 3. Configure Your API Keys
```bash
cp .env.sample .env
```
Open `.env` and fill in your API keys. **Never share this file. Never commit this file.**

### 4. Launch JupyterLab
```bash
source venv/bin/activate
jupyter lab
```

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
├── setup.sh                    ← one-command environment setup
├── prompt_template.md          ← how to ask AI for help on assignments
├── custom.css                  ← Michigan-themed notebook styling
└── assignments/
    └── assignment_01_hello_world/
        ├── README.md           ← assignment instructions and objectives
        ├── assignment_01.ipynb ← your notebook
        ├── data/               ← input datasets
        ├── assets/             ← images, charts, reference files
        ├── output/             ← files your notebook creates
        └── docs/
            └── notes.md        ← your notes and documentation
```

---

## How Assignments Work

1. A new assignment folder gets added to `/assignments/`
2. Read the assignment `README.md` first
3. Work in the `.ipynb` notebook
4. Use `prompt_template.md` when asking AI for help
5. Save your work, commit, and push

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

*Built with Dylan — Go Blue! 💛💙*
