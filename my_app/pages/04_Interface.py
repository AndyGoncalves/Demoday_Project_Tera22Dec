#----- IMPORTAR BIBLIOTECAS ------
import pandas as pd # pip install pandas openpyxl
import streamlit as st #pip install streamlit
import plotly.express as px #pip install plotly-express
import statistics
import numpy
from collections import defaultdict

@st.experimental_memo
def filter_selections(df, **kwargs):
    output_df = df.copy()
    for col, values in kwargs.items():
        if len(values) > 0:
            output_df = output_df[output_df[col].isin(values)]
    return output_df

st.subheader('🚨 Atenção às premissas🚨')

st.write("""
        - Informações referentes à cidade de São Paulo, no ano 2022;
        - Informações considerando que o empregador declarado é um 'CNPJ RAIZ', 'CPF' ou 'Não Identificado';
        - A calculadora informa considerando apenas as informações declaradas via 'eSocial', 'CAGED' e 'EmpregadoWEB'.
        - Salário mínimo 2022 a R$ 1.212,00. A métrica se basea na mediana do valor do salário.
        """)
st.markdown("---")

select_filter = {}

df = pd.read_csv("my_app/caged.csv")
st.header("Defina seu perfil aqui: ")

dic_racacor = {
    1:'Branca',
    2:'Preta',
    3:'Parda',
    4:'Amarela',
    5:'Indígena',
    6:'Não informada',
    7:'Não Identificado'
}

dic_sexo = {
    1:"homem",
    3:"mulher"
}

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

with st.form("my form"):

    col_1, col_2 = st.columns((5, 5))

    with col_1:
        descricao = st.multiselect(
            "Selecione o cargo:",
            options=df["Descrição"].unique()
        )

        select_filter["sexo_name"] = st.multiselect(
            "Selecione o gênero:",
            options=list(dic_sexo.values())
            )

        idade = st.slider('Qual a sua idade?', 17, 72, 25)

    with col_2:
        select_filter["raca_name"] = st.multiselect(
            "Selecione sua cor:",
            options=list(dic_racacor.values())
        )

        select_filter["defic_name"] = st.multiselect(
            "Tipo de deficiência:",
            options=list(dic_deficiencia.values())
        )

        select_filter["grau_inst"] = st.multiselect(
            "Selecione o grau de instrução:",
            options=list(dic_grau.values())
        )
    calc_button = st.form_submit_button("Calcular meu salário!")

if calc_button:
    df["raca_name"] = df["raçacor"].apply(lambda x: dic_racacor[x])
    df["grau_inst"] = df["graudeinstrução"].apply(lambda x: dic_grau[x])
    df["defic_name"] = df["tipodedeficiência"].apply(lambda x: dic_deficiencia[x])
    df["sexo_name"] = df["sexo"].apply(lambda x: dic_sexo[x])

    df.drop(["raçacor", "graudeinstrução", "tipodedeficiência", "sexo", "Unnamed: 0.1", "Unnamed: 0"], axis=1, inplace=True)
    df = df[df["idade"] == idade]
    df_selection = filter_selections(df, **select_filter)

    df_selection.reset_index(inplace=True)
    if df_selection["salário"].empty:
        st.warning("Não foi encontrado salário para o perfil selecionado! Por favor, modifique as opções selecionadas.")
    else:
        salario_max = df_selection["salário"].max()
        salario_min = df_selection["salário"].min()
        salario_mediano = df_selection["salário"].median()
        salario_moda = statistics.mode(df_selection["salário"])

        percentual_minimo = round(((salario_min - salario_mediano)*100/salario_min), 2)
        percentual_maximo = round(((salario_max - salario_mediano)*100/salario_max), 2)

        percentual_minimo = round(((salario_min - salario_mediano)*100/salario_min), 2)
        percentual_maximo = round(((salario_max - salario_mediano)*100/salario_max), 2)

        col1, col2, col3, col4 = st.columns((3,3,3,3))
        with col1:
            st.metric("Salário máximo", f"R${salario_max:,.2f}", f"{percentual_maximo}%")
        with col2:
            st.metric("Salário mínimo", f"R${salario_min:,.2f}", f"{percentual_minimo}%")
        with col3:
            st.metric("Salário mediano", f"R${salario_mediano:,.2f}")
        with col4:
            st.metric("Moda do salário", f"R${salario_moda:,.2f}")

        st.markdown("---")
