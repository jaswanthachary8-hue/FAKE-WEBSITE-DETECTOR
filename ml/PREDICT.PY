import joblib
import numpy as np
from features.feature_extractor import extract_features

MODEL_PATH = "ml/phishing_model.pkl"


def load_model():
    """Load the trained model from disk."""
    try:
        model = joblib.load(MODEL_PATH)
        return model
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Model not found at {MODEL_PATH}. Please train the model first using ml/train_model.py"
        )


def predict(url: str) -> dict:
    """
    Predict if a URL is phishing or legitimate.
    
    Args:
        url: The URL to check
        
    Returns:
        dict with 'prediction' (0=legitimate, 1=phishing), 'probability', and 'confidence'
    """
    model = load_model()
    
    # Extract features
    features = extract_features(url)
    
    # Convert to numpy array in the correct order
    feature_order = [
        "url_length", "has_ip", "at_count", "dash_count", "dot_count",
        "subdomain_count", "has_shortener", "suspicious_word_count",
        "domain_age_days", "domain_expiry_days", "is_new_domain", "is_risky_tld",
        "has_form", "has_password_input", "external_form_action",
        "iframe_count", "external_script_count", "keyword_count"
    ]
    
    feature_vector = np.array([[features.get(key, -1) for key in feature_order]])
    
    # Predict
    prediction = model.predict(feature_vector)[0]
    probabilities = model.predict_proba(feature_vector)[0]
    
    # Get confidence (probability of predicted class)
    confidence = float(probabilities[prediction])
    
    result = {
        "prediction": int(prediction),
        "label": "Phishing" if prediction == 1 else "Legitimate",
        "confidence": round(confidence * 100, 2),
        "probabilities": {
            "legitimate": round(probabilities[0] * 100, 2),
            "phishing": round(probabilities[1] * 100, 2)
        }
    }
    
    return result


if __name__ == "__main__":
    # Test prediction
    test_urls = [
        "https://www.google.com",
        "http://secure-login-paypal.verify-user.xyz"
    ]
    
    print("Testing predictions...\n")
    for url in test_urls:
        result = predict(url)
        print(f"URL: {url}")
        print(f"Prediction: {result['label']}")
        print(f"Confidence: {result['confidence']}%")
        print(f"Probabilities: Legitimate={result['probabilities']['legitimate']}%, Phishing={result['probabilities']['phishing']}%")
        print("-" * 50)
