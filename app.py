import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open("diamond_knn_model.pkl", "rb"))

st.title("💎 Diamond Price Prediction App")

st.write("Enter Diamond Details")

# Numerical Inputs
carat = st.number_input("Carat", min_value=0.1, max_value=5.0, value=0.5)

depth = st.number_input("Depth", min_value=40.0, max_value=80.0, value=61.5)

table = st.number_input("Table", min_value=40.0, max_value=80.0, value=55.0)

x = st.number_input("Length (x)", min_value=0.0, max_value=10.0, value=5.0)

y = st.number_input("Width (y)", min_value=0.0, max_value=10.0, value=5.0)

z = st.number_input("Height (z)", min_value=0.0, max_value=10.0, value=3.0)

# Categorical Inputs
cut = st.selectbox("Cut", ['Ideal','Premium','Good','Very Good','Fair'])

color = st.selectbox("Color", ['D','E','F','G','H','I','J'])

clarity = st.selectbox("Clarity", ['SI2','SI1','VS2','VS1','VVS2','VVS1','IF'])

# Predict Button
if st.button("Predict Price"):

    input_data = pd.DataFrame({
        "carat":[carat],
        "cut":[cut],
        "color":[color],
        "clarity":[clarity],
        "depth":[depth],
        "table":[table],
        "x":[x],
        "y":[y],
        "z":[z]
    })

    prediction = model.predict(input_data)

    st.success(f"💰 Predicted Diamond Price: ${prediction[0]:,.2f}")