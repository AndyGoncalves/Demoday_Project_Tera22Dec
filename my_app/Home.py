# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("# DEMODAY TERA ")
#st.sidebar.markdown("#")

body = '''Trabalho de conclusão de curso - Dez/2022.

 Turma DCS042022 -  "Data Science and Machine Learning" 
 '''

st.markdown(body, unsafe_allow_html=False)

image1 = Image.open('my_app\\andreia.jpg') 
image2 = Image.open('my_app\ezequiel.jpg')
image3 = Image.open('my_app\marcos.jpg')
image4 = Image.open('my_app\\tamara.jpg')

left_column, middle1_column, middle2_column, right_column = st.columns(4)
with left_column:
    st.subheader("Andréia Gonçalves") 
    st.image(image1, caption='https://www.linkedin.com/in/andreiagoncalvesbh/') 
    
with middle1_column:
    st.subheader("Ezequiel Martins") 
    st.image(image2, caption='https://www.linkedin.com/in/fontesmartins23/')

with middle2_column:
    st.subheader("Marcos Oliveira") 
    st.image(image3, caption='https://www.linkedin.com/in/one-marcos/')

with right_column:
    st.subheader("Tamara Cunha") 
    st.image(image4, caption='https://www.linkedin.com/in/tamara-cunha/')







