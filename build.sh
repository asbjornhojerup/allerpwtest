#!/bin/bash
set -e

echo "Cleaning old node_modules and npm cache..."
rm -rf node_modules
npm cache clean --force

echo "Installing Node.js dependencies from lock file..."
npm ci

echo "Installing Playwright browsers..."
npx playwright install --with-deps chromium

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build complete!"
