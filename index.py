"""Entry point for the Playwright Test Runner web application.

Running this module will start the Flask web server.

Usage:

```bash
python index.py
```

or:

```bash
flask run --app web_app
```
"""

import os
import sys

# when the module is executed directly, run the flask web app

def main() -> None:
    # delegate to the Flask app if it exists
    try:
        import web_app
        port = int(os.environ.get("PORT", 8000))
        web_app.app.run(host="0.0.0.0", port=port, debug=True)
    except ImportError:
        sys.exit("web_app module not found; cannot start web server")


if __name__ == "__main__":
    main()
