import pandas as pd
import os

# paths
INPUT_CSV = "dataset/phishing_site_urls.csv"   # rename if needed
LEGIT_FILE = "dataset/urls/legit.txt"
PHISH_FILE = "dataset/urls/phishing.txt"

# ensure folder exists
os.makedirs("dataset/urls", exist_ok=True)

# load data
df = pd.read_csv(INPUT_CSV)

# sanity check
print(df["Label"].value_counts())

# split
legit_urls = df[df["Label"] == "good"]["URL"]
phish_urls = df[df["Label"] == "bad"]["URL"]

# save
legit_urls.to_csv(LEGIT_FILE, index=False, header=False)
phish_urls.to_csv(PHISH_FILE, index=False, header=False)

print("Done.")
print(f"Legit URLs: {len(legit_urls)}")
print(f"Phishing URLs: {len(phish_urls)}")
