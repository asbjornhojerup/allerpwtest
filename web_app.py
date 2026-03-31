from flask import Flask, render_template, request
import subprocess
from pathlib import Path
import os
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
import shutil

app = Flask(__name__)


def discover_tests():
    script_dir = Path(__file__).parent
    project_root = script_dir
    tests_dir = project_root / "tests"
    if not tests_dir.exists():
        tests_dir = Path.cwd() / "tests"
    test_files = sorted([f.name for f in tests_dir.glob("*.test.ts")])
    sites = sorted(list(set([f[0:2] for f in test_files])))
    envs = sorted(list(set([f.split('.')[0][2:] for f in test_files])))
    plats = sorted(list(set([f.split('.')[1] for f in test_files])))
    return tests_dir, test_files, sites, envs, plats


def run_single_test(tests_dir, test_name):
    try:
        project_root = Path(__file__).parent
        playwright_bin = project_root / "node_modules" / ".bin" / "playwright"
        cmd = [str(playwright_bin), "test", str(tests_dir / test_name),
               "--project=chromium", "--workers=2", "--reporter=json"]
        result = subprocess.run(
            cmd,
            cwd=str(project_root),
            capture_output=True,
            text=True,
            timeout=300
        )
        tests = []
        try:
            data = json.loads(result.stdout)
            ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
            def walk(suites):
                for s in suites:
                    for spec in s.get("specs", []):
                        error = None
                        if not spec["ok"]:
                            for t in spec.get("tests", []):
                                for r in t.get("results", []):
                                    msg = (r.get("error") or {}).get("message", "")
                                    if msg:
                                        error = ansi_escape.sub("", msg)
                                        break
                                if error:
                                    break
                        tests.append({"title": spec["title"], "ok": spec["ok"], "error": error})
                    walk(s.get("suites", []))
            walk(data.get("suites", []))
        except (json.JSONDecodeError, KeyError):
            pass
        return {"test": test_name, "returncode": result.returncode, "tests": tests}
    except subprocess.TimeoutExpired:
        return {"test": test_name, "returncode": -1, "stdout": "", "stderr": "Timeout"}
    except Exception as e:
        return {"test": test_name, "returncode": -1, "stdout": "", "stderr": str(e)}


@app.route("/", methods=["GET", "POST"])
def index():
    tests_dir, test_files, sites, envs, plats = discover_tests()
    if not shutil.which("npx"):
        return ("<h2>npx is not available</h2>" 
                "<p>Install Node.js/npm or run this server where it's available.</p>")
    results = None
    errors = []
    if request.method == "POST":
        selected_site = request.form.get("site", "").strip()
        selected_envs = request.form.getlist("env")
        selected_plats = request.form.getlist("plat")
        
        if not (selected_site and selected_envs and selected_plats):
            errors.append("You must select a site and at least one environment and platform")
        else:
            combos = []
            for env in selected_envs:
                for plat in selected_plats:
                    test_name = f"{selected_site}{env}.{plat}.test.ts"
                    test_file = tests_dir / test_name
                    if test_file.exists():
                        combos.append(test_name)
                    else:
                        errors.append(f"Test not found: {test_name}")
            
            if combos:
                results = []
                with ThreadPoolExecutor(max_workers=4) as executor:
                    futures = {executor.submit(run_single_test, tests_dir, t): t for t in combos}
                    for future in as_completed(futures):
                        results.append(future.result())
    
    return render_template("index.html", sites=sites, envs=envs,
                           plats=plats, results=results, errors=errors)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
