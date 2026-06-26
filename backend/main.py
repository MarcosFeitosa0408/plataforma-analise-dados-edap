from fastapi import FastAPI, UploadFile, File
import pandas as pd
import os

from backend.etl.pipeline import ETLPipeline

app = FastAPI(title="EDAP - API de Dados")

etl = ETLPipeline()


@app.get("/")
def home():
    return {"status": "EDAP ONLINE"}


@app.post("/etl/upload")
async def upload_file(file: UploadFile = File(...)):

    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    result = etl.run(file_path)

    return {
        "status": "success",
        "rows": len(result),
        "columns": list(result.columns),
        "preview": result.head(5).to_dict()
    }
