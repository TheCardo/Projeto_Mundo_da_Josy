import streamlit as st 
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pacote.sub_pacote.funcoes import listar_produtos, excluir_produto

def atualizar_produto():
         st.session_state.produtos = listar_produtos()

def ListarProdutosPage():
    st.subheader("Lista de Produtos")
    if "produtos" not in st.session_state:
          atualizar_produto()

    df_produtos = pd.DataFrame(st.session_state.produtos, columns=["ID", "Nome", "Marca","quantidade", "Categoria", "Lote", "Validade"])
    st.table(df_produtos)

    for i, row in df_produtos.iterrows():
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.text(f"{row['Nome']} / Marca: {row['Marca']} / Lote: ({row['Lote']})")
        col2.button("Excluir", key=f"excluir_{row['ID']}", on_click=excluir_produto, args=(row["ID"],), kwargs={}, help="Remove o produto da sua tabela e atualiza a lista automaticamente" )
        col3.button("Editar", key=f"editar_{row['ID']}")   
    if "produtos" in st.session_state:
          atualizar_produto()

