from fpdf import FPDF
from pathlib import Path

def save_to_pdf(slides, notes, filename="output/presentation.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.set_font("Helvetica", size=14)  # ✅ Use built-in font

    # Slide content
    pdf.add_page()
    pdf.cell(200, 10, txt="Slide Content", ln=True, align='C')
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 10, slides)

    # Optional image
    image_path = "output/slide_image_dalle.png"
    if Path(image_path).exists():
        pdf.add_page()
        pdf.set_font("Helvetica", size=14)
        pdf.cell(200, 10, txt="AI-Generated Illustration", ln=True, align='C')
        pdf.image(image_path, x=10, y=30, w=pdf.w - 20)

    # Speaker notes
    pdf.add_page()
    pdf.set_font("Helvetica", size=14)
    pdf.cell(200, 10, txt="Speaker Notes", ln=True, align='C')
    pdf.set_font("Helvetica", size=11)
    pdf.multi_cell(0, 10, notes)

    pdf.output(filename)
