from keras.models import load_model
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(
    BASE_DIR,
    "models",
    "ddos_lstm_model.keras"
)

encoder_path = os.path.join(
    BASE_DIR,
    "models",
    "label_encoder.pkl"
)

model = load_model(model_path)
label_encoder = joblib.load(encoder_path)

