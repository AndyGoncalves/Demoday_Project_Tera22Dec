#----- IMPORTAR BIBLIOTECAS ------
import pandas as pd # pip install pandas openpyxl
import streamlit as st #pip install streamlit
import plotly.express as px #pip install plotly-express
import statistics
import numpy

#----- ETICA ------
st.subheader('ATENÇÃO ÀS PREMISSAS:')
body = '''
1) Informações referentes à cidade de São Paulo, no ano 2022;
2) Informações considerando que o empregador declarado é um 'CNPJ RAIZ', 'CPF' ou 'Não Identificado';
3) A calculadora informa considerando apenas as informações declaradas via 'eSocial', 'CAGED' e 'EmpregadoWEB'.
 '''
st.markdown(body, unsafe_allow_html=False)
st.markdown("---")

# ----- CARREGAR BASE DE DADOS -----
df = pd.read_csv("caged.csv") 
# ----- VISUALIZAR BASE --------
st.dataframe(df)

# ----- SIDEBAR -----
st.sidebar.header("Defina seu perfil aqui: ")
#profissao, sexo, idade, raca, deficiencia, grau

# ----- PROFISSAO -----
descricao = st.sidebar.selectbox(
    "Selecione o cargo:",
    options=df["Descrição"].unique()
)
# ----- SEXO -----
#dic_sexo = {
#"homem": 1,
#"mulher": 3
#}

dic_sexo = {
1:"homem",
3:"mulher"
}

#values()
sexo = st.sidebar.selectbox(
    "Selecione o gênero:",
    options=list(dic_sexo.values())
    )
# ----- IDADE -----
idade = st.sidebar.slider('Qual a sua idade?', 17, 72, 25)
#no banco de dados vai até a idade 72 anos.

# ----- RACA -----
dic_racacor = {
'Branca':1,
'Preta':2,
'Parda':3,
'Amarela':4,
'Indígena':5,
'Não informada':6,
'Não Identificado':9
}

racacor = st.sidebar.selectbox(
    "Selecione sua cor:",
    options=list(dic_racacor.keys())
)
# ----- DEFICIENCIA -----
dic_deficiencia = {
'Não Deficiente':0.0,
'Física':1.0,
'Auditiva':2.0,
'AIntelectual (Mental)':4.0,
'Múltipla':5.0,
'Reabilitado':6.0,
'Não Identificado':9.0
}
#0.0	Não Deficiente
#1.0	Física
#2.0	Auditiva
#3.0	Visual
#4.0	Intelectual (Mental)
#5.0	Múltipla
#6.0	Reabilitado
#9.0	Não Identificado

deficiencia = st.sidebar.selectbox(
    "Selecione sua cor:",
    options=list(dic_deficiencia.keys())
)

# ----- ESCOLARIDADE -----
dic_grau = {
'Analfabeto':1.0,
'Até 5ª Incompleto':2.0,
'6ª a 9ª Fundamental':4.0,
'Fundamental Completo':5.0,
'Médio Incompleto':6.0,
'Médio Completo':7.0,
'Superior Incompleto':8.0,
'Superior Completo':9.0,
'Mestrado':10.0,
'Doutorado':11.0,
'Pós-Graduação completa':80.0,
'Não Identificado':99.0
}

#1.0	Analfabeto
#2.0	Até 5ª Incompleto
#3.0	5ª Completo Fundamental
#4.0	6ª a 9ª Fundamental
#5.0	Fundamental Completo
#6.0	Médio Incompleto
#7.0	Médio Completo
#8.0	Superior Incompleto
#9.0	Superior Completo
#10.0	Mestrado
#11.0	Doutorado
#80.0	Pós-Graduação completa
#99.0	Não Identificado

graudeinstrucao = st.sidebar.selectbox(
    "Selecione o grau de instrução:",
    options=list(dic_grau.keys())
)

# ----- QUERY COM FILTROS -----
df_selection = df.query(
"Descrição == @descricao & sexo == @sexo.str.contains(dic_sexo.keys())"
)
    #"Descrição == @descricao & sexo == @dic_sexo & idade == @idade & raçacor == @dic_racacor.keys() & graudeinstrução == @dic_grau.keys()"
#df.loc[(df['make']=make_choice) & (df['year']=year_choice) & (df['model']= model_choice) & (df[engine]=engine_choice)]


# ----- MAINPAGE -----
st.title("SAIBA SEU SALÁRIO DE MERCADO:")
st.subheader(f"{descricao}")

#st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
# ----- TOP KPI'S -----
salario_max = df_selection["salário"].max()
salario_min = df_selection["salário"].min()
#salario_moda = df_selection["salário"].mode()
#salario mínimo = 1212.00
#percentual_minimo=
#percentual_maximo=
#percentual_moda= 
#st.metric(label="Gas price", value=4, delta=-0.5)

col1, col2 = st.columns(2)
col1.metric("Salário máximo:", salario_max)
col2.metric("Salário mínimo:", salario_min)
#col3.metric("Salário frequente:", salario_moda)
#colocar indicador percentual acima do salário mínimo

st.markdown("---")

# ----- MAINPAGE -----
#st.title("SELECIONA A FAIXA SALARIAL QUE GOSTARIA DE TER:")
#st.subheader(f"Vou te mostrar o perfil dessas pessoas. ")
#vincular com a página do modelo (não sei como fazer)
#st.write()


# ----- VISUALIZAR BASE COM FILTROS --------
#st.dataframe(df_selection)

#----- CONFIGURAR PÁGINA STREAMLIT ------
#emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

#st.set_page_config(page_title="NOME DASHBOARD",
 #                  page_icon=":bar_chart:",
  #                 layout="wide"
#)

# ----- CARREGAR BASE DE DADOS -----
#CSV
#df = pd.read_csv("caged.csv") 

# ----- VISUALIZAR BASE --------
#st.dataframe(df)

#left_column, middle_column, right_column = st.columns(3)
#with left_column:
   # st.metric("Salário máximo: ", salario_max)
#with middle_column:
    #st.metric("Salário mínimo: ", salario_min)
#with right_column:
    #st.metric("Salário frequente: ", salario_moda, delta=float)





trace0 = go.Box(y=df["sexo"],name="sexo")
trace1 = go.Box(y=df["idade"],name="idade")
trace2 = go.Box(y=df["racacor"],name="racacor")
trace3 = go.Box(y=df["grau"],name="grau")
trace4 = go.Box(y=df["tipodeficiencia"],name="deficiencia")
trace5 = go.Box(y=df["nome_ocu"],name="ocupacao")
data = [trace0, trace1, trace2,trace3, trace4, trace5]
iplot(data)

import pandas as pd
import numpy as np
import altair as alt
import numpy as np
import plotly.figure_factory as ff
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly import tools
import plotly.plotly as py
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)
import plotly.graph_objs as go
import plotly.figure_factory as ff
from IPython.display import HTML, Image

#fig = ff.create_distplot([df],['sexo'],bin_size=5)
#iplot(fig, filename='Basic Distplot')
