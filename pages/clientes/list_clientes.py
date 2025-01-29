import streamlit as st 
import pandas as pd
import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pacote.sub_pacote.funcoes import listar_clientes
from App import excluir_cliente

def ListarClientesPage():
    st.subheader("Lista de Clientes")
    clientes = listar_clientes()

    if clientes:
        df_clientes = pd.DataFrame(clientes, columns=["ID", "Nome", "Telefone", "Data de Nascimento", "CPF"])
        st.table(df_clientes)

    for i, row in df_clientes.iterrows():
        col1, col2, col3= st.columns([2, 1, 1])
        col1.text(f"{row['Nome']}/Telefone: {row['Telefone']}  /  CPF: ({row['CPF']})")
        excluir = col2.button("Excluir", key=f"excluir_{row['ID']}")
        editar = col3.button("Editar", key=f"Editar_{row['ID']}")
        if excluir:
                with st.expander(f"Confirmar Exclusão de {row['Nome']}"):
                    confirmar = st.radio(
                    f"Tem certeza que deseja excluir esse Cliente '{row['Nome']}'?",
                    options=["Não", "Sim"],
                    key=f"confirmar_{row['ID']}",
                )
                    if confirmar == "Sim":
                        excluir_cliente(row["ID"], row["Nome"])
                        st.success(f"Produto excluído com sucesso!")
