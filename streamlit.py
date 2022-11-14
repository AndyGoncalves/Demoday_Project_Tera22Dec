import streamlit as st
import pandas as pd

st.header("Predição salário TERA")

profissoes = pd.read_csv("profissoesti.csv")

name = st.text_input("Qual é o seu nome?")

if(len(name)>0):
    st.write(f'Seu nome é {name}')
else:
    st.write('Favor inserir seu nome!')

st.header("Arquivo usado")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
