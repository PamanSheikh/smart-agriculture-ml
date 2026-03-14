import pandas as pd
import joblib
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/fertilizer.csv")

# Encode categorical features
le_soil = LabelEncoder()
le_crop = LabelEncoder()
le_fert = LabelEncoder()

df["Soil Type"] = le_soil.fit_transform(df["Soil Type"])
df["Crop Type"] = le_crop.fit_transform(df["Crop Type"])
df["Fertilizer Name"] = le_fert.fit_transform(df["Fertilizer Name"])

# Features and target
X = df.drop("Fertilizer Name", axis=1)
y = df["Fertilizer Name"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Decision Tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("Fertilizer Model Accuracy:", accuracy_score(y_test, y_pred))

# Save model + encoders
joblib.dump((model, le_soil, le_crop, le_fert), "models/fertilizer_model.pkl")
print("✅ Fertilizer model saved successfully")
