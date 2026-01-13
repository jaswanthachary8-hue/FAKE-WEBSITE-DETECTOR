from features.url_features import extract_url_features
from features.domain_features import extract_domain_features
from features.content_features import extract_content_features


FEATURE_ORDER = [
    # URL features
    "url_length",
    "has_ip",
    "at_count",
    "dash_count",
    "dot_count",
    "subdomain_count",
    "has_shortener",
    "suspicious_word_count",

    # Domain features
    "domain_age_days",
    "domain_expiry_days",
    "is_new_domain",
    "is_risky_tld",

    # Content features
    "has_form",
    "has_password_input",
    "external_form_action",
    "iframe_count",
    "external_script_count",
    "keyword_count"
]


def extract_features(url: str) -> dict:
    features = {}

    url_features = extract_url_features(url)
    domain_features = extract_domain_features(url)
    content_features = extract_content_features(url)

    features.update(url_features)
    features.update(domain_features)
    features.update(content_features)

    # Enforce fixed order and missing keys
    final_features = {}
    for key in FEATURE_ORDER:
        final_features[key] = features.get(key, -1)

    return final_features
