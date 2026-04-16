from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


def generar_pdf_informe(stats: dict) -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    elementos = []

    elementos.append(Paragraph("Informe de análisis", styles["Title"]))
    elementos.append(Spacer(1, 20))

    elementos.append(Paragraph(f"Total de registros: {stats['total']}", styles["Normal"]))
    elementos.append(Spacer(1, 10))

    elementos.append(Paragraph(f"Precio medio: {stats['media']:.2f}", styles["Normal"]))
    elementos.append(Spacer(1, 10))

    elementos.append(Paragraph(f"Precio máximo: {stats['max']:.2f}", styles["Normal"]))
    elementos.append(Spacer(1, 10))

    elementos.append(Paragraph(f"Precio mínimo: {stats['min']:.2f}", styles["Normal"]))
    elementos.append(Spacer(1, 10))

    elementos.append(Paragraph(f"Valores nulos detectados: {stats['nulos']}", styles["Normal"]))

    doc.build(elementos)

    pdf = buffer.getvalue()
    buffer.close()

    return pdf