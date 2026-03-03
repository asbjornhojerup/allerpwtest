import streamlit as st
import subprocess
from pathlib import Path
import os

# Get paths
project_root = Path(__file__).parent.parent
tests_dir = project_root / "tests"

# Parse test files to extract site/env/platform combinations
test_files = sorted([f.name for f in tests_dir.glob("*.test.ts")])

# Extract unique values
sites = sorted(list(set([f[0:2] for f in test_files])))
envs = sorted(list(set([f.split('.')[0][2:] for f in test_files])))
plats = sorted(list(set([f.split('.')[1] for f in test_files])))

st.set_page_config(page_title="Playwright Test Runner", layout="wide")

st.title("🎭 Playwright Test Runner")
st.markdown("Select parameters and run E2E tests")

col1, col2, col3 = st.columns(3)

with col1:
    # allow single or multiple sites
    site = st.multiselect("Website", sites, default=sites[0])
with col2:
    env = st.multiselect("Environment", envs, default=envs[0])
with col3:
    plat = st.multiselect("Platform", plats, default=plats[0])

run_button = st.button("▶️ Run Test", use_container_width=True)

# option to run in parallel if multiple sites selected
parallel = st.checkbox("Run tests concurrently (multi-worker)", value=False)

if run_button:
    # support running multiple sites at once
    selected_sites = site if isinstance(site, list) else [site]
    selected_envs = env if isinstance(env, list) else [env]
    selected_plats = plat if isinstance(plat, list) else [plat]

    def run_test(s: str, e: str, p: str) -> tuple[str, str, int]:
        """Invoke playwright for a single test combination and return (name, output, returncode)."""
        test_name = f"{s}{e}.{p}.test.ts"
        test_file = tests_dir / test_name
        if not test_file.exists():
            return (test_name, f"❌ Test file not found", -1)
        cmd = ["npx", "playwright", "test", test_name]
        proc = subprocess.run(
            cmd,
            cwd=str(tests_dir),
            capture_output=True,
            text=True,
            timeout=300
        )
        return (test_name, proc.stdout + proc.stderr, proc.returncode)

    # build list of all combinations
    combos = [(s, e, p) for s in selected_sites for e in selected_envs for p in selected_plats]

    def run_combo(args):
        s, e, p = args
        return run_test(s, e, p)

    if parallel and len(combos) > 1:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        futures = []
        with ThreadPoolExecutor(max_workers=len(combos)) as exec:
            for combo in combos:
                futures.append(exec.submit(run_combo, combo))

            for fut in as_completed(futures):
                test_name, output, code = fut.result()
                if code == -1:
                    st.error(f"❌ {test_name} not found")
                    continue
                if code == 0:
                    st.success(f"✅ {test_name} passed!")
                else:
                    st.error(f"❌ {test_name} failed (code {code})")
                st.subheader(f"Output for {test_name}")
                st.code(output, language="text")
    else:
        for combo in combos:
            test_name, output, code = run_combo(combo)
            if code == -1:
                st.error(f"❌ {test_name} not found")
                continue
            if code == 0:
                st.success(f"✅ {test_name} passed!")
            else:
                st.error(f"❌ {test_name} failed (code {code})")
            st.subheader(f"Output for {test_name}")
            st.code(output, language="text")

st.divider()
st.markdown("### Available Tests")
for test in test_files:
    st.code(test)
