import streamlit as st
import pandas as pd
from pacote.sub_pacote.funcoes import vendas_totais_mes, produtos_mais_vendidos
import plotly.express as px

def VisaoGeralPage():
    st.title("📊 Visão Geral")
    
    df_vendas = vendas_totais_mes()
    if not df_vendas.empty:
        fig_vendas = px.bar(df_vendas, x="Mês/Ano", y="Total Vendas", title="Total de Vendas por Mês", text_auto=True)
        st.plotly_chart(fig_vendas)
    else:
        st.warning("Nenhum dado de vendas encontrado.")
    

    df_produtos = produtos_mais_vendidos()
    if not df_produtos.empty:
        fig_produtos = px.pie(df_produtos, names="Produto", values="Quantidade Vendida", title="Produtos Mais Vendidos", hole=0.3)
        st.plotly_chart(fig_produtos)
    else:
        st.warning("Nenhum dado de produtos vendidos encontrado.")
    

    total_receita = df_vendas["Total Vendas"].sum() if not df_vendas.empty else 0
    st.metric("💰 Receita Total", f"R$ {total_receita:,.2f}")