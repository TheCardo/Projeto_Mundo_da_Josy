import sqlite3
from datetime import datetime
import pandas as pd

def connect_db():
    return sqlite3.connect("estoX.db")



#CRUD
def adicionar_clientes(nome, telefone, data_nascimento, cpf):
    if not validar_cpf(cpf):
        return 'CPF invalido. por favor insira um cpf com 11 digitos (apenas números)'
    if not validar_telefone(telefone):
        return 'telefone invalido' 
    banco = None
    try:
        banco = connect_db()
        cursor = banco.cursor()

        cursor.execute("""INSERT INTO clientes (nome, telefone, data_nascimento, cpf)
                        VALUES (?, ?, ?, ?) 
                        """, (nome, telefone, data_nascimento, cpf))
        banco.commit()
        return "Cliente adicionado com sucesso!"
    except sqlite3.Error as erro:
        if banco:
            banco.rollback()
        return f"Erro ao adicionar cliente: {erro}"
    finally:
        if banco:
            banco.close()

def adicionar_produtos(nome, marca, categoria, lote, validade, quantidade):
    banco = None
    try:
        banco = connect_db()
        cursor = banco.cursor()

        cursor.execute("""INSERT INTO produtos (nome, marca, categoria, lote, validade, quantidade)
                       VALUES(?,?,?,?,?,?)
                       """,(nome, marca, categoria, lote, validade, quantidade))
        banco.commit()
        return "produto adicionado com sucesso!"
    except sqlite3.Error as erro:
        if banco:
            banco.rollback()
        return f"Erro ao adicionar produto: {erro}"
    finally:
        if banco:
            banco.close()

def listar_produtos():
    banco = None
    try:
        banco = connect_db()
        cursor = banco.cursor()

        cursor.execute('SELECT * FROM produtos')
        produtos = cursor.fetchall()
        return produtos
    except sqlite3.Error as erro:
        return f"Erro ao listar produtos: {erro}"
    finally:
        if banco:
            banco.close()

def editar_produtos(id, nova_quantidade):
    banco = None
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("SELECT nome, quantidade From produtos Where id = ?",(id,))
        produto = cursor.fetchone()
        if produto is None:
            print ( f"produto com {id} não encontrado.")
        else:
            nome_do_produto, quantidade_anterior = produto
            print (f"produto encontrado: {nome_do_produto}")
            print (f" quantidade antes: {quantidade_anterior} | quantidade atual {nova_quantidade}")
        
        
        cursor.execute("""
                    
                UPDATE  produtos
                SET quantidade = ? 
                WHERE id = ?
                    
                """,(nova_quantidade, id))
    
        banco.commit()
    except sqlite3.Error as erro:
        if banco:
            banco.rollback()
            return f'erro ao editar o produto: {erro}'
    finally:
        if banco:
            banco.close()

def excluir_produto(id,):
    banco = None
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute (' DELETE FROM produtos WHERE id = ?',(id,))
        banco.commit()
    except sqlite3.Error as erro:
        if banco:
            banco.rollback()
        return f"Erro ao excluir produto: {erro}"
    finally:
        if banco:
            banco.close()

def realizar_venda(valor, quantidade, cpf, id_produto):
    banco = None
    try:
        banco = connect_db()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM clientes WHERE cpf = ?", (cpf,))
        cliente = cursor.fetchone()
        if not cliente:
            return "Cliente não encontrado."
        
        cursor.execute("SELECT quantidade FROM produtos WHERE id = ?", (id_produto,))
        produto = cursor.fetchone()
        if not produto:
            return "Produto não encontrado."
        if produto[0] < quantidade:
            return "Quantidade em estoque insuficiente."
        
        data_atual = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        cursor.execute("""
            INSERT INTO vendas (valor, data, id_cliente, id_produto)
            VALUES (?, ?, ?, ?)
        """, (valor, data_atual, cpf, id_produto))

        nova_quantidade = produto[0] - quantidade
        cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id_produto))

        banco.commit()
        return "Venda registrada com sucesso!"
    except sqlite3.Error as erro:
        if banco:
            banco.rollback()
        return f"Erro ao registrar venda: {erro}"
    finally:
        if banco:
            banco.close()

def listar_clientes():
    banco = None
    try:
        banco = connect_db()
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return clientes
    except sqlite3.Error as erro:
        return f"Erro ao listar clientes: {erro}"
    finally:
        if banco:
            banco.close()
