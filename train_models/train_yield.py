import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv("data/crop_yield.csv").dropna()

# Encode categorical features
le_crop = LabelEncoder()
le_season = LabelEncoder()
le_state = LabelEncoder()

df["Crop"] = le_crop.fit_transform(df["Crop"])
df["Season"] = le_season.fit_transform(df["Season"])
df["State"] = le_state.fit_transform(df["State"])

# Features and target
X = df[["Crop", "Season", "Area", "Annual_Rainfall"]]
y = df["Yield"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest Regressor
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Yield Model MSE:", mse)

# Save model + encoders
joblib.dump((model, le_crop, le_season, le_state), "models/yield_model.pkl")
print("✅ Yield model saved successfully")
