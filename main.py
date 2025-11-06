from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("linear+_regression_model.pkl")
scaler = joblib.load("scaler.pkl")

# Initialize app
app = FastAPI()

# define pydantic model

class PredictionRequest(BaseModel):
    hours_studied: float

# lets create our get endpoint
@app.get("/")
def home():
    return {"message":"Welcome to the AI Engineering Fellows"}



@app.post("/predict")
def predict(request:PredictionRequest):
    hours = request.hours_studied
    data = pd.DataFrame([[hours]], columns = ["Hour_Studied"])
    scaled_data = scaler.transform(data)
    prediction = model.predict(scaled_data)
    return {"predicted_test_score": float[0]}

# LEts try handling  errors
@app.post("/post")
def predict(request:PredictionRequest):
    try:
        hours = request.hours_studied
        data = pd.DataFrame([[hours]], columns = ["Hour_Studied"])
        scaled_data = scaler.transform(data)
        prediction = model.predict(scaled_data)
        return {"predicted_test_score": float[0]}
    except Exception as e:
        return {"error": str(e)}
    
# run app with ---> univcorn main:app --reload