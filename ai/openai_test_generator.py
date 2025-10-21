import openai
import os

# Load API key from environment variable (safer than hardcoding)
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_test_from_requirement_openai(requirement):
    """
    Generate a test case from natural language requirement using OpenAI.
    Returns a dict: test_name, steps, expected_result
    """
    prompt = f"Generate a detailed test case from this requirement:\n{requirement}\nFormat as steps."
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=200
        )
        text = response.choices[0].message.content
        # Split lines into steps
        steps = [line.strip() for line in text.split("\n") if line.strip()]
        return {
            "test_name": requirement[:50],
            "steps": steps,
            "expected_result": "Check system behavior"
        }
    except Exception as e:
        return {
            "test_name": requirement[:50],
            "steps": ["ERROR generating test"],
            "expected_result": str(e)
        }
