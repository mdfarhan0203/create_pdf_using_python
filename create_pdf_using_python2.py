from fpdf import FPDF
pdf=FPDF()
pdf.add_page()
pdf.set_font("Arial",size=20)

pdf.cell(200,10,txt="Dynamic programmin languag",ln=1,align="c")
pdf.cell(200,10,txt="A place for python programming langguae",ln=2,align="c")
pdf.cell(200,10,txt="nice learning ",ln=2,align="c")
pdf.output("python_created_pdf.pdf")