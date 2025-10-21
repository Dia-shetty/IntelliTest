import joblib
import os
import numpy as np

def predict_failure(execution_time, complexity):
    model_path = os.path.join("ai", "models", "failure_predictor.joblib")

    if not os.path.exists(model_path):
        raise FileNotFoundError("❌ Model not found! Run model_trainer.py first.")

    model = joblib.load(model_path)
    prediction = model.predict(np.array([[execution_time, complexity]]))[0]

    return bool(prediction)
