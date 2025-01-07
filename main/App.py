import sqlite3
from datetime import datetime
from validadores import validar_cpf, validar_data_nascimento, validar_telefone

def adicionar_clientes(nome, telefone, data_nascimento, cpf):
    if not validar_cpf(cpf):
        return 'cpf invalido'
    if not validar_telefone(telefone):
        return 'telefone invalido'
    if not validar_data_nascimento(data_nascimento):
        return 'data de nascimento invalida' 
    try:
        banco = sqlite3.connect("Mundo_da_Josy.db")
        cursor = banco.cursor()

        cursor.execute("""INSERT INTO clientes (nome, telefone, data_nascimento, cpf)
                        VALUES (?, ?, ?, ?) 
                        """, (nome, telefone, data_nascimento, cpf))
        banco.commit()
        return "Cliente adicionado com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao adicionar cliente: {erro}"
    finally:
        banco.close()
adicionar_clientes('ricardo', '81994602580', '4/12/2003', '12345678912')