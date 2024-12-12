from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf():
    c = canvas.Canvas("bank_details.pdf", pagesize=letter)
    width, height = letter

    c.drawString(100, height - 100, "Your Name: Adarsh")
    c.drawString(100, height - 130, "Bank Name: XYZ Bank")
    c.drawString(100, height - 160, "Account Number: 123456789")
    c.drawString(100, height - 190, "Account Currency: USD")
    c.drawString(100, height - 220, "Time Frame Requested: Jan 2023 - Dec 2023")

    c.save()

create_pdf()

