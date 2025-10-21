import json
from pathlib import Path

TEMPLATES = {
    "login": [
        {
            "id": "test_login_valid",
            "description": "Verify user can login with valid credentials",
            "steps": [
                "Open browser",
                "Navigate to login page",
                "Enter valid username and password",
                "Click login button",
                "Verify dashboard is visible"
            ]
        }
    ],
    "logout": [
        {
            "id": "test_logout",
            "description": "Verify user can logout successfully",
            "steps": [
                "Login with valid credentials",
                "Click logout button",
                "Verify redirected to login page"
            ]
        }
    ]
}

def generate_test(feature, output_dir="tests/generated"):
    """
    Generates test cases based on predefined templates.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    generated = []
    if feature in TEMPLATES:
        for t in TEMPLATES[feature]:
            file = Path(output_dir) / f"{t['id']}.json"
            json.dump(t, open(file, "w"), indent=2)
            print(f"📝 Generated {file}")
            generated.append(file)
    return generated

if __name__ == "__main__":
    generate_test("login")
