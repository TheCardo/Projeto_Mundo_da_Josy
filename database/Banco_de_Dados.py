import sqlite3
banco = sqlite3.connect("Mundo_da_Josy.db")
cursor = banco.cursor()
cursor.execute("CREATE TABLE clientes (nome, telefone,data de nascimento, cpf) ")

cursor.execute ("CREATE TABLE produtos (id, nome, marca, categoria, lote, validade)")