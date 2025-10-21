import os
import subprocess

def run_in_ci():
    """
    Simulates CI test run with reporting.
    """
    print("🏗️ Starting CI pipeline...")
    os.system("pytest --maxfail=1 --disable-warnings --html=report.html")
    print("📊 Report generated: report.html")

if __name__ == "__main__":
    run_in_ci()
