import streamlit as st
import pandas as pd

st.header("Perfil do usuário - inputs")

profissoes = pd.read_csv("profissoesti.csv")

st.write(profissoes)

name = st.text_input("Qual é o seu nome?")

if(len(name)>0):
    st.write(f'Seu nome é {name}')
else:
    st.write('Favor inserir seu nome!')
