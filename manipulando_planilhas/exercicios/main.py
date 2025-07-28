from openpyxl import Workbook

arquivo = Workbook()
planilha_pessoas = arquivo.active
planilha_pessoas.title = 'Pessoas'

planilha_pessoas['A1'] = "Nome"
planilha_pessoas['B1'] = 'Cidade'

planilha_pessoas['A2'] = 'João'
planilha_pessoas['B2'] = "Recife"
planilha_pessoas['A3'] = "Mariana"
planilha_pessoas['B3'] = "São Paulo"
planilha_pessoas['A4'] = "Otávio"
planilha_pessoas['B4'] = "Belo Horizonte"

planilha_pessoas.append(['Letícia', 'Porto Alegre'])
planilha_pessoas.append(['Gustavo', 'Salvador'])

arquivo.create_sheet('visitas')
planilha_visitas = arquivo['visitas']

planilha_visitas.append(['01/01/2025', 134])
planilha_visitas.append(['02/01/2025', 156])

planilha_visitas['B2'] = 142

arquivo.save('pessoas.xlsx')