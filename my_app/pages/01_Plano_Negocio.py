# Contents of ~/my_app/pages/page_2.py
import streamlit as st

st.markdown("# Problema de Negócio")
st.sidebar.markdown("# Problema de Negócio")

body = '''Através da metodologia dos 5 por quês - definimos que o problema de negócio é
 '''

st.markdown(body, unsafe_allow_html=False)

left_column, right_column = st.columns(2)
with left_column:
   st.metric(label="PÚBLICO ALVO:", value="Profissionais TI")
          
with right_column:
    st.metric(label="CONTEXTO:", value="Pretensão salarial")


left_column, right_column = st.columns(2)
with left_column:
   st.metric(label="DECISÕES TOMADAS:", value="15")
          
with right_column:
    st.metric(label="CONSEQUÊNCIAS:", value="4")

left_column, right_column = st.columns(2)
with left_column:
   st.metric(label="IMPACTO:", value="15")
          
with right_column:
    st.metric(label="VALOR:", value="4")


from PIL import Image
image = Image.open('porques.PNG')

st.image(image, caption='Sunrise by the mountains')


body = '''RASCUNHO PDF

Devemos entender:
● Quem é o seu público?
● Qual é o contexto em que o seu público está
inserido?
● Quais são as decisões tomadas atualmente?
● Quais decisões serão afetadas ou tomadas pela sua
solução?
● Onde está o diferencial do uso de técnicas de
machine learning?
● Como a sua solução afetará o contexto e as pessoas
envolvidas?
● Como você espera que a sua solução irá afetar a vida
das pessoas e gerar valor?
● Quem consumirá diretamente o resultado da sua
solução, uma pessoa ou um sistema?
● Qual via será utilizada por essa pessoa ou sistema
para o consumo da informação?
● Quais camadas a sua solução possui? Como é o
fluxo de dados em uma visão macro?
● Onde estão os dados que vocês irão utilizar?

 '''

st.markdown(body, unsafe_allow_html=False)