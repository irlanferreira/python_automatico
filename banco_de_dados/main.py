import sqlite3

conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# cursor.execute("DROP TABLE IF EXISTS produtos")
# cursor.execute("""
# CREATE TABLE produtos(
#                id INTEGER PRIMARY KEY,
#                nome TEXT NOT NULL,
#                preco REAL NOT NULL)""")

# produto_nome = input("Qual o nome do produto?: ")
# produto_preco = float(input("Qual o preço do produto?: "))

# cursor.execute("INSERT INTO produtos (nome, preco) VALUES (?,?)", (produto_nome, produto_preco))
cursor.execute("SELECT * FROM produtos WHERE preco < ?", ("5"))
produtos = cursor.fetchall()
for produto in produtos:
    id, nome, preco = produto
    print(f"Nome: {nome}\nPreço: {preco}\n\n")
conexao.commit()