import re
from pypdf import PdfReader

def retornar_datas(texto:str):
    datas = []
    expressao = r"\d{2}/\d{2}/\d{4}"
    resultados = re.findall(expressao, texto)
    if resultados:
        for resultado in resultados:
            datas.append(resultado)
    return datas

def retornar_vendas(produtos:list, texto:str):
    vendas = {}
    for produto in produtos:
        expressao = rf"({produto}):\s*(\d+)\s*unidades"
        resultados = re.findall(expressao, texto)
        if resultados:
            soma = 0
            for resultado in resultados:
                soma += int(resultado[1])
            vendas[produto] = soma
    
    return vendas

vendas_relatorio = PdfReader("vendas.pdf")
print(f"Número de páginas: {len(vendas_relatorio.pages)}")

texto_completo = ""
for pagina in vendas_relatorio.pages:
    texto_completo += pagina.extract_text()

with open("resumo_vendas.txt", 'w', encoding='utf-8') as arquivo:
    arquivo.write("RELATÓRIO DE VENDAS\n")
    arquivo.write("="*30)
    arquivo.write('\n')

    arquivo.write("DATAS ENCONTRADAS:\n")
    for data in retornar_datas(texto_completo):
        arquivo.write(f"{data}\n")
    
    lista_produtos = ['Mouse', 'Teclado']
    produtos = retornar_vendas(lista_produtos, texto_completo)

    arquivo.write("\nPRODUTOS:\n")

    for produto, qtd in produtos.items():
        arquivo.write(f"{produto}: {qtd}\n")
    