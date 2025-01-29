import streamlit as st 
import pandas as pd
import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pacote.sub_pacote.funcoes import listar_produtos
from App import excluir_produto

def ListarProdutosPage():
    st.subheader("Lista de Produtos")

    if "mensagem" in st.session_state:
        if st.session_state.tipo_mensagem == "success":
            st.success(st.session_state.mensagem)
        elif st.session_state.tipo_mensagem == "error":
            st.error(st.session_state.mensagem)
        del st.session_state.mensagem
        del st.session_state.tipo_mensagem



    produtos = listar_produtos()

    if produtos:
        df_produtos = pd.DataFrame(produtos, columns=["ID", "Nome", "Marca", "Categoria", "Quantidade", "Lote", "Validade"])
        st.table(df_produtos)

    for i, row in df_produtos.iterrows():
        col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
        col1.text(f"{row['Nome']} - {row['Marca']} ({row['Categoria']})")
        col2.text(f"Estoque: {row['Quantidade']}")
        excluir = col3.button("Excluir", key=f"excluir_{row['ID']}")
        editar = col4.button("Editar", key=f"Editar_{row['ID']}")
        if excluir:
                confirmar = st.radio(
                f"Tem certeza que deseja excluir o produto '{row['Nome']}'?",
                options=["Não", "Sim"],
                key=f"confirmar_{row['ID']}",
                )

                if confirmar == "Sim":
                    sucesso = excluir_produto(row["ID"], row["Nome"])
                    if sucesso:
                        st.session_state.mensagem = f"Produto '{row['Nome']}' excluído com sucesso!"
                        st.session_state.tipo_mensagem = "success"
                    else:
                        st.session_state.mensagem = "Erro ao excluir o produto. Tente novamente."
                        st.session_state.tipo_mensagem = "error"       
                    st.rerun()