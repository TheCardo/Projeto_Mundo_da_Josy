import streamlit as st 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pacote.sub_pacote.funcoes import realizar_venda


def RealizarVendaPage():
    st.title("Realizar Venda")
    with st.form(key="form_venda"):
        valor = st.number_input("Valor da Venda:", min_value=0.0, step=0.01)
        quantidade = st.number_input("Quantidade:", min_value=1, step=1)
        cpf = st.text_input("CPF do CLiente:")
        id_produto = st.number_input("ID do Produto:", min_value=1, step=1)

        botao_submit = st.form_submit_button("Registrar Venda")

    if botao_submit:
        if valor and quantidade and cpf and id_produto:
            resultado = realizar_venda(valor, quantidade, cpf, id_produto)
            if resultado == "Venda registrada com sucesso!":
                st.success(resultado)
            else:
                st.error(resultado)
        else:
            st.error("Por favor, preencha todos os campos corretamente!")

