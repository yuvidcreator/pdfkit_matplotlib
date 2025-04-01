import os
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output_file):
    """Merge multiple PDFs into one"""
    merger = PdfMerger()

    for pdf in pdf_list:
        abs_pdf_path = os.path.abspath(pdf)
        if not os.path.exists(abs_pdf_path):
            raise FileNotFoundError(f"Missing PDF file: {abs_pdf_path}")
        merger.append(abs_pdf_path)

    merger.write(output_file)
    merger.close()
