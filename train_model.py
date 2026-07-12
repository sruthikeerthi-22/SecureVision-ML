import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load Dataset
data = pd.read_csv("phishing.csv")

# Features
X = data.drop("Result", axis=1)

# Target
y = data["Result"]

# Train Model
model = RandomForestClassifier()
model.fit(X, y)

# Save Model
joblib.dump(model, "model.pkl")

print("Model Trained Successfully")
print("Model Saved as model.pkl")