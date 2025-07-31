from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font('Helvetica', size=12)
pdf.multi_cell(0, 5, text="Bem-vindo ao curso **Python Automático**! Esperamos que você aproveite a jornada de aprendizado.", new_x="LMARGIN", new_y="NEXT")

pdf.ln(6)

pdf.multi_cell(0, 5, "Este curso foi preparado para iniciantes em automação com Python.", new_x="LMARGIN", new_y="NEXT")


pdf.output("apresentacao.pdf")