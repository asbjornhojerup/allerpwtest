# Playwright Test Runner UI

A simple Streamlit web interface for running Playwright tests without needing CLI access.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Access in browser:**
   Open `http://localhost:8501` in your web browser.

## How it works

- Select a site, environment, and platform from the dropdowns
- Click "Run Test" to execute the test via Playwright
- View the output and test results in real-time

## Requirements

- Python 3.8+ with pip
- Node.js with npm (for Playwright)
- Tests directory accessible at `../tests`

## Deployment

To deploy publicly:

1. **Streamlit Cloud (recommended for public repos)**
   - Push to GitHub
   - Connect repo at https://streamlit.io/cloud
   - Set working directory to `streamlit-runner`

2. **Docker container**
   - Build with Node.js + Python layer
   - Mount tests directory
   - Expose port 8501

3. **Self-hosted server**
   - Install dependencies
   - Use systemd/screen/supervisor to keep process running
   - Add reverse proxy (nginx) for HTTPS

## Notes

- Tests run in the context of the tests directory
- Ensure all npm dependencies are installed (`npm install` in tests folder)
- Playwright browsers must be available (`npx playwright install`)
