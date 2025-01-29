import streamlit as st 
import pandas as pd
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from App import adicionar_produtos, listar_clientes, listar_produtos
from pacote.sub_pacote import funcoes
from App import validar_telefone, validar_cpf



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
            resultado = funcoes.adicionar_clientes(nome, telefone, data_nascimento, cpf)
            if resultado == "Cliente adicionado com sucesso!":
                st.success(resultado)
            else:
                st.error(resultado)
        else:
            st.error("Por favor, preencha todos os campos corretamente!")