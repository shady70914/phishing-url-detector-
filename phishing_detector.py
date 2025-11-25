import pandas as pd
import numpy as np
import re
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# ---------------------------
# 1. Load Dataset
# ---------------------------
data = pd.read_csv("dataset.csv")

X = data.drop("label", axis=1)
y = data["label"]

# ---------------------------
# 2. Train Model
# ---------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model Accuracy:", accuracy_score(y_test, model.predict(X_test)))

# ---------------------------
# 3. Feature Extraction for new URL
# ---------------------------
def extract_features(url):
    features = {
        "url_length": len(url),
        "has_ip": 1 if re.match(r"^\d+\.\d+\.\d+\.\d+$", url) else 0,
        "num_dots": url.count("."),
        "has_at": 1 if "@" in url else 0,
        "has_https": 1 if "https" in url else 0,
        "num_slashes": url.count("/"),
        "suspicious_chars": url.count("?") + url.count("=")
    }
    return pd.DataFrame([features])

# ---------------------------
# 4. Predict Function
# ---------------------------
while True:
    url = input("\nEnter URL: ")
    features = extract_features(url)
    prediction = model.predict(features)[0]

    if prediction == 0:
        print("✔ SAFE URL")
    else:
        print("⚠ MALICIOUS URL!")
