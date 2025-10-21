import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

def generate_test_from_requirement(requirement: str):
    """
    Convert a natural language requirement into a structured test case.
    """
    doc = nlp(requirement)
    test_case = {
        "test_name": requirement[:30] + "...",
        "steps": [],
        "expected_result": ""
    }

    for sent in doc.sents:
        if "should" in sent.text.lower():
            test_case["steps"].append(sent.text)
        if "verify" in sent.text.lower() or "expect" in sent.text.lower():
            test_case["expected_result"] = sent.text

    return test_case

# Optional test
if __name__ == "__main__":
    example = "User should login with valid credentials. Verify dashboard loads."
    print(generate_test_from_requirement(example))
