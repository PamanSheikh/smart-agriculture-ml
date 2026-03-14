import streamlit as st
import joblib
import numpy as np

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Smart Agriculture ML", layout="wide")
st.title("🌾 Smart Agriculture Decision Support System")
st.caption("कृषी निर्णय सहाय्य प्रणाली | Agriculture Decision Support System")

# ================= LOAD MODELS =================
crop_model = joblib.load("models/crop_model.pkl")
fert_model, le_soil, le_crop_fert, le_fert = joblib.load("models/fertilizer_model.pkl")
yield_model, le_crop_yield, le_season, le_state = joblib.load("models/yield_model.pkl")

# ================= DESCRIPTIONS =================
crop_info = {
    "Rice": "🌾 Rice / भात : Suitable for high rainfall areas. June–July sowing recommended.",
    "Wheat": "🌾 Wheat / गहू : Grows best in winter with moderate rainfall.",
    "Maize": "🌽 Maize / मका : Needs good sunlight and well-drained soil."
}

fert_info = {
    "Urea": "🧪 Urea / युरिया : Improves leaf growth and greenness.",
    "DAP": "🧪 DAP : Strengthens roots and early crop growth.",
    "MOP": "🧪 MOP : Improves crop quality and disease resistance."
}

# ================= MODE SELECTION =================
mode = st.sidebar.radio(
    "Select Mode | मोड निवडा",
    ["👨‍🌾 Farmer Mode", "👨‍🔬 Expert Mode"]
)

menu = st.sidebar.selectbox(
    "Select Feature | सुविधा निवडा",
    ["Crop Recommendation", "Fertilizer Recommendation", "Yield Prediction"]
)

# =================================================
# 🌱 CROP RECOMMENDATION
# =================================================
if menu == "Crop Recommendation":
    st.subheader("🌱 Crop Recommendation | पिक शिफारस")

    # ---------- FARMER MODE ----------
    if mode == "👨‍🌾 Farmer Mode":
        st.info("सरळ प्रश्नांची उत्तरे द्या | Answer simple questions")

        soil = st.selectbox("मातीचा प्रकार | Soil Type", ["Black / काळी", "Red / लाल", "Sandy / वालुकामय"])
        rain = st.selectbox("पावसाचे प्रमाण | Rainfall", ["Low / कमी", "Medium / मध्यम", "High / जास्त"])
        temp = st.selectbox("हवामान | Temperature", ["Cool / थंड", "Moderate / मध्यम", "Hot / गरम"])

        # Mapping to ML values
        soil_map = {
            "Black / काळी": (90, 40, 40),
            "Red / लाल": (60, 30, 30),
            "Sandy / वालुकामय": (40, 20, 20)
        }
        rain_map = {"Low / कमी": 300, "Medium / मध्यम": 700, "High / जास्त": 1200}
        temp_map = {"Cool / थंड": 20, "Moderate / मध्यम": 28, "Hot / गरम": 35}

        N, P, K = soil_map[soil]
        rainfall = rain_map[rain]
        temperature = temp_map[temp]

        humidity = 70
        ph = 6.5

        if st.button("🌾 पिक सुचवा | Recommend Crop"):
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            crop = crop_model.predict(data)[0]

            st.success(f"✅ Recommended Crop | शिफारस केलेले पिक: **{crop}**")
            st.info(crop_info.get(crop, "हे पिक आपल्या जमिनीस योग्य आहे | Suitable for your land."))

    # ---------- EXPERT MODE ----------
    else:
        N = st.number_input("Nitrogen (N)", 0, 200)
        P = st.number_input("Phosphorus (P)", 0, 200)
        K = st.number_input("Potassium (K)", 0, 200)
        temperature = st.number_input("Temperature (°C)")
        humidity = st.number_input("Humidity (%)")
        ph = st.number_input("Soil pH")
        rainfall = st.number_input("Rainfall (mm)")

        if st.button("Predict Crop"):
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            crop = crop_model.predict(data)[0]

            st.success(f"🌱 Recommended Crop: **{crop}**")
            st.info(crop_info.get(crop))

# =================================================
# 🧪 FERTILIZER RECOMMENDATION
# =================================================
elif menu == "Fertilizer Recommendation":
    st.subheader("🧪 Fertilizer Recommendation | खत शिफारस")

    soil = st.selectbox("Soil Type | मातीचा प्रकार", le_soil.classes_)
    crop = st.selectbox("Crop | पिक", le_crop_fert.classes_)

    # ---------- FARMER MODE ----------
    if mode == "👨‍🌾 Farmer Mode":
        st.info("सोपे स्लायडर वापरा | Use simple sliders")

        moisture_level = st.slider(
            "मातीतील ओलावा | Soil Moisture",
            1, 3, 2,
            help="1 = कमी, 2 = मध्यम, 3 = जास्त"
        )

        nutrient_level = st.slider(
            "पोषक तत्वांची पातळी | Nutrient Level",
            1, 3, 2,
            help="1 = कमी, 2 = मध्यम, 3 = जास्त"
        )

        # Mapping slider → ML values
        level_map = {
            1: 20,   # Low
            2: 50,   # Medium
            3: 80    # High
        }

        moisture = level_map[moisture_level]
        N = level_map[nutrient_level]
        P = level_map[3 - nutrient_level + 1]   # force variation
        K = level_map[nutrient_level]

        temp = 28
        humidity = 65

    # ---------- EXPERT MODE ----------
    else:
        temp = st.number_input("Temperature (°C)")
        humidity = st.number_input("Humidity (%)")
        moisture = st.number_input("Moisture (%)")
        N = st.number_input("Nitrogen (N)")
        K = st.number_input("Potassium (K)")
        P = st.number_input("Phosphorus (P)")

    if st.button("🧪 खत सुचवा | Recommend Fertilizer"):
        data = [[
            temp, humidity, moisture,
            le_soil.transform([soil])[0],
            le_crop_fert.transform([crop])[0],
            N, K, P
        ]]

        fert = fert_model.predict(data)[0]
        fert_name = le_fert.inverse_transform([fert])[0]

        st.success(f"🧪 Recommended Fertilizer | शिफारस: **{fert_name}**")
        st.info(fert_info.get(fert_name, "योग्य खत वापरा | Use appropriate fertilizer"))


# =================================================
# 📈 YIELD PREDICTION
# =================================================
else:
    st.subheader("📈 Yield Prediction | उत्पादन अंदाज")

    crop = st.selectbox("Crop | पिक", le_crop_yield.classes_)
    season = st.selectbox("Season | हंगाम", le_season.classes_)
    area = st.number_input("Area (Hectares) | क्षेत्र")
    rainfall = st.number_input("Rainfall (mm) | पाऊस")

    if st.button("📊 उत्पादन अंदाज"):
        data = [[
            le_crop_yield.transform([crop])[0],
            le_season.transform([season])[0],
            area,
            rainfall
        ]]
        yield_pred = yield_model.predict(data)[0]

        st.success(f"📈 Expected Yield | अपेक्षित उत्पादन: **{yield_pred:.2f} tons/hectare**")
        st.info(
            f"{crop} पिकासाठी {season} हंगामात अंदाजे "
            f"{yield_pred:.2f} टन प्रति हेक्टर उत्पादन अपेक्षित आहे."
        )
