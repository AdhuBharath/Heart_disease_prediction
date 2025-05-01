import pickle
import streamlit as st

model = pickle.load(open("D:/data science/heart_disease_model.pkl", "rb"))

def main():
    st.title("Heart Disease predictive system")

    Age = st.text_input("Age_of_patient")
    Sex = 1 if st.selectbox("Select Gender", ["Male", "Female"]) == "Male" else 0
    Chest_pain_type = st.selectbox("Select Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    Chest_pain_type = {"Typical Angina": 1, "Atypical Angina": 2, "Non-Anginal Pain": 3, "Asymptomatic": 4}[Chest_pain_type]
    BP = st.text_input("Blood Pressure ")
    Cholesterol = st.text_input("Cholesterol")
    FBS_over_120 = st.selectbox("Fasting Blood Sugar", ["Yes", "No"])
    FBS_over_120 = {"Yes": 1, "No": 0}[FBS_over_120]
    EKG_results = st.selectbox("Electrocardiogram", [0, 1, 2])
    Max_HR = st.text_input("Max_Heart_Rate")
    Exercise_angina = st.selectbox("Pain_while_doing_exercise", ["Yes", "No"])
    Exercise_angina = {"Yes": 1, "No": 0}[Exercise_angina]
    ST_depression = st.text_input("ST_depression")
    Slope_of_ST = st.selectbox("Slope of ST", ["Upsloping", "Flat", "Downsloping"])
    Slope_of_ST = {"Upsloping": 1, "Flat": 2, "Downsloping": 3}[Slope_of_ST]
    Number_of_vessels_fluro = st.selectbox("number of major vessels colored by fluoroscopy", [0, 1, 2, 3])
    Thallium = st.selectbox("Thallium Stress Test Result", ["Normal", "Fixed Defect", "Reversible Defect"])
    Thallium = {"Normal": 3, "Fixed Defect": 6, "Reversible Defect": 7}[Thallium]

    # Convert input features to numeric types
    Age = int(Age)
    BP = float(BP)
    Cholesterol = float(Cholesterol)
    Max_HR = float(Max_HR)
    ST_depression = float(ST_depression)

    if st.button("Predict"):
        solution = model.predict([[Age, Sex, Chest_pain_type, BP, Cholesterol, FBS_over_120,
                                   EKG_results, Max_HR, Exercise_angina, ST_depression,
                                   Slope_of_ST, Number_of_vessels_fluro, Thallium]])
        output = solution[0]

        if output == 'Presence':
            st.write("Patient is having heart diseases.")
        else:
            st.write("Patient is not having heart diseases.")

if __name__ == "__main__":
    main()