#!/bin/bash
set -e

echo "Installing Node.js dependencies..."
npm ci

echo "Installing Playwright browsers..."
npx playwright install --with-deps chromium

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build complete!"
