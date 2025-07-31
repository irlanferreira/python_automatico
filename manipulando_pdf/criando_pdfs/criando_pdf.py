from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font('Helvetica', size=16)
pdf.cell(0, 10, text="Título de Exemplo", new_x='LMARGIN', new_y='NEXT')

pdf.ln(10)

pdf.set_font("Helvetica", size=12)
pdf.cell(0, 5, text="Eu sou um --parágrafo--", new_x="LMARGIN", new_y="NEXT", markdown=True)
pdf.ln(5)

pdf.multi_cell(0, 5, text="Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! Eu sou um parágrafo! ")
pdf.ln(10)

pdf.image("logo_Python.png", w=30, x='CENTER')

pdf.output('exemplo.pdf')