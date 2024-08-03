import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    countries = (
        "United States of America",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Canada",
        "India",
        "France",
        "Netherlands",
        "Australia",
        "Brazil",
        "Spain",
        "Sweden",
        "Italy",
        "Poland",
        "Other",
        "Switzerland",
        "Denmark",
        "Norway",
        "Israel",
        "Portugal",
        "Austria",
        "Finland",
        "Belgium",
        "Russian Federation",
        "New Zealand",
        "Ukraine",
        "Turkey",
        "Czech Republic",
        "South Africa",
        "Greece",
        "Romania",
        "Ireland",
        "Mexico",
        "Hungary",
        "Colombia",
        "Argentina",
        "Bulgaria",
        "Pakistan",
        "Iran, Islamic Republic of...",
        "Japan",
        "Serbia",
        "Lithuania",
        "China",
        "Singapore",
        "Bangladesh",
        "Indonesia",
        "Croatia",
        "Estonia",
        "Chile",
        "Slovenia",
        "Philippines",
        "Viet Nam",
        "Malaysia",
        "Slovakia",
        "Taiwan",
        "Latvia",
        "Thailand",
        "South Korea",
        "Sri Lanka",
        "Hong Kong (S.A.R.)",
        "Georgia",
        "United Arab Emirates",
        "Egypt",
        "Nigeria",
        "Uruguay",
        "Nepal",
        "Peru",
        "Kenya",
        "Armenia",
        "Costa Rica",
        "Republic of Korea",
        "Bosnia and Herzegovina",
        "Venezuela, Bolivarian Republic of...",
        "Cyprus",
        "Morocco",
        "Luxembourg",
        "Ecuador",
        "Belarus",
        "Kazakhstan",
        "Tunisia"
    )

    education = (
        "Less than a Bachelors",
        "Bachelor’s degree",
        "Master’s degree",
        "Post grad",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)

    expericence = st.slider("Years of Experience", 0, 30, 3)

    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")