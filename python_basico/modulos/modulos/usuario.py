def criar_perfil(nome, idade):
    dicionario = {
        "nome":nome,
        "idade":idade
    }
    return dicionario

def validar_idade(idade):
    if idade >= 18:
        return True
    else:
        return False