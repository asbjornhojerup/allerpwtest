# Base image with both Python and Node.js
FROM python:3.11-slim as builder

# Install Node.js (required for Playwright)
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy and install Python dependencies
COPY streamlit-runner/requirements.txt ./streamlit-runner/requirements.txt
RUN python3 -m pip install --no-cache-dir -r streamlit-runner/requirements.txt

# Copy application and project files
COPY streamlit-runner ./streamlit-runner
COPY package*.json ./

# Install npm dependencies at project root
RUN npm install

# Copy entire tests directory (no need for separate npm step)
COPY tests ./tests

# Install Playwright browsers inside tests folder (skip additional deps to avoid ARM package issues)
RUN cd tests && npx playwright install

# Expose port for Streamlit
EXPOSE 8501

# Set environment variables to disable telemetry and run headless
ENV ST_DEFAULT_SERVER_PORT=8501 \
    PIP_NO_CACHE_DIR=off \
    PYTHONUNBUFFERED=1

# Default command to start Streamlit
CMD ["python3", "-m", "streamlit", "run", "streamlit-runner/streamlit_app.py", "--server.headless=true"]
