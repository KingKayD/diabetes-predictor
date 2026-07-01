import streamlit as st
import joblib
import pandas as pd

st.title("Diabetes Risk Predictor")
st.write("Enter patient details below to assess diabetes risk.")

# Load saved model and scaler
model = joblib.load("diabetes_model.pkl")
scaler = joblib.load("diabetes_scaler.pkl")

st.header("Enter Patient Information")

pregnancies = st.number_input("Number of Pregnancies", 
              min_value=0, max_value=20, value=1)
glucose = st.number_input("Glucose Level (mg/dL)", 
          min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure (mmHg)", 
                 min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness (mm)", 
                 min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin Level (µU/mL)", 
          min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", 
      min_value=0.0, max_value=70.0, value=25.0, step=0.1)
diabetes_pedigree = st.number_input("Diabetes Pedigree Function", 
                    min_value=0.0, max_value=3.0, 
                    value=0.5, step=0.01)
age = st.number_input("Age", 
      min_value=1, max_value=120, value=30)

if st.button("Predict"):
    # Build patient row in exact column order model was trained on
    patient = pd.DataFrame([[pregnancies, glucose, blood_pressure,
                              skin_thickness, insulin, bmi,
                              diabetes_pedigree, age]],
                            columns=['pregnancies', 'glucose',
                                     'blood_pressure', 'skin_thickness',
                                     'insulin', 'bmi',
                                     'diabetes_pedigree', 'age'])

    patient_scaled = scaler.transform(patient)
    prediction = model.predict(patient_scaled)[0]
    probability = model.predict_proba(patient_scaled)[0][1]

    if prediction == 1:
        st.error(f"High risk of diabetes — {probability*100:.1f}% probability")
    else:
        st.success(f"Low risk of diabetes — {probability*100:.1f}% probability")