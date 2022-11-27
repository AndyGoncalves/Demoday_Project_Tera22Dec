# Contents of ~/my_app/pages/page_2.py
import streamlit as st
from PIL import Image

st.markdown("# DEFINIÇÃO DO PROBLEMA")

st.subheader('Produto desenvolvido pelo grupo:')
body = ''' Calculadora onde o usuário (empregador ou empregado) seleciona o perfil (habilidades comportamentais e técnicas), de acordo com as variáveis da base de dados (CAGED), e recebe como resultado o salário médio de mercado para comparação e tomada de decisão.
 '''
st.markdown(body, unsafe_allow_html=False)

st.subheader('Profissões analisadadas')
image1 = Image.open('profissoes_analisadas.png')
st.image(image1)

st.subheader('Problema de negócio')
body = ''' No mercado de TI tem colaboradores com o mesmo cargo e salários muito destoantes. Como predizer o salário de um profissional de Tecnologia? 
Quais as características impactam mais na sua remuneração? '''
st.markdown(body, unsafe_allow_html=False)


st.subheader('Metodologia - 5 porquês')
image = Image.open('porques_2.PNG')
st.image(image)



