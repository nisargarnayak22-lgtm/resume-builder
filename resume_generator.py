from reportlab.pdfgen import canvas

def create_resume(name, email, phone, address, education, skills, projects, experience):

    pdf = canvas.Canvas("generated_resume.pdf")

    y = 800

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(50, y, name)

    y -= 30
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, f"Email: {email}")

    y -= 20
    pdf.drawString(50, y, f"Phone: {phone}")

    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Address")

    y -= 20
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, address)

    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Education")

    y -= 20
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, education)

    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Skills")

    y -= 20
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, skills)

    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Projects")

    y -= 20
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, projects)

    y -= 40
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(50, y, "Experience")

    y -= 20
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, y, experience)

    pdf.save()