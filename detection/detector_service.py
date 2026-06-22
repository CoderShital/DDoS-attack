from detection.ml_detector import predict
from detection.rule_engine import check_rules

def detect_attack(features):

    rule_result = check_rules(features)

    if rule_result:
        return {
            "attack": True,
            "source": "rule_engine"
        }

    ml_result = predict(features)

    if ml_result.upper() == "BENIGN":
        return {
            "attack": False,
            "source": "ml_model",
            "attack_type": ml_result
        }

    return {
        "attack": True,
        "source": "ml_model",
        "attack_type": ml_result
    }