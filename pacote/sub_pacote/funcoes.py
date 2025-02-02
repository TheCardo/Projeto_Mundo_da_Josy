import sqlite3
from datetime import datetime



def adicionar_clientes(nome, telefone, data_nascimento, cpf):
    if not validar_cpf(cpf):
        return 'CPF invalido. por favor insira um cpf com 11 digitos (apenas números)'
    if not validar_telefone(telefone):
        return 'telefone invalido' 
    banco = None
    try:
        banco = sqlite3.connect("estoX.db")
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
        banco = sqlite3.connect("estoX.db")
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
        banco = sqlite3.connect("estoX.db")
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
        banco = sqlite3.connect("estoX.db")
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
        banco = sqlite3.connect("estoX.db")
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
        banco = sqlite3.connect("estoX.db")
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
        banco = sqlite3.connect("estoX.db")
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM clientes")
        clientes = cursor.fetchall()
        return clientes
    except sqlite3.Error as erro:
        return f"Erro ao listar clientes: {erro}"
    finally:
        if banco:
            banco.close()

def editar_clientes(id, nome_refatorado, telefone_refatorado, cpf_refatorado, data_nascimento_refatorado):
    banco = None
    try:
        banco = sqlite3.connect("estoX.db")
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id,))
        cliente = cursor.fetchone()

        if not cliente:
            return "Cliente não encontrado."

        cursor.execute("""
            UPDATE clientes
            SET nome = ?, telefone = ?, cpf = ?, data_nascimento = ?
            WHERE id = ?
        """, (nome_refatorado, telefone_refatorado, cpf_refatorado, data_nascimento_refatorado, id))

        banco.commit()
        return "Cliente atualizado com sucesso!"
    except sqlite3.Error as erro:
        if banco:
            banco.rollback()
        return f"Erro ao editar o cliente: {erro}"
    finally:
        if banco:
            banco.close()

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) == 11

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def vendas_totais_mes():
    banco = sqlite3.connect("estoX.db")
    cursor = banco.cursor()
    mes_atual = datetime.now().strftime("%m/%Y")
    cursor.execute("""
        SELECT SUM(valor) FROM vendas
        WHERE strftime('%m/%Y', data) = ?
    """, (mes_atual,))
    resultado = cursor.fetchone()[0]
    banco.close()
    return resultado if resultado else 0

def produtos_mais_vendidos():
    banco = sqlite3.connect("estoX.db")
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
    return resultado

def vendas_arrecadadas():
    banco = sqlite3.connect("estoX.db")
    cursor = banco.cursor()
    cursor.execute("SELECT SUM(valor) FROM vendas")
    resultado = cursor.fetchone()[0]
    banco.close()
    return resultado if resultado else 0

















# def validar_data_nascimento(data_nascimento):
#     try:
#         datetime.strptime(data_nascimento, "%d/%m/%Y")
#         return True
#     except ValueError:
#         return False
       
# def validar_validade(validade):
#     try:
#         datetime.strptime("validade", "%d/%m/%Y")
#         return True
#     except ValueError:
#         return False
    
editar_clientes("8", "matheus","81992456976", "24367845321", "25/02/2005")