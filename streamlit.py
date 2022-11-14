import streamlit as st
import pandas as pd
import numpy as np

#bibliotecas com erro -----------------------
#import plotly.graph_objects as go
#import plotly.express as px
#---------------------------------------------

##lista de melhorias a fazer--------------------------
# .sort_values()
# dicionario raça, sexo para aparecer na seleção
#-----------------------------------------------------

#nomear página------------------------------------------
st.set_page_config(
    page_title="Demoday TERA 122022 Calculadora de salario TI")


#nomear trabalho -------------------------------------------
st.header("DEMODAY TITULO")

#criar texto apresentacao -------------------------------------------
txt = st.text_area(''' Este é um trabalho de conclusão no curso "Data Science and Machine Learning"
    turma 042022 - TERA. Autores: Andréia Gonçalves (@Andy), Ezequiel,Marcos (@onemarcos),Tamara''')

#??? st.write('Informacões:', run_sentiment_analysis(txt))

# importar os dados que serão usados no modelo-------------------------
df = pd.read_csv("1_filter.csv")

# definir as seleções - obs.: aperfeiçoar: .sort_values() --------------
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



#criar título perfil usuário -------------------------------------------
st.subheader('Perfil d@ usuári@:')

name = st.text_input("Olá. Qual é o seu nome?")

if(len(name)>0):
    st.write(f'{name}, conforme seu perfil, seu salário seria:')
else:
    st.write('Favor inserir seu nome!')
    
#-----------------------------------------------------------------
#teste graficos

#teste = pd.DataFrame({
  #"Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
 # "Contestant": ["Alex", "Alex", "Alex", "Jordan", "Jordan", "Jordan"],
 # "Number Eaten": [2, 1, 3, 1, 3, 2],
#})


# Plotly Express import plotly.express as px
#fig = px.bar(teste, x="Fruit", y="Number Eaten", color="Contestant", barmode="group")
#fig.show()


# Graph Objects import plotly.graph_objects as go
#fig = go.Figure()
#for contestant, group in teste.groupby("Contestant"):
    #fig.add_trace(go.Bar(x=group["Fruit"], y=group["Number Eaten"], name=contestant,
      #hovertemplate="Contestant=%s<br>Fruit=%%{x}<br>Number Eaten=%%{y}<extra></extra>"% contestant))
#fig.update_layout(legend_title_text = "Contestant")
#fig.update_xaxes(title_text="Fruit")
#fig.update_yaxes(title_text="Number Eaten")
#fig.show()
    
