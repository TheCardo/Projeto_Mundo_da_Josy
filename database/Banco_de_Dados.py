import sqlite3

banco = sqlite3.connect("estoX.db")
cursor = banco.cursor()
# cursor.execute("DROP TABLE IF EXISTS vendas")
# cursor.execute("DROP TABLE IF EXISTS produtos")
# cursor.execute("DROP TABLE IF EXISTS clientes") para caso eu precise refazer as tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    cpf TEXT PRIMARY KEY,
    nome TEXT NOT NULL,
    telefone INTEGER NOT NULL,
    data_nascimento DATE NOT NULL)
''')


cursor.execute('''
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
    cpf_cliente TEXT,
    id_produto INTEGER,
    FOREIGN KEY(cpf_cliente) REFERENCES clientes(cpf),
    FOREIGN KEY(id_produto) REFERENCES produtos(id))
''')

banco.commit()
banco.close()
