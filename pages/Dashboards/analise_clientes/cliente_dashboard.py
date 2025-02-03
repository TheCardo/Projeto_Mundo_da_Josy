import streamlit as st
import pandas as pd
import plotly.express as px
from pacote.sub_pacote.funcoes import clientes_mais_compraram, ticket_medio


def AnaliseClientesPage():
    st.title("📊 Análise de Clientes")

    df_clientes = clientes_mais_compraram()
    if not df_clientes.empty:
        fig_clientes = px.bar(df_clientes, x="Cliente", y="Total Gasto", title="Clientes que mais compraram", text_auto=True)
        st.plotly_chart(fig_clientes)
    else:
        st.warning("Nenhum dado de compras encontrado.")
    

    media_ticket = ticket_medio()
    st.metric("💳 Ticket Médio", f"R$ {media_ticket:,.2f}")
