import pandas as pd
import joblib
import os

from sklearn.ensemble import IsolationForest

MODEL_FILE = "model.pkl"
CSV_FILE = "traffic_logs.csv"


def train_model():

    if not os.path.exists(CSV_FILE):
        return

    try:

        data = pd.read_csv(CSV_FILE)

        # minimum logs required
        if len(data) < 20:
            return

        X = data[["request_count"]]

        model = IsolationForest(
            contamination=0.1,
            random_state=42
        )

        model.fit(X)

        joblib.dump(model, MODEL_FILE)

        print("ML model trained successfully")

    except Exception as e:
        print("Training Error:", e)


def predict_attack(request_count):

    if not os.path.exists(MODEL_FILE):
        return 1

    try:

        model = joblib.load(MODEL_FILE)

        prediction = model.predict([[request_count]])

        return prediction[0]

    except Exception as e:

        print("Prediction Error:", e)

        return 1