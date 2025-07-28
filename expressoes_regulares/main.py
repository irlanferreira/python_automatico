import re

# texto = "Eu tenho um gato"
# expressao = 'gato'

# resultado = re.search(expressao, texto)

# if resultado:
#     print(resultado.group())
# else:
#     print("Não encontrei")

# texto = "Meu número é 98894-7890, o do meu amigo é 57694-8238"
# expressao = r"\d{5}-\d{4}"

# resultados = re.findall(expressao, texto)
# if resultados:
#     print("Números encontrados:")
#     for resultado in resultados:
#         print(resultado)

# texto = "Data de hoje: 28/07/2025... A data de amanhã é 29-07-2025"
# expresso = r"\d{2}[/-]\d{2}[/-]\d{4}"

# novo_texto = re.sub(expresso, 'XX/XX/XXXX', texto)

# print(novo_texto)

texto = "Meu e-mail é irlan@gmail.com. O do meu amigo é joao@gmail.com"
expressao = r"\w+@\w+\.\w+"

resultados = re.findall(expressao, texto)
if resultados:
    for resultado in resultados:
        print(resultado)