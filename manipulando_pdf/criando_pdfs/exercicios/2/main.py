from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.image('python_banner.png', w=50, x='CENTER')

pdf.set_font('Helvetica', size=16)
pdf.cell(0, 10, text='Evento Python 2025 - Inscreva-se Já!',align='CENTER')

pdf.output('cartaz.pdf')