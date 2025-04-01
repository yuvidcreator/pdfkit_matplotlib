from fastapi import FastAPI, UploadFile, File, BackgroundTasks
import os
from app.pdf_generator import generate_pdf
from app.excel_processor import process_excel
from app.chart_generator import generate_doughnut_chart
from app.pdf_merger import merge_pdfs

app = FastAPI()

UPLOAD_DIR = "uploads/"
STATIC_DIR = "static/"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)




async def handle_excel_file(file_path: str, output_pdf: str):
    """Process Excel file and generate final PDF"""
    data = process_excel(file_path)
    
    # Generate doughnut chart
    chart_path = generate_doughnut_chart(data, f"{UPLOAD_DIR}chart.webp")
    
    temp_pdf = f"{UPLOAD_DIR}temp_report.pdf"
    
    generate_pdf(data, chart_path, temp_pdf)  # Generate report with chart
    
    # Merge with static pages
    static_pdf = f"{STATIC_DIR}static_pages.pdf"
    if not os.path.exists(static_pdf):
        raise FileNotFoundError(f"Static PDF not found: {static_pdf}")
    merge_pdfs([static_pdf, temp_pdf], output_pdf)



@app.post("/upload-excel/")
async def upload_excel(file: UploadFile = File(...), background_tasks: BackgroundTasks = BackgroundTasks()):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    output_pdf = f"{UPLOAD_DIR}final_report.pdf"
    background_tasks.add_task(handle_excel_file, file_path, output_pdf)
    
    return {"status": "Processing", "file_path": output_pdf}