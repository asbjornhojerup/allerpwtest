#!/usr/bin/env python3
"""Script to replace cookie consent strings in test files."""
import os
import glob

# Define replacement patterns
replacements = [
    {"old": "Allow all cookies", "new": "Tillad alle"},
    {"old": "Use Necessary cookies", "new": "Kun nødvendige cookies"},
    {"old": "Use necessary cookies only", "new": "Kun nødvendige cookies"},
    {"old": "Use necessary cookies", "new": "Kun nødvendige cookies"},
]

# Get all test .py files
test_files = glob.glob("/Users/asbjorn.hojerup/allerpwtest/tests/test_*.py")

# Track results
results = {}
total_replacements = 0

for file_path in sorted(test_files):
    # Skip conftest.py and non-relevant files
    if "conftest" in file_path or "isstaging" in file_path or "isprod" in file_path:
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    file_replacements = 0
    
    # Apply replacements in order
    for replacement in replacements:
        old = replacement["old"]
        new = replacement["new"]
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            file_replacements += count
            
            if file_path not in results:
                results[file_path] = {}
            results[file_path][f"{old} → {new}"] = count
    
    # Write back if there were changes
    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        total_replacements += file_replacements
        print(f"✓ {os.path.basename(file_path)}: {file_replacements} replacements")
    else:
        print(f"- {os.path.basename(file_path)}: No changes")

# Print summary
print("\n" + "=" * 70)
print("SUMMARY OF REPLACEMENTS")
print("=" * 70)

for file_path in sorted(results.keys()):
    filename = os.path.basename(file_path)
    print(f"\n{filename}:")
    for replacement, count in results[file_path].items():
        print(f"  {replacement}: {count} instance(s)")

print(f"\nTotal replacements: {total_replacements}")
