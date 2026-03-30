#!/bin/bash
set -e

echo "Cleaning old node_modules, lock files, and npm cache..."
rm -rf node_modules package-lock.json
npm cache clean --force

echo "Installing Node.js dependencies fresh..."
npm install

echo "Installing Playwright browsers..."
npx playwright install --with-deps chromium

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build complete!"
