import streamlit as st
import pandas as pd

#nomear
st.header("Perfil do usuário - inputs")

# importar os dados que serão usados no modelo
df = pd.read_csv("1_filter.csv")

# definir as seleções - obs.: aperfeiçoar: .sort_values()
profissoes = df['nome_ocu'].unique().tolist()
sexo = df['sexo'].unique().tolist()
raca = df['sexo'].unique().tolist()

ticker = st.sidebar.selectbox(
    'Qual a sua profissão em carteira?',
     profissoes)

ticker2 = st.sidebar.selectbox(
    'Qual o seu gênero?',
     sexo)

ticker3 = st.sidebar.selectbox(
    'Qual a sua raça?',
     raca)

name = st.text_input("Qual é o seu nome?")

if(len(name)>0):
    st.write(f'Seu nome é {name}')
else:
    st.write('Favor inserir seu nome!')
