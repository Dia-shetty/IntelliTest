import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import os

def train_failure_model():
    data_path = os.path.join("data", "sample_test_data.csv")
    df = pd.read_csv(data_path)

    # Features and labels
    X = df[["execution_time", "complexity"]]
    y = df["failed"]

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"✅ Model trained with accuracy: {accuracy*100:.2f}%")

    # Save model
    os.makedirs("ai/models", exist_ok=True)
    joblib.dump(model, "ai/models/failure_predictor.joblib")
    print("💾 Model saved as ai/models/failure_predictor.joblib")

if __name__ == "__main__":
    train_failure_model()
