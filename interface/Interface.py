import streamlit as st
import pandas as pd
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from App import adicionar_produtos, listar_clientes, listar_produtos
from pacote.sub_pacote import funcoes

st.title("Gerencie o seu Estoque com o estoX!")

menu = st.sidebar.radio("Selecione uma funcionalidade:", [
    "Ínicio",
    "Cadastrar Cliente",
    "Adicionar Produto",
    "Listar Produtos",
    "Listar Clientes",
    "Editar Produto",
    "Excluir Produto",
    "Realizar Venda"
])


def connect_db():
    return sqlite3.connect("estoX.db")

if menu == "Cadastrar Cliente":
    st.subheader("Cadastro o seu cliente")

    with st.form(key="form_cliente"):
        nome = st.text_input("Nome do Cliente:")
        telefone = st.text_input("Telefone:")
        data_nascimento = st.date_input("Data de Nascimento:")
        cpf = st.text_input("CPF (Somente Números):")

        botao_submit = st.form_submit_button("Cadastrar Cliente")

    if botao_submit:
        if nome and telefone and data_nascimento and cpf:
            try:
                funcoes.adicionar_clientes(nome, telefone, data_nascimento, cpf)
                st.success("Cliente cadastrado com sucesso!")
            except sqlite3.Error as erro:
                st.error(f"Erro ao salvar no banco de dados: {erro}")
        else:
            st.error("Por favor, preencha todos os campos corretamente!")

elif menu == "Adicionar Produto":
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

elif menu == "Listar Produtos":
    st.subheader("Lista de Produtos")
    produtos = listar_produtos()
    if produtos:
        df_produtos = pd.DataFrame(produtos, columns=["ID", "Nome", "Marca", "Categoria", "Quantidade", "Lote", "Validade"])
        st.table(df_produtos)
    else:
        st.error("Nenhum produto encontrado!")


elif menu == "Listar Clientes":
    st.subheader("Lista de Clientes")
    clientes = listar_clientes()
    if clientes:
        df_clientes = pd.DataFrame(clientes, columns=["ID", "Nome", "Telefone", "Data de Nascimento", "CPF"])
        st.table(df_clientes)
    else:
        st.error("Nenhum cliente encontrado!")