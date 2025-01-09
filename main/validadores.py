from datetime import datetime


def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) == 11

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11


def validar_data_nascimento(data_nascimento):
    try:
        datetime.strptime(data_nascimento, "%d/%m/%Y")
        return True
    except ValueError:
        return False
       
def validar_validade(validade):
    try:
        datetime.strptime(validade, "%d/%m/%Y")
        return True
    except ValueError:
        return False