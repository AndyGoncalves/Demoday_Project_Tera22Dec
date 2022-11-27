#----- IMPORTAR BIBLIOTECAS ------
import pandas as pd # pip install pandas openpyxl
import streamlit as st #pip install streamlit
import plotly.express as px #pip install plotly-express
import statistics
import numpy
from collections import defaultdict
#----- ETICA ------
st.subheader('ATENÇÃO ÀS PREMISSAS:')
body = '''
1) Informações referentes à cidade de São Paulo, no ano 2022;
2) Informações considerando que o empregador declarado é um 'CNPJ RAIZ', 'CPF' ou 'Não Identificado';
3) A calculadora informa considerando apenas as informações declaradas via 'eSocial', 'CAGED' e 'EmpregadoWEB'.
4) Salário mínimo 2022 a R$ 1.212,00. A métrica se basea na mediana do valor do salário.  
'''
st.markdown(body, unsafe_allow_html=False)
st.markdown("---")

# ----- CARREGAR BASE DE DADOS -----
df = pd.read_csv("caged.csv") 
# ----- VISUALIZAR BASE --------
#st.dataframe(df)
#st.write(df.columns)
# ----- SIDEBAR -----
st.sidebar.header("Defina seu perfil aqui: ")
#profissao, sexo, idade, raca, deficiencia, grau

# ----- PROFISSAO -----
descricao = st.sidebar.selectbox(
    "Selecione o cargo:",
    options=df["Descrição"].unique()
)
# ----- SEXO -----

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
1:'Branca',
2:'Preta',
3:'Parda',
4:'Amarela',
5:'Indígena',
6:'Não informada',
7:'Não Identificado'
}

racacor = st.sidebar.selectbox(
    "Selecione sua cor:",
    options=list(dic_racacor.values())
)


# ----- DEFICIENCIA -----
dic_deficiencia = {
0:'Não Deficiente',
1:'Física',
2:'Auditiva',
3:'visual',
4:'AIntelectual (Mental)',
5:'Múltipla',
6:'Reabilitado',
9:'Não Identificado'
}

deficiencia = st.sidebar.selectbox(
    "Tipo de deficiência:",
    options=list(dic_deficiencia.values())
)

# ----- ESCOLARIDADE -----
dic_grau = {
1:'Analfabeto',
2:'Até 5ª Incompleto',
3:'5ª Completo Fundamental',
4:'6ª a 9ª Fundamental',
5:'Fundamental Completo',
6:'Médio Incompleto',
7:'Médio Completo',
8:'Superior Incompleto',
9:'Superior Completo',
10:'Mestrado',
11:'Doutorado',
80:'Pós-Graduação completa',
99:'Não Identificado'
}

graudeinstrucao = st.sidebar.selectbox(
    "Selecione o grau de instrução:",
    options=list(dic_grau.values())
)

# ----- QUERY COM FILTROS -----
#preciso incluir um if se caso não tiver a busca com o perfil selecionado
df_selection = df.query(
"Descrição == @descricao & sexo==@sexo & idade == @idade & raçacor==@racacor & tipodedeficiência==@deficiencia & graudeinstrução==@graudeinstrucao"
)


#df_selection = df.query(
#"Descrição == @descricao & sexo==@sexo & idade == @idade & raçacor==@racacor & tipodedeficiência==@deficiencia & graudeinstrução==@graudeinstrucao"
#)   #AttributeError: 'float' object has no attribute 'round'




#df_selection = df.query(
#"Descrição == @descricao & sexo.isin(@sexo) & idade == @idade & raçacor.isin(@racacor) & tipodedeficiência.isin(@deficiencia) & graudeinstrução.isin(@graudeinstrucao)"
#)
      

#df_selection = df.query(
#"Descrição == @descricao & sexo.isin(@dic_sexo) & idade == @idade & raçacor.isin(@dic_racacor) & tipodedeficiência.isin(@dic_deficiencia) & graudeinstrução.isin(@dic_grau)"
#)


# ----- MAINPAGE -----
st.title("SAIBA SEU SALÁRIO DE MERCADO:")
st.subheader(f"{descricao}")

#st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
# ----- TOP KPI'S -----
salario_max = df_selection["salário"].max()
salario_min = df_selection["salário"].min()
salario_mediano = df_selection["salário"].median()
#salario_moda = df_selection["salário"].mode()
salario_minimo = 1212.00
percentual_minimo=(((salario_min - salario_mediano)*100/salario_min).round(2))
percentual_maximo=(((salario_max - salario_mediano)*100/salario_max).round(2))
#percentual_moda= (((salario_moda - salario_minimo)*100/salario_moda).round(2))
#st.metric(label="Gas price", value=percentual_minimo, delta=percentual_minimo)

col1, col2, col3 = st.columns(3)
col1.metric("Salário máximo:", f"R${salario_max:,.2f}", percentual_maximo)
col2.metric("Salário mínimo:", f"R${salario_min:,.2f}",percentual_minimo)
col3.metric("Salário mediano:", f"R${salario_mediano:,.2f}")
#col3.metric("Salário frequente:", salario_moda, percentual_moda)
#colocar indicador percentual acima do salário mínimo

st.markdown("---")