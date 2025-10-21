import sys, os
# Add project root (parent folder of src) to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ai.predictor_engine import predict_failure

def prioritize_tests(test_data):
    """
    Sorts tests based on predicted failure probability.
    """
    predictions = []
    for t in test_data:
        # Updated for Phase 2 ML model: only execution_time & complexity
        prob = predict_failure(t["execution_time"], t["complexity"])
        predictions.append((t["id"], prob))
    
    predictions.sort(key=lambda x: x[1], reverse=True)
    
    print("\n🔥 Prioritized Test Order:")
    for test_id, prob in predictions:
        print(f"{test_id}: {prob}")
    
    return predictions

if __name__ == "__main__":
    # Dummy test data using execution_time & complexity
    dummy_tests = [
        {"id": "test_login", "execution_time": 2.3, "complexity": 8},
        {"id": "test_logout", "execution_time": 1.1, "complexity": 4}
    ]
    
    # Prioritize tests based on ML predictions
    prioritize_tests(dummy_tests)
    
    # Optional: test single prediction
    result = predict_failure(execution_time=4.5, complexity=4)
    print("\n⚙️ Predicted failure for example case:", result)
