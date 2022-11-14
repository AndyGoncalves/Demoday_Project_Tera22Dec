import streamlit as st
import pandas as pd

#nomear
st.header("Perfil do usuário - inputs")

#dados que serão usados 
df = pd.read_csv("1_filter.csv")
profissoes = df['nome_ocu'].unique().sort_values().tolist() 

ticker = st.sidebar.selectbox(
    'Escolha uma profissão',
     profissoes)

name = st.text_input("Qual é o seu nome?")

if(len(name)>0):
    st.write(f'Seu nome é {name}')
else:
    st.write('Favor inserir seu nome!')
