# detection/model_loader.py

from tensorflow.keras.models import load_model
import joblib

model = load_model("models/ddos_lstm_model.keras")
encoder = joblib.load("models/label_encoder.pkl")