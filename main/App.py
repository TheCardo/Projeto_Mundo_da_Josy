import sqlite3
from datetime import datetime
from validadores import validar_cpf, validar_data_nascimento, validar_telefone, validar_validade





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

def adicionar_produtos(nome, marca, categoria, lote, validade, quantidade):
    if not validar_validade(validade):
        return 'data de validade inválida'
    try:
        banco = sqlite3.connect("Mundo_da_Josy.db")
        cursor = banco.cursor()

        cursor.execute("""INSERT INTO produtos (nome, marca, categoria, lote, validade, quantidade)
                       VALUES(?,?,?,?,?,?)
                       """,(nome, marca, categoria, lote, validade, quantidade))
        banco.commit()
        return "produto adicionado com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao adicionar produto: {erro}"
    finally:
        banco.close()


def listar_produtos():

    banco = sqlite3.connect("Mundo_da_Josy.db")
    cursor = banco.cursor()

    cursor.execute('SELECT * FROM produtos')
    for linha in cursor.fetchall():
        print (linha)


    banco.close()
    
 
def editar_produtos(id, nova_quantidade):
    
    banco = sqlite3.connect("Mundo_da_Josy.db")
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
    banco.close()


def excluir_produto(id,nome):
    banco = sqlite3.connect("Mundo_da_Josy.db")
    cursor = banco.cursor()
    cursor.execute (' DELETE FROM produtos WHERE id = ?',(id,))
    
    banco.commit()
    banco.close()
def realizar_venda(valor, data, id_cliente, id_produto):
    try:
        banco = sqlite3.connect("Mundo_da_Josy.db")
        cursor = banco.cursor()

        cursor.execute("SELECT * FROM clientes WHERE id = ?", (id_cliente,))
        cliente = cursor.fetchone()
        if not cliente:
            return "Cliente não encontrado."
        
        cursor.execute("SELECT quantidade FROM produtos WHERE id = ?", (id_produto,))
        produto = cursor.fetchone()
        if not produto:
            return "Produto não encontrado."
        if produto[0] < quantidade:
            return "Quantidade em estoque insuficiente."
        
        data_atual = datetime.now().strftime("%d/%m/%Y")
        cursor.execute("""
            INSERT INTO vendas (valor, data, id_cliente, id_produto)
            VALUES (?, ?, ?, ?)
        """, (valor, data_atual, id_cliente, id_produto))

        nova_quantidade = produto[0] - quantidade
        cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id_produto))

        banco.commit()
        return "Venda registrada com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao registrar venda: {erro}"
    finally:
        banco.close()


#adicionar_clientes("Chico", "81989668877","20/05/2003","12345678910")
#adicionar_produtos("ilia","natura","perfume","35","20/05/2027",15)
#print(adicionar_produtos("Produto Teste", "Marca Teste", "Categoria Teste", "123", "31/12/2025", 10))
#listar_produtos()
#excluir_produto(8,"Produto Teste")
editar_produtos(1,10)