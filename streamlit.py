import streamlit as st
import pandas as pd

st.header("Perfil do usuário")

profissoes = pd.read_csv("profissoesti.csv")

st.write(profissoes)

nome_profissao = st.selectbox(st.write(profissoes))

name = st.text_input("Qual é o seu nome?")

if(len(name)>0):
    st.write(f'Seu nome é {name}')
else:
    st.write('Favor inserir seu nome!')


data = pd.DataFrame({Prof:profissoes},index=[0])

st.header("Suba um arquivo")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

