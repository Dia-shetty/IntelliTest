import json
import subprocess
from pathlib import Path

def run_test_case(file_path):
    """
    Runs a generated test case file using pytest.
    """
    print(f"🧪 Running test case: {file_path}")
    result = subprocess.run(["pytest", str(file_path), "--maxfail=1", "--disable-warnings", "-q"])
    if result.returncode == 0:
        print(f"✅ Test passed: {file_path}")
    else:
        print(f"❌ Test failed: {file_path}")
    return result.returncode

def run_all_tests(directory="tests/generated"):
    """
    Runs all test cases inside the given directory.
    """
    for file in Path(directory).glob("*.json"):
        run_test_case(file)

if __name__ == "__main__":
    run_all_tests()
