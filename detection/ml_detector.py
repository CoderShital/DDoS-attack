from models.model_loader import model, label_encoder
import numpy as np


def predict(features):

    # Convert to numpy array
    features = np.array(features, dtype=np.float32)

    # IMPORTANT:
    # Model expects (samples, 77, 1)

    features = features.reshape(1, 77, 1)

    prediction = model.predict(features, verbose=0)

    predicted_class = np.argmax(prediction, axis=1)

    attack_label = label_encoder.inverse_transform(predicted_class)

    return attack_label[0]