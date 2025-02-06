import streamlit as st
from pacote.sub_pacote.funcoes import vendas_totais_mes
import plotly.express as px

def VisaoGeralPage():
    st.title("📊 Visão Geral")
    
    df_vendas = vendas_totais_mes()
    if not df_vendas.empty:
        fig_vendas = px.bar(df_vendas, x="Mês/Ano", y="Total Vendas", title="Total de Vendas por Mês", text_auto=True)
        st.plotly_chart(fig_vendas)
    else:
        st.warning("Nenhum dado de vendas encontrado.")
    
