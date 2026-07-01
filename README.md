# diabetes-predictor
Diabetes risk prediction web app built with Streamlit and scikit-learn


Diabetes Risk Predictor
A machine learning web application that predicts the likelihood of diabetes in a patient based on 8 clinical features including glucose level, BMI, age, insulin, blood pressure, and family history (diabetes pedigree function).
How it works:
The app is powered by a class-weighted Random Forest model trained on the Pima Indians Diabetes dataset (768 patients). The model achieves 77.2% cross-validated accuracy and 67.3% sensitivity. Class weighting was applied during training to reduce missed diabetic patients — prioritising sensitivity over raw accuracy, since an undiagnosed diabetic patient carries far greater clinical risk than a false alarm.
A user enters a patient's clinical measurements into the form, clicks Predict, and the app returns an instant risk assessment with a probability score — for example, "High risk of diabetes — 82.0% probability."
Key finding: Glucose level was the strongest predictor of diabetes in this dataset, followed by BMI and age — consistent with established clinical understanding of Type 2 diabetes risk factors.
Built with: Python, scikit-learn, Pandas, Streamlit
Deployed at: https://diabetes-predictor-kingkayd.streamlit.app/
Dataset: Pima Indians Diabetes Dataset — originally from the National Institute of Diabetes and Digestive and Kidney Diseases
