# 🚢 Titanic Survival Prediction App

This Streamlit app predicts whether a passenger would have survived the Titanic tragedy based on key information like age, gender, ticket class, and fare paid.

---

## 📌 Features

- Interactive web interface built using **Streamlit**
- Predicts survival using a trained **Machine Learning model**
- Input fields for all key features: age, gender, fare, embarked port, etc.
- Dynamic response with styled output for predicted results
- Special warning message if all inputs are empty
- Lightweight and deployable to **Streamlit Cloud** or other platforms

---

## 🧠 Machine Learning Model

The model (`model.pkl`) is trained on the Titanic dataset with the following features:
- `Pclass` (Ticket Class)
- `Sex` (Gender)
- `Age`
- `SibSp` (Siblings/Spouses Aboard)
- `Parch` (Parents/Children Aboard)
- `Fare`
- `Embarked` (Port of Embarkation)

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/titanic-survival-app.git
cd titanic-survival-app
```
2. Install Dependencies
```bash

pip install -r requirements.txt
```
4. Run the App
```bash

streamlit run app.py
```
📁 File Structure
```bash

├── app.py                # Main Streamlit app
├── model.pkl             # Pre-trained ML model
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```
```
⚠️ Null Input Handling
If the user submits the form without entering any details (i.e., all values default), the app will display a special message:

"🚢 You're on the ship, but we don't know who you are!"
