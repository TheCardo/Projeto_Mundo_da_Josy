import streamlit as st
import pandas as pd
import plotly.express as px
from pacote.sub_pacote.funcoes import produtos_mais_vendidos, produtos_menos_vendidos

def AnaliseProdutosPage():
    st.title("📦 Análise de Produtos")
    df_mais_vendidos = produtos_mais_vendidos()
    if not df_mais_vendidos.empty:
        st.subheader("🔥 Produtos Mais Vendidos")
        fig_mais_vendidos = px.bar(df_mais_vendidos, x="Produto", y="Quantidade Vendida", title="Top Produtos Mais Vendidos", text_auto=True)
        st.plotly_chart(fig_mais_vendidos)
    else:
        st.warning("Nenhum dado de produtos vendidos encontrado.")

    df_menos_vendidos = produtos_menos_vendidos()
    if not df_menos_vendidos.empty:
        st.subheader("📉 Produtos Menos Vendidos")
        fig_menos_vendidos = px.bar(df_menos_vendidos, x="Produto", y="Quantidade Vendida", title="Top Produtos Menos Vendidos", text_auto=True)
        st.plotly_chart(fig_menos_vendidos)
    else:
        st.warning("Nenhum dado de produtos menos vendidos encontrado.")