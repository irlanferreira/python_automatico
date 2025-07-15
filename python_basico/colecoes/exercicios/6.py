dicionario_correto = {
    'usuario': 'Lan',
    'senha': 456
}
dicionario_entrada = {
    'usuario': input("Digite seu usuário: "),
    'senha': int(input("Digite sua senha: "))
}

if dicionario_entrada['usuario'] == dicionario_correto['usuario'] and dicionario_entrada['senha'] == dicionario_correto['senha']:
    print("Acesso liberado! Pode entrar!")
else:
    print("Credenciais incorretas. Tente novamente.")