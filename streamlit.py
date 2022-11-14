import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

#lista de melhorias a fazer
# .sort_values()
# dicionario raça, sexo para aparecer na seleção


#nomear página
st.set_page_config(
    page_title="Demoday TERA 122022 Calculadora de salario TI")

#nomear
st.header("DEMODAY TITULO")

txt = st.text_area('Text to analyze', '''
    Este é um trabalho de conclusão no curso "Data Science and Machine Learning"
    turma 042022 - TERA. 
    Autores: 
    Andréia Gonçalves (@Andy)
    Ezequiel
    Marcos (@onemarcos)
    Tamara
    ''')

st.write('Informacões:', run_sentiment_analysis(txt))

st.subheader('Perfil d@ usuári@:')
# importar os dados que serão usados no modelo
df = pd.read_csv("1_filter.csv")

# definir as seleções - obs.: aperfeiçoar: .sort_values()
profissoes = df['nome_ocu'].unique().tolist()
sexo = df['sexo'].unique().tolist()
raca = df['racacor'].unique().tolist()

ticker = st.sidebar.selectbox(
    'Qual a sua profissão em carteira?',
     profissoes)

ticker2 = st.sidebar.selectbox(
    'Qual o seu gênero?',
     sexo)

ticker3 = st.sidebar.selectbox(
    'Qual a sua raça?',
     raca)

name = st.text_input("Olá. Qual é o seu nome?")

if(len(name)>0):
    st.write(f'{name}, conforme seu perfil, seu salário seria:')
else:
    st.write('Favor inserir seu nome!')
    
 
    
    
