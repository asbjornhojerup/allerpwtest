# allerpwtest

This repository contains Playwright and pytest test suites for various environments
and platforms. It also includes a Streamlit runner example.

## Structure

- `tests/`: Python and TypeScript tests with fixtures
- `e2e/`: Example Playwright spec
- `streamlit-runner/`: Streamlit application and requirements

## Usage

Activate the Python virtual environment:

```bash
source .venv/bin/activate
```

Run tests with pytest:

```bash
pytest
```

Run Playwright tests:

```bash
npx playwright test
```

Run the Flask web app:

```bash
python index.py
# or
flask run --app web_app
```
