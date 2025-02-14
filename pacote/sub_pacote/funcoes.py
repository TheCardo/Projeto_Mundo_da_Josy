import sqlite3
from datetime import datetime
import pandas as pd


def connect_db():
    return sqlite3.connect("estoX.db")

#=========================================================================================
banco = connect_db()
cursor = banco.cursor()

query_produtos = '''INSERT INTO produtos (nome, marca, categoria, quantidade, lote, validade) VALUES
('Shampoo Hidratante', 'Pantene', 'Cosméticos', 15, 'A001', '2026-12-15'),
('Condicionador Nutritivo', 'L’Oréal', 'Cosméticos', 20, 'A002', '2026-10-10'),
('Sabonete Líquido', 'Dove', 'Higiene', 30, 'A003', '2027-05-20'),
('Creme para Pentear', 'Salon Line', 'Beleza', 25, 'A004', '2025-11-30'),
('Base Líquida', 'Maybelline', 'Cosméticos', 10, 'A005', '2026-08-15'),
('Perfume Floral', 'O Boticário', 'Cuidados Pessoais', 8, 'A006', '2028-04-10'),
('Hidratante Corporal', 'Nivea', 'Cosméticos', 18, 'A007', '2027-07-22'),
('Pó Compacto', 'Vult', 'Beleza', 12, 'A008', '2026-09-18'),
('Máscara de Cílios', 'Avon', 'Beleza', 14, 'A009', '2027-01-05'),
('Batom Matte', 'MAC', 'Cosméticos', 20, 'A010', '2026-03-14'),
('Óleo Capilar', 'Elseve', 'Cosméticos', 17, 'A011', '2027-06-30'),
('Protetor Solar FPS 50', 'Neutrogena', 'Cuidados Pessoais', 10, 'A012', '2026-12-01'),
('Lenços Umedecidos', 'Huggies', 'Higiene', 22, 'A013', '2027-08-12'),
('Desodorante Roll-on', 'Rexona', 'Cuidados Pessoais', 28, 'A014', '2027-03-20'),
('Creme Dental', 'Colgate', 'Higiene', 35, 'A015', '2028-02-28'),
('Escova de Dentes', 'Oral-B', 'Higiene', 40, 'A016', '2030-01-01'),
('Sabonete Esfoliante', 'Granado', 'Higiene', 16, 'A017', '2026-05-17'),
('Kit Pincéis de Maquiagem', 'Ruby Rose', 'Beleza', 7, 'A018', '2029-07-14'),
('Creme Antirrugas', 'La Roche-Posay', 'Cosméticos', 9, 'A019', '2028-10-30'),
('Tônico Facial', 'The Body Shop', 'Cosméticos', 11, 'A020', '2027-09-09'),
('Shampoo Detox', 'TRESemmé', 'Cosméticos', 18, 'A021', '2026-11-23'),
('Máscara Capilar', 'Novex', 'Cosméticos', 14, 'A022', '2027-04-19'),
('Gel Fixador', 'Bozzano', 'Beleza', 15, 'A023', '2027-07-07'),
('Perfume Amadeirado', 'Natura', 'Cuidados Pessoais', 6, 'A024', '2028-05-03'),
('Tônico Adstringente', 'Neutrogena', 'Cuidados Pessoais', 8, 'A025', '2026-12-27'),
('Creme Hidratante para Mãos', 'Avène', 'Cosméticos', 13, 'A026', '2028-08-21'),
('Serum Facial', 'The Ordinary', 'Cosméticos', 10, 'A027', '2029-01-09'),
('Lápis de Olho', 'Quem Disse, Berenice?', 'Beleza', 16, 'A028', '2026-06-11'),
('Esmalte Vermelho', 'Risqué', 'Beleza', 25, 'A029', '2027-03-15'),
('Kit de Cuidados com a Pele', 'Mary Kay', 'Cosméticos', 5, 'A030', '2029-12-10'),
('Sabonete Íntimo', 'Dermacyd', 'Higiene', 19, 'A031', '2028-04-22'),
('Creme para Estrias', 'Bio-Oil', 'Cuidados Pessoais', 12, 'A032', '2027-11-30'),
('Condicionador Matizador', 'Yellow', 'Cosméticos', 9, 'A033', '2026-09-05'),
('Fixador de Maquiagem', 'Klass Vough', 'Beleza', 7, 'A034', '2028-03-01'),
('Sabonete de Enxofre', 'Granado', 'Higiene', 14, 'A035', '2027-06-14'),
('Kit de Barbear', 'Gillette', 'Cuidados Pessoais', 11, 'A036', '2026-07-07'),
('Shampoo Anticaspa', 'Clear', 'Cosméticos', 13, 'A037', '2027-10-19'),
('Máscara Facial de Argila', 'Lush', 'Cosméticos', 8, 'A038', '2028-01-29'),
('Creme Clareador de Manchas', 'Nivea', 'Cosméticos', 10, 'A039', '2028-06-18'),
('Protetor Labial', 'Bepantol', 'Cuidados Pessoais', 20, 'A040', '2029-02-05');
'''

