from fastapi import FastAPI, UploadFile, File, Query
from fastapi.middleware.cors import CORSMiddleware
from model_predict import predict_disease
from gemini_utils import explain_disease  
from pydantic import BaseModel
from typing import List
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
def predict(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    label, confidence = predict_disease(file_path)
    os.remove(file_path)

    return {"disease": label, "confidence": confidence}


class DiseaseRequest(BaseModel):
    disease: str

@app.post("/gemini_disease_info")
def gemini_disease_info(data: DiseaseRequest):
    reply = explain_disease(data.disease)
    return {"reply": reply}

