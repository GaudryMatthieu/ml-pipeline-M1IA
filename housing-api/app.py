from fastapi import FastAPI
import joblib
import pandas as pd
from schema import HousingFeatures, PredictionResponse

app = FastAPI()

model = joblib.load('model.joblib')

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "L'API est opérationnelle"}

@app.post("/predict", response_model=PredictionResponse)
def predict(features: HousingFeatures):
    input_data = pd.DataFrame([features.dict()])
    
    prediction = model.predict(input_data)
    
    return PredictionResponse(predicted_house_value=float(prediction[0]))