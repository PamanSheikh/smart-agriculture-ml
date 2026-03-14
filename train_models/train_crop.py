import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/Crop_recommendation.csv")

# Features and target
X = df.drop("label", axis=1)
y = df["label"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate accuracy
y_pred = model.predict(X_test)
print("Crop Recommendation Model Accuracy:", accuracy_score(y_test, y_pred))

# Save model
joblib.dump(model, "models/crop_model.pkl")
print("✅ Crop model saved successfully")