cursor.executescript(query_produtos)

banco.commit()
banco.close()

print("40 produtos adicionados com sucesso!")

#=======================================================================================

banco = connect_db()
cursor = banco.cursor()

query_clientes = '''INSERT INTO clientes (cpf, nome, telefone, data_nascimento) VALUES
('12345678900', 'Ana Souza', 11987654321, '1995-06-12'),
('23456789011', 'Bruno Lima', 11976543210, '1988-09-25'),
('34567890122', 'Carlos Mendes', 11965432109, '1992-04-17'),
('45678901233', 'Daniela Castro', 11954321098, '1997-11-30'),
('56789012344', 'Eduardo Silva', 11943210987, '1985-03-05'),
('67890123455', 'Fernanda Alves', 11932109876, '1999-07-20'),
('78901234566', 'Gabriel Oliveira', 11921098765, '2001-01-10'),
('89012345677', 'Helena Santos', 11910987654, '1994-05-22'),
('90123456788', 'Igor Martins', 11999887766, '1989-10-15'),
('01234567899', 'Juliana Pereira', 11988776655, '1996-12-08'),
('11112222333', 'Karina Fernandes', 11977665544, '1991-02-14'),
('22223333444', 'Lucas Costa', 11966554433, '1986-08-29'),
('33334444555', 'Mariana Rocha', 11955443322, '1998-06-04'),
('44445555666', 'Nathan Borges', 11944332211, '1993-09-19'),
('55556666777', 'Olívia Ribeiro', 11933221100, '2000-11-25'),
('66667777888', 'Paulo Teixeira', 11922110099, '1987-07-13'),
('77778888999', 'Rafaela Nunes', 11911009988, '1995-03-07'),
('88889999000', 'Samuel Batista', 11900998877, '1990-05-30'),
('99990000111', 'Tatiane Moreira', 11919876543, '1997-12-02'),
('00001111222', 'Vinícius Lopes', 11928765432, '2002-04-18');
'''
cursor.executescript(query_clientes)

banco.commit()
banco.close()

print("20 clientes adicionados com sucesso!")
#============================================================================================

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
        return "Produto adicionado com sucesso!"
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
        banco = sqlite3.connect("estoX.db")
        cursor = banco.cursor()
        cursor.execute("SELECT cpf FROM clientes WHERE cpf = ?", (cpf,))
        cliente = cursor.fetchone()
        if not cliente:
            return "Cliente não encontrado."
        cpf_cliente = cliente[0]

        cursor.execute("SELECT quantidade FROM produtos WHERE id = ?", (id_produto,))
        produto = cursor.fetchone()
        if not produto:
            return "Produto não encontrado."
        if produto[0] < quantidade:
            return "Quantidade insuficiente no estoque."

        data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("""
            INSERT INTO vendas (valor, data, cpf_cliente, id_produto)
            VALUES (?, ?, ?, ?)
        """, (valor, data_atual, cpf_cliente, id_produto))

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

#edição de produtos ---------------------------------------------------

def editar_nome_produto(id, novo_nome):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE produtos SET nome = ? WHERE id = ?", (novo_nome, id))
        banco.commit()
        return "Nome atualizado com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar o nome: {erro}"
    finally:
        banco.close()

def editar_marca_produto(id, nova_marca):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE produtos SET marca = ? WHERE id = ?", (nova_marca, id))
        banco.commit()
        return "Marca atualizada com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar a marca: {erro}"
    finally:
        banco.close()

def editar_categoria_produto(id, nova_categoria):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE produtos SET categoria = ? WHERE id = ?", (nova_categoria, id))
        banco.commit()
        return "Categoria atualizada com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar a categoria: {erro}"
    finally:
        banco.close()

def editar_lote_produto(id, novo_lote):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE produtos SET lote = ? WHERE id = ?", (novo_lote, id))
        banco.commit()
        return "Lote atualizado com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar o lote: {erro}"
    finally:
        banco.close()

def editar_validade_produto(id, nova_validade):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE produtos SET validade = ? WHERE id = ?", (nova_validade, id))
        banco.commit()
        return "Data de validade atualizada com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar a validade: {erro}"
    finally:
        banco.close()

def editar_quantidade_produto(id, nova_quantidade):
    try:
        banco = connect_db()
        cursor = banco.cursor()
        cursor.execute("UPDATE produtos SET quantidade = ? WHERE id = ?", (nova_quantidade, id))
        banco.commit()
        return "Quantidade atualizada com sucesso!"
    except sqlite3.Error as erro:
        return f"Erro ao editar a quantidade: {erro}"
    finally:
        banco.close()
#-----------------------------------------------------------------------


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
        JOIN clientes c ON cpf_cliente = c.cpf
        GROUP BY v.cpf_cliente
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
            SELECT SUM(valor) as total_gasto FROM vendas GROUP BY cpf_cliente
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


