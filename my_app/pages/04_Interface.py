#----- IMPORTAR BIBLIOTECAS ------
import pandas as pd # pip install pandas openpyxl
import streamlit as st #pip install streamlit
import plotly.express as px #pip install plotly-express
import statistics
import numpy

st.markdown("# Page 4 🎉")
st.sidebar.markdown("# Page 4 🎉")

#----- CONFIGURAR PÁGINA STREAMLIT ------
#emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

#st.set_page_config(page_title="NOME DASHBOARD",
 #                  page_icon=":bar_chart:",
  #                 layout="wide"
#)

# ----- CARREGAR BASE DE DADOS -----
#CSV
df = pd.read_csv("caged.csv") 

# ----- VISUALIZAR BASE --------
#st.dataframe(df)


# ----- SIDEBAR -----
st.sidebar.header("Defina seu perfil aqui: ")

#colocar dicionário para sexo
sexo = st.sidebar.multiselect(
    "Selecione o gênero:",
    options=df["sexo"].unique(),
    default=df["sexo"].unique()
)

descricao = st.sidebar.multiselect(
    "Selecione o cargo:",
    options=df["Descrição"].unique(),
    default=df["Descrição"].unique()
)

#cidade = st.sidebar.multiselect(
#    "Selecione a cidade:",
#    options=df["cidade"].unique(),
#   default=df["cidade"].unique()
#)


df_selection = df.query(
    "sexo == @sexo & Descrição == @descricao"
)


# ----- MAINPAGE -----
st.title(":moneybag:  :computer: Receita")
st.markdown("##")

# ----- TOP KPI'S -----
salario_max = df_selection["salário"].max()
salario_min = df_selection["salário"].min()
salario_moda = df_selection["salário"].mode()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Salário máximo: ") 
    st.subheader(f"R$ {salario_max}") 
with middle_column:
    st.subheader("Salário mínimo: ") 
    st.subheader(f"R$ {salario_min}") 
with right_column:
    st.subheader("Salário mais frequente: ") 
    st.subheader(f"R$ {salario_moda}") 

st.markdown("---")


# ----- VISUALIZAR BASE COM FILTROS --------
#st.dataframe(df_selection)


