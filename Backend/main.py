from classification import *

from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    # Ubuntu: /mnt/c/Users/maxim/OneDrive/Desktop/MP/Projects/#1 - Image Classification project/Images for testing/Frog #2 - test image (J).jpg
    filepath: str

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to the Image Classifier!"

@app.post("/classify")
def classify(input:Input):
    return {"prediction": classification_process(input.filepath)}