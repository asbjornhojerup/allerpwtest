import streamlit as st
import subprocess
from pathlib import Path
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import shutil

# Get paths - handle both local and cloud deployments
script_dir = Path(__file__).parent
project_root = script_dir.parent
tests_dir = project_root / "tests"

# Fallback for cloud deployments where structure might differ
if not tests_dir.exists():
    # Try looking for tests in parent directory
    tests_dir = Path(__file__).parent.parent.parent / "tests"
    
if not tests_dir.exists():
    # Try current working directory
    tests_dir = Path.cwd() / "tests"

# Parse test files to extract site/env/platform combinations
test_files = sorted([f.name for f in tests_dir.glob("*.test.ts")])

# Extract unique values
sites = sorted(list(set([f[0:2] for f in test_files])))
envs = sorted(list(set([f.split('.')[0][2:] for f in test_files])))
plats = sorted(list(set([f.split('.')[1] for f in test_files])))

st.set_page_config(page_title="Playwright Test Runner", layout="wide")

st.title("🎭 Playwright Test Runner")
st.markdown("Select parameters and run E2E tests")

# Check if npx is available
npx_available = shutil.which("npx") is not None

if not npx_available:
    st.error("""
    ❌ **Node.js/npm is not available in this environment**
    
    This app requires `npx` to run Playwright tests. 
    
    **To use this app:**
    - Run it **locally** on your machine with: `/usr/bin/python3 -m streamlit run streamlit_app.py`
    - This app cannot run on Streamlit Cloud since it doesn't support Node.js
    
    **If you want to run tests in the cloud, you have these options:**
    1. Convert tests to Python using Playwright Python library
    2. Deploy a separate Node.js backend service to run the tests
    3. Use the app locally only
    """)
    st.stop()

# Debug info (can be removed later)
with st.expander("Debug Info", expanded=False):
    st.write(f"Script location: {Path(__file__)}")
    st.write(f"Tests directory: {tests_dir}")
    st.write(f"Tests directory exists: {tests_dir.exists()}")
    if tests_dir.exists():
        st.write(f"Tests found: {len(test_files)}")
    else:
        st.error(f"⚠️ Tests directory not found at: {tests_dir}")

col1, col2, col3 = st.columns(3)

with col1:
    selected_sites = st.multiselect("Website", sites, default=[sites[0]] if sites else [])
with col2:
    selected_envs = st.multiselect("Environment", envs, default=[envs[0]] if envs else [])
with col3:
    selected_plats = st.multiselect("Platform", plats, default=[plats[0]] if plats else [])

run_button = st.button("▶️ Run Tests", use_container_width=True)

if run_button:
    if not selected_sites or not selected_envs or not selected_plats:
        st.error("❌ Please select at least one option for each parameter")
    else:
        # Generate all combinations
        test_combinations = []
        for site in selected_sites:
            for env in selected_envs:
                for plat in selected_plats:
                    test_name = f"{site}{env}.{plat}.test.ts"
                    test_file = tests_dir / test_name
                    if test_file.exists():
                        test_combinations.append(test_name)
                    else:
                        st.warning(f"⚠️ Test file not found: {test_name}")
        
        if test_combinations:
            st.info(f"Running {len(test_combinations)} test(s) simultaneously...")
            
            # Function to run a single test
            def run_single_test(test_name):
                try:
                    cmd = ["npx", "playwright", "test", test_name]
                    result = subprocess.run(
                        cmd,
                        cwd=str(tests_dir),
                        capture_output=True,
                        text=True,
                        timeout=300
                    )
                    return {
                        "test": test_name,
                        "returncode": result.returncode,
                        "stdout": result.stdout,
                        "stderr": result.stderr
                    }
                except subprocess.TimeoutExpired:
                    return {
                        "test": test_name,
                        "returncode": -1,
                        "stdout": "",
                        "stderr": "Test execution timed out (5 minutes)"
                    }
                except Exception as e:
                    return {
                        "test": test_name,
                        "returncode": -1,
                        "stdout": "",
                        "stderr": str(e)
                    }
            
            with st.spinner("Executing tests..."):
                # Run tests concurrently
                results = []
                with ThreadPoolExecutor(max_workers=4) as executor:
                    futures = {executor.submit(run_single_test, test): test for test in test_combinations}
                    for future in as_completed(futures):
                        results.append(future.result())
            
            # Display results
            passed_count = sum(1 for r in results if r["returncode"] == 0)
            failed_count = len(results) - passed_count
            
            st.subheader(f"Results: {passed_count} passed, {failed_count} failed")
            
            # Show results in tabs
            if passed_count > 0:
                with st.expander(f"✅ Passed Tests ({passed_count})", expanded=True):
                    for result in results:
                        if result["returncode"] == 0:
                            st.success(result["test"])
                            st.code(result["stdout"], language="text")
            
            if failed_count > 0:
                with st.expander(f"❌ Failed Tests ({failed_count})", expanded=True):
                    for result in results:
                        if result["returncode"] != 0:
                            st.error(result["test"])
                            output = result["stdout"] + result["stderr"]
                            st.code(output if output else "No output captured", language="text")

st.divider()
st.markdown("### Available Tests")
for test in test_files:
    st.code(test)
