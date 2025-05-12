import streamlit as st
import numpy as np
import joblib

st.title("Mobile Price Prediction App")
st.write("Fill in the details below to predict the price category of a mobile device.")

# Load the logistic regression model
model = joblib.load("logistic_regression_model.pkl")

# User inputs
battery_power = st.number_input('Battery Power (mAh)', min_value=0, key="battery_power")
int_memory = st.number_input("Internal Memory (GB)", min_value=0, key="int_memory")
mobile_wt = st.number_input("Mobile Weight (grams)", min_value=0, key="mobile_wt")
n_cores = st.number_input("Number of Cores", min_value=1, key="n_cores")
px_height = st.number_input("Pixel Height", min_value=0, key="px_height")
px_width = st.number_input("Pixel Width", min_value=0, key="px_width")
ram = st.number_input("RAM (MB)", min_value=0, key="ram")
sc_h = st.number_input("Screen Height (cm)", min_value=0, key="sc_h")
sc_w = st.number_input("Screen Width (cm)", min_value=0, key="sc_w")
talk_time = st.number_input("Talk Time (hours)", min_value=0, key="talk_time")
fc = st.number_input("Front Camera (MP)", min_value=0, key="fc")
pc = st.number_input("Primary Camera (MP)", min_value=0, key="pc")
m_dep = st.number_input("Mobile Depth (cm)", min_value=0, key="m_dep")

three_g = st.selectbox("3G Support", [0, 1], key="three_g")
four_g = st.selectbox("4G Support", [0, 1], key="four_g")
touch_screen = st.selectbox("Touch Screen", [0, 1], key="touch_screen")
wifi = st.selectbox("WiFi Support", [0, 1], key="wifi")
blue = st.selectbox("Bluetooth Support", [0, 1], key="blue")
dual_sim = st.selectbox("Dual SIM Support", [0, 1], key="dual_sim")

# Prepare the feature vector
features = np.array([[battery_power, int_memory, mobile_wt, n_cores, px_height, px_width,
                      ram, sc_h, sc_w, talk_time, three_g, four_g, touch_screen, wifi, blue, dual_sim,
                      fc, pc, m_dep, mobile_wt]])

# Predict button
if st.button("Predict Price Category"):
    prediction = model.predict(features)
    st.success(f"The predicted price category is: {prediction[0]}")

# Path to the Python Scripts directory
python_scripts_path = r"C:\Users\<VotreNomUtilisateur>\AppData\Local\Programs\Python\PythonXX\Scripts"