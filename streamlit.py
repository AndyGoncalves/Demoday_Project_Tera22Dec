import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(
    page_title="Salários TI CAGED")

st.title("Salários TI CAGED")

df = pd.DataFrame(
   np.random.randn(50, 20),
   columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)