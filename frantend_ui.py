import streamlit as st
import pandas as pd 
import joblib

# run like this   :  streamlit run file name
#-------------------------------------------------------------------------------------------------------

model = joblib.load('Housing_model.pkl')

st.title(""" 
# House Price Prediction App 
This app predicts the **House price**!""")

st.write("--")

area = st.number_input('area')
bedrooms = st.number_input('bedrooms')
bathroms = st.number_input('bathroms')
stories = st.number_input('stories')
frunishing_statues_0_1 = st.number_input('frunishing_staues_0_1')
mainroad = st.number_input('mainroad')
parking = st.number_input('parking')
airconditioning = st.number_input('airconditioning_0/1')

if st.button('predict_result'):
  result =  model.predict([[area,bedrooms, bathroms, stories, frunishing_statues_0_1, parking,airconditioning, mainroad]])
  st.success('House price: {}'.format(result))