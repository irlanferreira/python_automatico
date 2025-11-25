import sqlite3

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
               id INTEGER PRIMARY KEY,
               nome TEXT NOT NULL,
               idade INTEGER NOT NULL,
               email TEXT NOT NULL);""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos(
               id INTEGER PRIMARY KEY,
               descricao TEXT NOT NULL,
               valor REAL NOT NULL,
               usuario_id INTEGER NOT NULL,
               FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
               )""")
conexao.commit()

def adicionar_usuario():
    print(f"{'='*20}Adicionar Usuários{'='*20}")
    while True:
        usuario_nome = input("Digite o nome do usuário (deixe vazio para sair): ")
        if usuario_nome == "":
            break
        usuario_idade = int(input("Digite a idade do usuário: "))
        usuario_email = input("Digite o email do usuário: ")

        cursor.execute("INSERT INTO usuarios (nome, idade, email) VALUES (?, ?, ?)", (usuario_nome, usuario_idade, usuario_email))
        print(f"Usuário {usuario_nome} adicionado com sucesso!\n")
        conexao.commit()

def exibir_usuarios(opcao=2):
    filtro = ""
    match opcao:
        case "2":
            filtro = "ORDER BY nome ASC"
        case "2.1":
            filtro = "WHERE idade < 18"
        case "2.2":
            filtro = "WHERE idade > 17"
    print(filtro)
    cursor.execute(f"SELECT * FROM usuarios {filtro}")
    usuarios = cursor.fetchall()
    print(f"{'='*20}Usuários{'='*20}")
    for usuario in usuarios:
        id, nome, idade, email = usuario
        print(f"Id: {id}\nNome: {nome}\nIdade: {idade}\nemail: {email}\n{'='*10}")
    print("\n")

def editar_usuario():
    usuario_id = input("Qual usuário deseja editar? (digite seu id): ")
    campo_opcao = input("Qual campo deseja alterar?\n1. Nome\n2. Idade\n3. Email\n4. Telefone\n: ")
    match campo_opcao:
        case "1":
            campo_opcao = "nome"
        case "2":
            campo_opcao = "idade"
        case "3":
            campo_opcao = "email"
        case "4":
            campo_opcao = "telefone"
    novo_valor = input(f"Digite o novo valor de {campo_opcao}: ")

    cursor.execute(f"UPDATE usuarios SET {campo_opcao} = ? WHERE id = ?", (novo_valor, usuario_id))
    conexao.commit()
    print("Usuário alterado com sucesso!\n")

def deletar_usuario():
    usuario_id = input("Qual usuário deseja deletar? (digite seu id): ")
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id))
    conexao.commit()
    print("Usuário deletado com sucesso!\n")


def adicionar_pedido():
    print(f"{'='*20}Adicionar Pedido{'='*20}")
    descricao = input("Digite o item do pedido: ")
    valor = int(input("Digite o valor do pedido: "))
    usuario_id = input("Digite o id do usuário que fez o pedido: ")

    cursor.execute("INSERT INTO pedidos (descricao, valor, usuario_id) VALUES (?, ?, ?)", (descricao, valor, usuario_id))
    print(f"Pedido adicionado com sucesso!\n")
    conexao.commit()

def exibir_pedidos(opcao="6"):
    filtro = ""
    if opcao == "7":
        usuario_id = input("Digite o id do usuário: ")
        filtro = f"WHERE usuario_id = {usuario_id}"
    cursor.execute(f"""
SELECT pedidos.id, pedidos.descricao, pedidos.valor, usuarios.nome FROM pedidos
JOIN usuarios
ON pedidos.usuario_id = usuarios.id {filtro}""")
    pedidos = cursor.fetchall()
    for pedido in pedidos:
        pedido_id, pedido_descricao, pedido_valor, usuario_nome = pedido
        print(f"{pedido_id}. {pedido_descricao} | {pedido_valor}R$ | {usuario_nome}\n")
    print(f"\n")
    
def deletar_pedido():
    pedido_id = input("Qual pedido deseja deletar? (digite o id): ")
    cursor.execute("DELETE FROM pedidos WHERE id = ?", (pedido_id))
    conexao.commit()
    print("Pedido deletado com sucesso!\n")

while True:
    opcao = input("""O que deseja fazer?
0. Sair
1. Adicionar Usuários
2. Exibir Usuários
    2.1. Exibir Usuários menores de idade
    2.2. Exibir Usuários maiores de idade
3. Editar Usuário
4. Deletar Usuário
5. Adicionar Pedido
6. Exibir Pedidos
7. Exibir Pedidos de usuário
8. Deletar Pedido
: """)
    match opcao:
        case "0":
            break
        case "1":
            adicionar_usuario()
        case "2" | "2.1" | "2.2":
            exibir_usuarios(opcao)
        case "3":
            editar_usuario()
        case "4":
            deletar_usuario()
        case "5":
            adicionar_pedido()
        case "6":
            exibir_pedidos()
        case "7":
            exibir_pedidos(opcao)
        case "8":
            deletar_pedido()