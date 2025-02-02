import streamlit as st 
import pandas as pd
import sqlite3
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from App import adicionar_produtos, listar_clientes, listar_produtos
from pacote.sub_pacote import funcoes
from pages.produtos.cad_produto import CadatrarProdutosPage
from pages.produtos.list_produtos import ListarProdutosPage
from pages.clientes.cad_clientes import IncluirClientePage
from pages.clientes.list_clientes import ListarClientesPage
from pages.vendas.realizar_vendas import RealizarVendaPage


imagem = st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2245/2245058.png", use_container_width=False)


menu = st.sidebar.selectbox("📝 Menu de Cadastros e Vendas:", [
    "Home",
    "Cadastrar Cliente",
    "Listagem e Edição de Produtos",
    "Listagem e Edição de Clientes",
    "Adicionar Produto",
    "Realizar Venda"
])
imagem = st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2782/2782122.png", use_container_width=False)
DashBoard = st.sidebar.selectbox("📈 Visualização de Dashboards: ", [
    "Visão Geral",
    "Análise de Produtos ",
    "Análise de Clientes",
    "Análise de Estoque"

])


def connect_db():
    return sqlite3.connect("estoX.db")



if menu == "Home":
    st.title("Bem Vindo ao EstoX")
    st.subheader("Gerencie o estoque da sua loja com o melhor dos gerenciadores do mercado!")
    st.image("https://cdn-icons-png.flaticon.com/512/18715/18715864.png",
            use_container_width=False)
    st.write("""
    O estoX é um gerenciador de estoque que lhe permite planejar, controlar e otimizar de forma dinâmica seus clientes e produtos.
            Desfrute de nossas funcionalidades na aba ao lado.
    """)


elif menu == "Cadastrar Cliente":
    IncluirClientePage()
   
elif menu == "Adicionar Produto":
    CadatrarProdutosPage()

elif menu == "Listagem e Edição de Produtos":
    ListarProdutosPage()

elif menu == "Listagem e Edição de Clientes":
    ListarClientesPage()


elif menu == "Realizar Venda":
    RealizarVendaPage()

