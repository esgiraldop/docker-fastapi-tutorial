import io
from PIL import Image
from typing import Dict, Union
from model import model_pipeline

from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/ask")
def ask(text: str, image: UploadFile) -> Dict[str, str]:
    content = image.file.read()
    image = Image.open(io.BytesIO(content))

    return {"answer": model_pipeline(text, image)}