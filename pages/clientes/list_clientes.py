
import streamlit as st 
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pacote.sub_pacote.funcoes import listar_clientes, editar_nome_cliente, editar_data_nascimento_cliente, editar_cpf_cliente, editar_telefone_cliente
from App import excluir_cliente

def atualizar_clientes():
    st.session_state.clientes = listar_clientes()
if "clientes" not in st.session_state:
    atualizar_clientes()

if "editando_cliente" not in st.session_state:
    st.session_state.editando_cliente = None

def ListarClientesPage():
    st.subheader("Lista de Clientes")
    if st.session_state.editando_cliente is None:
        df_clientes = pd.DataFrame(st.session_state.clientes, columns=["ID", "Nome", "Telefone", "Data de Nascimento", "CPF"])
        st.table(df_clientes)

        for i, row in df_clientes.iterrows():
            col1, col2, col3 = st.columns([2, 1, 1])
            col1.text(f"{row['Nome']} / Telefone: {row['Telefone']} / CPF: ({row['CPF']})")

            if col2.button("Excluir", key=f"excluir_{row['ID']}"):
                excluir_cliente(row["ID"])
                atualizar_clientes()
                st.success(f"Cliente '{row['Nome']}' excluído com sucesso!")
                st.rerun()

            if col3.button("Editar", key=f"editar_{row['ID']}"):
                st.session_state.editando_cliente = row["ID"]
                st.rerun()

    
    else:
        cliente = next((c for c in st.session_state.clientes if c[0] == st.session_state.editando_cliente), None)
        if cliente:
            st.subheader(f"Editando {cliente[1]}")
            campo = st.selectbox("Escolha o campo para editar:", ["Nome", "Telefone", "CPF", "Data de Nascimento"])
            novo_valor = st.text_input(f"Novo {campo}", value=cliente[1 if campo == "Nome" else 2 if campo == "Telefone" else 4 if campo == "CPF" else 3])
            if st.button("Salvar"):
                if novo_valor:
                    if campo == "Nome":
                        resultado = editar_nome_cliente(cliente[0], novo_valor)
                    elif campo == "Telefone":
                        resultado = editar_telefone_cliente(cliente[0], novo_valor)
                    elif campo == "CPF":
                        resultado = editar_cpf_cliente(cliente[0], novo_valor)
                    elif campo == "Data de Nascimento":
                        resultado = editar_data_nascimento_cliente(cliente[0], novo_valor)

                    if "sucesso" in resultado.lower():
                        st.success(resultado)
                        atualizar_clientes()
                        st.session_state.editando_cliente = None
                        st.rerun()
                    else:
                        st.error(resultado)
                else:
                    st.error("Por favor, insira um valor válido.")

            if st.button("Cancelar"):
                st.session_state.editando_cliente = None
                st.rerun()
        else:
            st.error("Cliente não encontrado.")
            st.session_state.editando_cliente = None
            st.rerun()