from features.feature_extractor import extract_features

url = "https://www.google.com"
features = extract_features(url)

for k, v in features.items():
    print(f"{k}: {v}")
