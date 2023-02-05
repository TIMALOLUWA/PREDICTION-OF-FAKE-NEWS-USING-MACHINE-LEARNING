import streamlit as st
import joblib

# Load the model
model = joblib.load('Real-Fake')
st.title('Prediction Of Fake News Using Machine Learning Algorithms')

# user input
ip = st.text_area("Enter the news content here :", height=200)
st.subheader('Note: ')
st.caption('The input format should be : (title of the news) - (text)')

# output = prediction if the user input is real or fake news
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
