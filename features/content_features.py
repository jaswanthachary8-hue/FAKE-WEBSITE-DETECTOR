import requests
import tldextract
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from utils.keywords import PHISHING_KEYWORDS

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def extract_content_features(url: str) -> dict:
    features = {
        "has_form": 0,
        "has_password_input": 0,
        "external_form_action": 0,
        "iframe_count": 0,
        "external_script_count": 0,
        "keyword_count": 0
    }

    try:
        response = requests.get(url, headers=HEADERS, timeout=8)
        html = response.text
    except Exception:
        return features  # fail safe

    soup = BeautifulSoup(html, "lxml")
    parsed_url = urlparse(url)
    base_domain = parsed_url.netloc

    # ---------- Forms & inputs ----------
    forms = soup.find_all("form")
    features["has_form"] = 1 if forms else 0

    for form in forms:
        inputs = form.find_all("input")
        for inp in inputs:
            if inp.get("type") == "password":
                features["has_password_input"] = 1

        action = form.get("action")
        if action:
            action_url = urljoin(url, action)
            if urlparse(action_url).netloc != base_domain:
                features["external_form_action"] = 1

    # ---------- Iframes ----------
    features["iframe_count"] = len(soup.find_all("iframe"))

    # ---------- External scripts (FIXED) ----------
    base_ext = tldextract.extract(base_domain)
    base_root = f"{base_ext.domain}.{base_ext.suffix}"

    scripts = soup.find_all("script", src=True)
    for script in scripts:
        src = script.get("src")
        if not src:
            continue

        src_domain = urlparse(src).netloc
        if not src_domain:
            continue

        src_ext = tldextract.extract(src_domain)
        src_root = f"{src_ext.domain}.{src_ext.suffix}"

        if src_root != base_root:
            features["external_script_count"] += 1

    # ---------- Keyword analysis ----------
    text = soup.get_text().lower()
    for word in PHISHING_KEYWORDS:
        features["keyword_count"] += text.count(word)

    return features
