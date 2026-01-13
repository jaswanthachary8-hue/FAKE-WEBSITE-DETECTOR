import csv
from features.feature_extractor import extract_features

URLS = [
    # Legitimate (label = 0)
    ("https://www.google.com", 0),
    ("https://www.wikipedia.org", 0),
    ("https://github.com", 0),
    ("https://stackoverflow.com", 0),

    # Phishing-like (label = 1)
    ("http://secure-login-paypal.verify-user.xyz", 1),
    ("http://account-update-google.security-alerts.ru", 1),
    ("http://login-facebook.session-expired.tk", 1),
    ("http://appleid.apple.verify-now.ga", 1),
]


OUTPUT_FILE = "dataset/phishing_dataset.csv"


def generate():
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        header = list(extract_features(URLS[0][0]).keys()) + ["label"]
        writer.writerow(header)

        for url, label in URLS:
            features = extract_features(url)
            row = list(features.values()) + [label]
            writer.writerow(row)


if __name__ == "__main__":
    generate()
