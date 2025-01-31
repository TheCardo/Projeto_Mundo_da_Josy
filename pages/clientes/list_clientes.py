import streamlit as st 
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pacote.sub_pacote.funcoes import listar_clientes, editar_clientes
from App import excluir_cliente


import streamlit as st 
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pacote.sub_pacote.funcoes import listar_clientes
from App import excluir_cliente
import streamlit as st 
import pandas as pd
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from pacote.sub_pacote.funcoes import listar_clientes
from App import excluir_cliente

def atualizar_clientes():
    st.session_state.clientes = listar_clientes()

def ListarClientesPage():
    st.subheader("Lista de Clientes")

    if "clientes" not in st.session_state:
        atualizar_clientes()

    df_clientes = pd.DataFrame(st.session_state.clientes, columns=["ID", "Nome", "Telefone", "Data de Nascimento", "CPF"])
    st.table(df_clientes)

    for i, row in df_clientes.iterrows():
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.text(f"{row['Nome']} / Telefone: {row['Telefone']} / CPF: ({row['CPF']})")
        col2.button("Excluir", key=f"excluir_{row['ID']}", on_click=excluir_cliente, args=(row["ID"],), kwargs={}, help="Remove o cliente e atualiza a lista automaticamente")
        col3.button("Editar", key=f"editar_{row['ID']}")   
    if "clientes" in st.session_state:
        atualizar_clientes()