#edição de clientes ---------------------------------------------------
def editar_nome_cliente(id, novo_nome):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE clientes SET nome = ? WHERE id = ?", (novo_nome, id))
        banco.commit()
        return "Nome atualizado com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar o nome: {erro}"
    finally:
        banco.close()

def editar_telefone_cliente(id, novo_telefone):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE clientes SET telefone = ? WHERE id = ?", (novo_telefone, id))
        banco.commit()
        return "Telefone atualizado com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar o telefone: {erro}"
    finally:
        banco.close()

def editar_cpf_cliente(id, novo_cpf):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE clientes SET cpf = ? WHERE id = ?", (novo_cpf, id))
        banco.commit()
        return "CPF atualizado com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar o CPF: {erro}"
    finally:
        banco.close()

def editar_data_nascimento_cliente(id, nova_data_nascimento):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE clientes SET data_nascimento = ? WHERE id = ?", (nova_data_nascimento, id))
        banco.commit()
        return "Data de nascimento atualizada com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar a data de nascimento: {erro}"
    finally:
        banco.close()
#----------------------------------------------------------------------

#validações
def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) == 11

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11
#consultas para a interface gráfica
def vendas_totais_mes():
    banco = connect_db()
    cursor = banco.cursor()
    cursor.execute("""
        SELECT strftime('%m/%Y', data) as mes_ano, SUM(valor) 
        FROM vendas 
        GROUP BY mes_ano 
        ORDER BY data
    """)
    resultado = cursor.fetchall()
    banco.close()
    return pd.DataFrame(resultado, columns=["Mês/Ano", "Total Vendas"])

def produtos_mais_vendidos():
    banco = connect_db()
    cursor = banco.cursor()
    cursor.execute("""
        SELECT p.nome, COUNT(v.id_produto) as total_vendas
        FROM vendas v
        JOIN produtos p ON v.id_produto = p.id
        GROUP BY v.id_produto
        ORDER BY total_vendas DESC
        LIMIT 5
    """)
    resultado = cursor.fetchall()
    banco.close()
    return pd.DataFrame(resultado, columns=["Produto", "Quantidade Vendida"])

def clientes_mais_compraram():
    banco = connect_db()
    cursor = banco.cursor()
    cursor.execute("""
        SELECT c.nome, COUNT(v.id) as total_compras, SUM(v.valor) as total_gasto
        FROM vendas v
        JOIN clientes c ON v.id_cliente = c.id
        GROUP BY v.id_cliente
        ORDER BY total_gasto DESC
        LIMIT 5
    """)
    resultado = cursor.fetchall()
    banco.close()
    return pd.DataFrame(resultado, columns=["Cliente", "Total Compras", "Total Gasto"])

def ticket_medio():
    banco = connect_db()
    cursor = banco.cursor()
    cursor.execute("""
        SELECT AVG(total_gasto) FROM (
            SELECT SUM(valor) as total_gasto FROM vendas GROUP BY id_cliente
        )
    """)
    resultado = cursor.fetchone()[0]
    banco.close()
    return resultado if resultado else 0

def produtos_perto_validade():
    banco = connect_db()
    cursor = banco.cursor()
    cursor.execute("""
        SELECT nome, validade FROM produtos 
        WHERE validade <= date('now', '+30 days')
        ORDER BY validade ASC
    """)
    resultado = cursor.fetchall()
    banco.close()
    return pd.DataFrame(resultado, columns=["Produto", "Validade"])

def produtos_baixo_estoque():
    banco = connect_db()
    cursor = banco.cursor()
    cursor.execute("""
        SELECT nome, quantidade FROM produtos 
        WHERE quantidade <= 5
        ORDER BY quantidade ASC
    """)
    resultado = cursor.fetchall()
    banco.close()
    return pd.DataFrame(resultado, columns=["Produto", "Quantidade"])

def produtos_menos_vendidos():
    banco = connect_db()
    cursor = banco.cursor()
    cursor.execute("""
        SELECT p.nome, COUNT(v.id_produto) as total_vendas
        FROM vendas v
        JOIN produtos p ON v.id_produto = p.id
        GROUP BY v.id_produto
        ORDER BY total_vendas ASC
        LIMIT 5
    """)
    resultado = cursor.fetchall()
    banco.close()
    return pd.DataFrame(resultado, columns=["Produto", "Quantidade Vendida"])
#------------------------------------------- 