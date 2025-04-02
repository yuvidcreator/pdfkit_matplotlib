import os
from fastapi import FastAPI
from app.routes.pdf_route import route as pdf_routes

app = FastAPI()

UPLOAD_DIR = "uploads/"
STATIC_DIR = "static/"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)



app.include_router(pdf_routes)