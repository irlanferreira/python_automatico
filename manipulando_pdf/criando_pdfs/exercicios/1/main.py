from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font('Helvetica', size=16)
pdf.cell(0, 10, text='Relatório de Vendas - Junho 2025')
pdf.ln(20)

pdf.set_font('Helvetica', size=12)
pdf.multi_cell(0, 5, text='As vendas de junho apresentaram um crescimento significativo em relação ao mês anterior, impulsionadas por campanhas promocionais e novos lançamentos.')

pdf.ln(8)

pdf.multi_cell(0, 5, text='A previsão para o próximo mês é de continuidade do crescimento, especialmente no setor de tecnologia.')

pdf.output('relatorio.pdf')