import streamlit as st 
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pacote.sub_pacote.funcoes import listar_produtos
from App import excluir_produto




def ListarProdutosPage():
    st.subheader("Lista de Produtos")
    produtos = listar_produtos()

    df_produtos = pd.DataFrame(produtos, columns=["ID", "Nome", "Marca","quantidade", "Categoria", "Lote", "Validade"])
    st.table(df_produtos)

    for i, row in df_produtos.iterrows():
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.text(f"{row['Nome']} / Marca: {row['Marca']} / Lote: ({row['Lote']})")
        col2.button("Excluir", key=f"excluir_{row['ID']}")
        col3.button("Editar", key=f"editar_{row['ID']}")   
   