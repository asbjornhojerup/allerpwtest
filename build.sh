#!/bin/bash
set -e

echo "Cleaning node modules..."
rm -rf node_modules package-lock.json

echo "Installing Node.js dependencies..."
npm install

echo "Installing Playwright browsers..."
npx playwright install

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build complete!"
