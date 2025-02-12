import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from pacote.sub_pacote.funcoes import produtos_baixo_estoque, produtos_perto_validade



def AnaliseEstoquePage():
    df_validade = produtos_perto_validade()
    if not df_validade.empty:
        st.subheader("⚠️ Produtos Perto da Validade")
        st.table(df_validade)
    else:
        st.success("Nenhum produto perto da validade.")

    df_estoque = produtos_baixo_estoque()
    if not df_estoque.empty:
        st.subheader("📉 Produtos com Baixo Estoque")
        fig_estoque = px.bar(df_estoque, x="Produto", y="Quantidade", title="Produtos com Baixo Estoque", text_auto=True)
        st.plotly_chart(fig_estoque)
    else:
        st.success("Nenhum produto com baixo estoque.")