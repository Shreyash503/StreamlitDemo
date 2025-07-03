import streamlit as st
import pickle

st.title('Insurance Premium Prediction App')

# Input fields
age = st.number_input('Enter your age:', min_value=1, max_value=120, value=25)

gender = st.radio('Select gender:', ['male', 'female'], horizontal=True)
gender = 0 if gender == 'male' else 1

bmi = st.number_input('Enter BMI:', min_value=10.0, max_value=60.0, value=25.0)

children = st.number_input('Enter number of children:', min_value=0, max_value=10, value=0)

smoker = st.radio('Do you smoke?', ['yes', 'no'], horizontal=True)
smoker = 1 if smoker == 'yes' else 0

# Prepare input
X_test = [[age, gender, bmi, children, smoker]]

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

# Prediction button
if st.button('Predict Insurance Premium'):
    yp = model.predict(X_test)
    st.write('Predicted Insurance Premium:', yp[0])
