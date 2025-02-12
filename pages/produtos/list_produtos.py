import streamlit as st
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from pacote.sub_pacote.funcoes import listar_produtos, editar_nome_produto, editar_marca_produto, editar_categoria_produto, editar_lote_produto, editar_validade_produto, editar_quantidade_produto
from App import excluir_produto


def atualizar_produtos():
    st.session_state.produtos = listar_produtos()

if "produtos" not in st.session_state:
    atualizar_produtos()

if "editando_produto" not in st.session_state:
    st.session_state.editando_produto = None

def ListarProdutosPage():
    st.subheader("Lista de Produtos")

    if "produtos" not in st.session_state:
        atualizar_produtos()
    if st.session_state.editando_produto is None:
        df_produtos = pd.DataFrame(st.session_state.produtos, columns=["ID", "Nome", "Marca", "Categoria", "Quantidade", "Lote", "Validade"])
        st.table(df_produtos)

        for i, row in df_produtos.iterrows():
            col1, col2, col3 = st.columns([2, 1, 1])
            col1.text(f"{row['Nome']} / Marca: {row['Marca']} / Categoria: {row['Categoria']} / Lote: {row['Lote']} / Validade: {row['Validade']} / Quantidade: {row['Quantidade']}")
            if col2.button("Excluir", key=f"excluir_{row['ID']}"):
                excluir_produto(row["ID"])
                atualizar_produtos()
                st.success(f"Produto '{row['Nome']}' excluído com sucesso!")
                st.rerun()
            if col3.button("Editar", key=f"editar_{row['ID']}"):
                st.session_state.editando_produto = row["ID"]
                st.rerun()

    else:
        produto = next((p for p in st.session_state.produtos if p[0] == st.session_state.editando_produto), None)
        if produto:
            st.subheader(f"Editando {produto[1]}")

            
            campo = st.selectbox("Escolha o campo para editar:", ["Nome", "Marca", "Categoria", "Lote", "Validade", "Quantidade"])
            
            indice_campo = {
                "Nome": 1,
                "Marca": 2,
                "Categoria": 3,
                "Quantidade": 4,
                "Lote": 5,
                "Validade": 6
    }
            if campo == "Validade":
                novo_valor = st.date_input(f"Nova {campo}", value=pd.to_datetime(produto[6]))
            elif campo == "Quantidade":
                novo_valor = st.number_input(f"Nova {campo}", value=int(produto[4]), min_value=0)
            else:
                indice = indice_campo.get(campo)
                novo_valor = st.text_input(f"Novo {campo}", value=produto[indice] if indice is not None else "")


            

            if st.button("Salvar"):
                if novo_valor:
                    if campo == "Nome":
                        resultado = editar_nome_produto(produto[0], novo_valor)
                    elif campo == "Marca":
                        resultado = editar_marca_produto(produto[0], novo_valor)
                    elif campo == "Categoria":
                        resultado = editar_categoria_produto(produto[0], novo_valor)
                    elif campo == "Lote":
                        resultado = editar_lote_produto(produto[0], novo_valor)
                    elif campo == "Validade":
                        resultado = editar_validade_produto(produto[0], novo_valor.strftime("%Y-%m-%d"))
                    elif campo == "Quantidade":
                        resultado = editar_quantidade_produto(produto[0], novo_valor)

                    if "sucesso" in resultado.lower():
                        st.success(resultado)
                        atualizar_produtos()
                        st.session_state.editando_produto = None
                        st.rerun()
                    else:
                        st.error(resultado)
                else:
                    st.error("Por favor, insira um valor válido.")
            if st.button("Cancelar"):
                st.session_state.editando_produto = None
                st.rerun()
        else:
            st.error("Produto não encontrado.")
            st.session_state.editando_produto = None 
            st.rerun()
