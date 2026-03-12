"""Convenience entry point for the Streamlit runner.

Running this module will start the Streamlit application located in
`streamlit-runner/streamlit_app.py`.

Usage:

```bash
python index.py
```

or, if the venv is activated:

```bash
streamlit run index.py
```
"""

import subprocess
import sys
from pathlib import Path

# determine path to the streamlit app
app_path = Path(__file__).parent / "streamlit-runner" / "streamlit_app.py"

if not app_path.exists():
    sys.exit(f"Streamlit app not found at {app_path}")

# when the module is executed directly, hand off to streamlit
def main() -> None:
    # use the same python executable to invoke streamlit
    cmd = [sys.executable, "-m", "streamlit", "run", str(app_path)]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as exc:
        sys.exit(f"Streamlit failed with exit code {exc.returncode}")


if __name__ == "__main__":
    main()
