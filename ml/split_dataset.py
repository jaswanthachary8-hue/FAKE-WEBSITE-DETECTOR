import pandas as pd
from sklearn.model_selection import train_test_split

# Load Kaggle dataset
df = pd.read_csv("dataset/phishing_site_urls.csv")  # adjust filename

print(df['Label'].value_counts())  # sanity check
