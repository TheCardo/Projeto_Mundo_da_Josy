import sqlite3
banco = sqlite3.connect("Mundo_da_Josy.db")
cursor = banco.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone INTEGER NOT NULL,
    data_nascimento DATE NOT NULL,
    cpf INTEGER NOT NULL)
               
''')

cursor.execute ('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    marca TEXT NOT NULL,
    categoria TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    lote TEXT NOT NULL,
    validade DATE NOT NULL)
                             
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    valor REAL NOT NULL,
    data DATE NOT NULL,
    id_cliente INTEGER,
    id_produto INTEGER,
    FOREIGN KEY(id_cliente) REFERENCES clientes(id),
    FOREIGN KEY(id_produto) REFERENCES produtos(id))
               
''')

banco.commit()
banco.close()



    