#!/bin/bash
set -e

echo "Installing Node.js dependencies..."
npm install --prefer-offline --no-audit

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Build complete!"
