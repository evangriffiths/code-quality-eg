# Code Quality Dev Tools

This example repo demonstrates adding dev tools to our workflow to improve code quality. Specifically, we look at:

- [mypy](https://github.com/python/mypy), a static type checker (improves code readability, and reduces bugs)
- [black](https://github.com/psf/black) a PEP8-like code formatter (improves code readability)
- [autoflake](https://github.com/PyCQA/autoflake) a linter that removes unused imports and variables (improves code readability and speed)
- [isort](https://github.com/PyCQA/isort) a linter that sorts imports (improves code readability)

Code readability is important when you have multiple people working on a project.

Code speed and buggyness are always good to improve!

## Setup

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Now install the tools:

```bash
pip install mypy black autoflake isort
```

## Run the tools

```bash
python -m mypy .

python -m black .
python -m autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive .
python -m isort --profile black .
```

## Pre-commit

Pre-commit is a tool that integrates with git to run some user-defined hooks when when you call `git commit`.

Install pre-commit:

```bash
pip install pre-commit
```

You have 3 options for integrating this with your development environment:

1. Run `pre-commit install`. Now every time you run `git commit ...` it runs the pre-commit hooks and changes the files for you to-recommit.
2. Run `pre-commit run --all-files` manually before committing.
3. Install the respective vscode extenstions ([black](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter), [autoflake](https://marketplace.visualstudio.com/items?itemName=mikoz.autoflake-extension) and [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)), and add [this](https://gist.github.com/evangriffiths/f9f8fd6d365f3acafb7e1aa1bff78dae) config to your vscode User settings.json. This will run the linting tools on-save on a per-file basis, so the CI checks will all pass, without requiring pre-commit.
