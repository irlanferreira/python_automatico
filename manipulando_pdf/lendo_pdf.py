from pypdf import PdfReader

relatorio = PdfReader("relatorio_de_vendas.pdf")
for pagina in relatorio.pages:
    print(pagina.extract_text())