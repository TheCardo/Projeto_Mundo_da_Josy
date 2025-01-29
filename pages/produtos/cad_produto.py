import streamlit as st 
import pandas as pd
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from App import adicionar_produtos, listar_clientes, listar_produtos
from pacote.sub_pacote import funcoes
from datetime import datetime


def CadatrarProdutosPage():
    st.subheader("Cadastre o seu produto")
    with st.form(key="form_produto"):
        nome = st.text_input("Nome do Produto:")
        marca = st.text_input("Marca:")
        categoria = st.text_input("Categoria:")
        lote = st.text_input("Lote:")
        validade = st.date_input("Data de Validade:")
        quantidade = st.number_input("Quantidade:", min_value=0)
        
        botao_submit = st.form_submit_button("Cadastrar Produto")

    if botao_submit:
        if nome and marca and categoria and lote and validade and quantidade:
            resultado = adicionar_produtos(nome, marca, categoria, lote, validade, quantidade)
            if resultado == "produto adicionado com sucesso!":
                st.success(resultado)
            else:
                st.error(resultado)
        else:
            st.error("Por favor, preencha todos os campos corretamente!")