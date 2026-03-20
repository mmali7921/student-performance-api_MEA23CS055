from fastapi import FastAPI
from .schemas import StudentInput
from .predictor import predict_performance

app = FastAPI(title="Student Performance API")


@app.get("/")
def home():
    return {"message": "API is running"}


@app.post("/predict")
def predict(data: StudentInput):
    result = predict_performance(data)
    return {"prediction": result}