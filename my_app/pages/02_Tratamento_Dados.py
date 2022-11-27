# Contents of ~/my_app/pages/page_2.py
import streamlit as st
import pandas as pd
from PIL import Image

st.markdown("# ANÁLISE DOS DADOS")

#-----VARIÁVEIS USADAS
df = pd.read_csv("Caged_cidade_filtro.csv") 

imagex = Image.open('boxplot_interpretacao.PNG')
imagey = Image.open('faixa_salarial.PNG')
image1 = Image.open('salario_cbo.png')
image2 = Image.open('salario_deficiencia.png')
image3 = Image.open('salario_raca.png')
image4 = Image.open('salario_sexo.png')
image5 = Image.open('salario_educacao.png')
image6 = Image.open('distribuicao_graueduca.PNG')


body1 = ''' Os profissões mais frequentes são:
'''
body2 = ''' O mercado é prioritáriamente masculino, com uma presença de 70%. 
'''
body3 = ''' Cerca de 70'%' das pessoas declararam não possuir deficiência. Das que declararam, o salário permaneceu  
'''
body4 = ''' A raça predominante é branca. Os negros representam x do mercado, e possuem uma renda similar.   
'''
body5 = ''' Faixa educação mostra que a    
'''
body6 = ''' Faixa educação mostra que a    
'''

st.subheader('Premissas:')

left_column, right_column = st.columns(2)
with left_column:
    st.caption("Leitura Boxplot") 
    st.image(imagex) 
    
with right_column:
    st.caption("Faixa salarial") 
    st.image(imagey)

st.markdown("---")

left_column, right_column = st.columns(2)
with left_column:
    st.caption("Faixa salarial por profissão") 
    st.image(image1) 
    st.markdown(body1, unsafe_allow_html=False)
    
with right_column:
    st.caption("Faixa salarial por sexo") 
    st.image(image4)
    st.markdown(body2, unsafe_allow_html=False)

st.markdown("---")

left_column, right_column = st.columns(2)
with left_column:
    st.caption("Faixa salarial por deficiência") 
    st.image(image2) 
    st.markdown(body3, unsafe_allow_html=False)
    
with right_column:
    st.caption("Faixa salarial por raça") 
    st.image(image3)
    st.markdown(body4, unsafe_allow_html=False)

st.markdown("---")

left_column, right_column = st.columns(2)
with left_column:
    st.caption("Faixa grau de educação") 
    st.image(image5) 
    st.markdown(body5, unsafe_allow_html=False)
    
with right_column:
    st.caption("Faixa salarial por faixa de educação") 
    st.image(image6)
    st.markdown(body6, unsafe_allow_html=False)

st.markdown("---")

st.markdown("# TESTES DE HIPÓTESE")

left_column, right_column = st.columns(2)
with left_column:
    st.caption("HIPÓTESE 1: O salário é influenciado pelo sexo. ") 
    st.image(image5) 
    st.markdown(body5, unsafe_allow_html=False)
    
with right_column:
    st.caption("HIPÓTESE 2: O salário não é tão influenciado pelo grau de educação.") 
    st.image(image6)
    st.markdown(body6, unsafe_allow_html=False)

