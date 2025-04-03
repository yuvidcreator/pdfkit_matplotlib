import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes.pdf_route import route as pdf_routes
from app.utils.custom_static_files import CustomStaticFiles

app = FastAPI()

UPLOAD_DIR = "uploads/"
STATIC_DIR = "static/"
# IMAGES_DIR = f"{STATIC_DIR}images/"
IMAGES_DIR = "images/"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(STATIC_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
# app.mount("/images", StaticFiles(directory="images"), name="images")
# app.mount("/images", CustomStaticFiles(directory="images"), name="images")

app.include_router(pdf_routes)