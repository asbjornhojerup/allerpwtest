#!/bin/bash
set -e

echo "Cleaning old node_modules..."
rm -rf node_modules

echo "Installing Node.js dependencies from lock file..."
npm ci --include=dev

echo "Verifying playwright-core installation..."
ls node_modules/playwright-core/lib/server/utils/debugLogger.js && echo "debugLogger OK" || echo "WARNING: debugLogger MISSING"

echo "Installing Playwright browsers..."
node_modules/.bin/playwright install --with-deps chromium

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build complete!"
