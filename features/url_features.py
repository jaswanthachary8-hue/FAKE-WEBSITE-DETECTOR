import re
from urllib.parse import urlparse

SHORTENERS = [
    "bit.ly", "tinyurl", "goo.gl", "t.co", "ow.ly", "is.gd"
]

SUSPICIOUS_WORDS = [
    "login", "secure", "verify", "account", "update",
    "bank", "signin", "confirm", "password"
]


def has_ip_address(url: str) -> int:
    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    return 1 if re.search(ip_pattern, url) else 0


def count_subdomains(url: str) -> int:
    parsed = urlparse(url)
    host = parsed.netloc.lower()

    # remove port if present
    host = host.split(":")[0]

    parts = host.split(".")

    if len(parts) <= 2:
        return 0

    # ignore common benign subdomains
    benign = {"www", "mail", "ftp"}
    subdomains = parts[:-2]

    return sum(1 for p in subdomains if p not in benign)


def has_url_shortener(url: str) -> int:
    for shortener in SHORTENERS:
        if shortener in url.lower():
            return 1
    return 0


def suspicious_words_count(url: str) -> int:
    url = url.lower()
    return sum(word in url for word in SUSPICIOUS_WORDS)


def extract_url_features(url: str) -> dict:
    return {
        "url_length": len(url),
        "has_ip": has_ip_address(url),
        "at_count": url.count("@"),
        "dash_count": url.count("-"),
        "dot_count": url.count("."),
        "subdomain_count": count_subdomains(url),
        "has_shortener": has_url_shortener(url),
        "suspicious_word_count": suspicious_words_count(url)
    }
