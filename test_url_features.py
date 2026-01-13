from features.url_features import extract_url_features

test_urls = [
    "https://www.google.com",
    "http://192.168.1.10/login",
    "https://secure-login-paypal.verify-user.xyz/account",
    "bit.ly/3Hd92Ls",
    "https://example.com"
]

for url in test_urls:
    print("=" * 60)
    print("URL:", url)
    features = extract_url_features(url)
    for k, v in features.items():
        print(f"{k}: {v}")

from features.domain_features import extract_domain_features

print("\nDOMAIN FEATURE TEST")
print("=" * 60)
print("Google:", extract_domain_features("https://www.google.com"))
print("Phishing:", extract_domain_features("https://secure-login-paypal.verify-user.xyz"))

from features.content_features import extract_content_features

print("\nCONTENT FEATURE TEST")
print("=" * 60)
print("Google:", extract_content_features("https://www.google.com"))
print("Phishing-like:", extract_content_features("https://secure-login-paypal.verify-user.xyz"))
