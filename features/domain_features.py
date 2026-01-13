import whois
import datetime
from urllib.parse import urlparse

RISKY_TLDS = {"tk", "ml", "ga", "cf", "gq", "xyz", "top"}


def extract_domain(url: str) -> str:
    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    domain = domain.split(":")[0]
    return domain


def extract_domain_features(url: str) -> dict:
    domain = extract_domain(url)

    features = {
        "domain_age_days": -1,
        "domain_expiry_days": -1,
        "is_new_domain": -1,
        "is_risky_tld": 0
    }

    try:
        w = whois.whois(domain)

        creation = w.creation_date
        expiry = w.expiration_date

        if isinstance(creation, list):
            creation = creation[0]
        if isinstance(expiry, list):
            expiry = expiry[0]

        now = datetime.datetime.utcnow()

        if creation:
            age = (now - creation).days
            features["domain_age_days"] = max(age, 0)
            features["is_new_domain"] = 1 if age < 180 else 0

        if expiry:
            features["domain_expiry_days"] = (expiry - now).days

    except Exception:
        # WHOIS failures are common — do NOT crash
        pass

    # TLD risk
    tld = domain.split(".")[-1]
    if tld in RISKY_TLDS:
        features["is_risky_tld"] = 1

    return features
