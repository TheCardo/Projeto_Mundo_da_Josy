import streamlit as st 
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pacote.sub_pacote.funcoes import adicionar_produtos, listar_produtos

def atualizar_produtos():
    st.session_state.produtos = listar_produtos()

if "produtos" not in st.session_state:
    atualizar_produtos()

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
            if resultado == "Produto adicionado com sucesso!":
                st.success(resultado)
                atualizar_produtos()
            else:
                st.error(resultado)
        else:
            st.error("Por favor, preencha todos os campos corretamente!")