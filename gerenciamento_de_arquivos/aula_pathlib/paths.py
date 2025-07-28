from pathlib import Path

# caminho = Path("arquivinho.txt")
# caminho_absoluto = caminho.absolute()

# print(caminho_absoluto)

# print(caminho)

# caminho = Path("arquivinho.txt")
# if caminho.exists():
#     print("Existe!")
# else:
#     print("Existe não!")

# caminho = Path("pastinha")

# if caminho.is_file():
#     print("É arquivo!")
# elif caminho.is_dir():
#     print("É uma pasta!")

# nova_pasta = Path("NovaPasta/outraPasta/maisUmaPasta")
# nova_pasta.mkdir(exist_ok=True, parents=True)

# arquivinho = Path("arquivinho.txt")
# novapasta = Path("NovaPasta")

# # arquivinho.unlink()
# novapasta.rmdir()

# arquivinho = Path("arquivinho.txt")
# texto = arquivinho.read_text()
# print(texto)
# arquivinho.write_text("Alguma frase aí", encoding='utf-8')

# pasta = Path("minha_pasta")
# for arquivo in pasta.glob("*.txt"):
#     print(arquivo)

# caminho = Path("minha_pasta/dados.xlsx")

# print(caminho)

# print(caminho.name)

# print(caminho.stem)

# print(caminho.suffix)

arquivo = Path("meu_arquivo.txt")
arquivo.touch()