from classification import *

from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    filepath: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Intro": "Welcome to the Image Classifier!"}

@app.post("/classify")
def classify(input:Input):
    return {"prediction": classification_process(input.filepath)}
