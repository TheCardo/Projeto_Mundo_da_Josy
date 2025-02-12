import streamlit as st 
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pacote.sub_pacote.funcoes import adicionar_clientes, listar_clientes

def atualizar_clientes():
    st.session_state.clientes = listar_clientes()


if "clientes" not in st.session_state:
    atualizar_clientes()

def IncluirClientePage():
    st.title("Cadastre o seu cliente")

    with st.form(key="form_cliente"):
        nome = st.text_input("Nome do Cliente:")
        telefone = st.text_input("Telefone:")
        data_nascimento = st.date_input("Data de Nascimento:")
        
        cpf = st.text_input("CPF (Somente Números):")

        botao_submit = st.form_submit_button("Cadastrar Cliente")

    if botao_submit:
        if nome and telefone and data_nascimento and cpf:
            resultado = adicionar_clientes(nome, telefone, data_nascimento, cpf)
            if resultado == "Cliente adicionado com sucesso!":
                st.success(resultado)
                atualizar_clientes()
            else:
                st.error(resultado)
        else:
            st.error("Por favor, preencha todos os campos corretamente!")
