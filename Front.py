import streamlit as st
import math
import pickle

# Set page configuration (must be first)
st.set_page_config(page_title="Titanic Survival Predictor", page_icon="🚢", layout="wide")

# Load model
with open("model.pkl", 'rb') as f:
    model = pickle.load(f)

# Header
st.header("Titanic Survival Prediction !!")
st.image("https://upload.wikimedia.org/wikipedia/commons/f/fd/RMS_Titanic_3.jpg", use_container_width=True)

st.markdown("<h1 style='text-align: center; color: #00416A;'>🚢 Titanic Survival Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter passenger details below to predict whether they would have survived the Titanic tragedy.</p>", unsafe_allow_html=True)
st.markdown("---")

# Passenger Input
st.subheader("🧾 Passenger Information")
col1, col2, col3 = st.columns(3)

with col1:
    Pclass = st.selectbox("Ticket Class", ("Premiere", "Executive", "Economy"),
                          help="Premiere = 1st class, Executive = 2nd, Economy = 3rd")
with col2:
    Sex = st.selectbox("Gender", ("Male", "Female"))
with col3:
    Age = st.number_input("Age", min_value=0.0, step=1.0, help="Enter the age of the passenger")

col4, col5 = st.columns(2)
with col4:
    SibSp = st.number_input("Siblings / Spouses Aboard", min_value=0, step=1)
with col5:
    Parch = st.number_input("Parents / Children Aboard", min_value=0, step=1)

col6, col7 = st.columns(2)
with col6:
    Fare = st.number_input("Fare Paid (£)", min_value=0.0, help="Total fare the passenger paid")
with col7:
    Embarked = st.selectbox("Port of Embarkation", ("Cherbourg", "Queenstown", "Southampton"))

st.markdown("---")

# Prediction Button Logic
if st.button("🎯 Predict Survival"):
    try:
        # Encode values
        pclass = {"Premiere": 1, "Executive": 2, "Economy": 3}[Pclass]
        gender = 1 if Sex == "Female" else 0
        age = math.ceil(Age)
        sibsp = math.ceil(SibSp)
        parch = math.ceil(Parch)
        fare = math.ceil(Fare)
        embarked = {"Cherbourg": 1, "Queenstown": 2, "Southampton": 0}[Embarked]

        # Check for empty input
        if Age == 0.0 and SibSp == 0 and Parch == 0 and Fare == 0.0:
            st.markdown("""
                <div style='background-color:#FFF3CD; padding:20px; border-radius:10px; border:1px solid #856404'>
                    <h3 style='color:#856404;'>🚢 You're on the ship, but we don't know who you are!</h3>
                    <p style='color:#856404;'>Please enter your details above to get a survival prediction.</p>
                </div>
            """, unsafe_allow_html=True)
            st.stop()

        # Make prediction
        result = model.predict([[pclass, gender, age, sibsp, parch, fare, embarked]])[0]

        # Show prediction
        if result == 1:
            st.markdown("""
                <div style='background-color:#D4EDDA; padding:20px; border-radius:10px; border:1px solid #155724'>
                    <h3 style='color:#155724;'>🎉 Prediction: The passenger would have <u>SURVIVED</u>.</h3>
                    <p style='color:#155724;'>There's a good chance they made it out alive.</p>
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown("""
                <div style='background-color:#F8D7DA; padding:20px; border-radius:10px; border:1px solid #721C24'>
                    <h3 style='color:#721C24;'>💀 Prediction: The passenger would <u>NOT have survived</u>.</h3>
                    <p style='color:#721C24;'>Unfortunately, the odds were against them.</p>
                </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ An error occurred during prediction: {e}")

# Feature Mappings Info
with st.expander("ℹ️ Feature Mapping Info"):
    st.markdown("""
    - **Ticket Class**: Premiere = 1, Executive = 2, Economy = 3  
    - **Gender**: Male = 0, Female = 1  
    - **Embarked**: Cherbourg = 1, Queenstown = 2, Southampton = 0
    """)

