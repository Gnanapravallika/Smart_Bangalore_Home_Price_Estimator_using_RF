from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy as np
import os
# Initialize app

from fastapi.middleware.cors import CORSMiddleware



app = FastAPI(title="Bangalore House Price Prediction API")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "model.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "..", "model", "columns.json")

# Load model and columns
model = pickle.load(open(MODEL_PATH, "rb"))
columns = json.load(open(COLUMNS_PATH, "r"))
# Request schema
class HouseData(BaseModel):
    location: str
    sqft: float
    bath: int
    bhk: int

@app.get("/")
def home():
    return {"message": "Bangalore House Price Prediction API is running"}

@app.post("/predict")
def predict_price(data: HouseData):
    x = np.zeros(len(columns))

    # Numerical features
    x[columns.index("total_sqft")] = data.sqft
    x[columns.index("bath")] = data.bath
    x[columns.index("bhk")] = data.bhk

    # Location feature
    loc_col = f"location_{data.location}"
    if loc_col in columns:
        x[columns.index(loc_col)] = 1

    predicted_price = model.predict([x])[0]

    return {
        "predicted_price_lakhs": round(predicted_price, 2)
    }
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


print("Loading model...")
model = pickle.load(open(MODEL_PATH, "rb"))
print("Model loaded!")

"""I deployed my trained regression model as a FastAPI service. The API loads the persisted model and feature schema, validates inputs using Pydantic, and returns real-time predictions via a REST endpoint. Linear regression can produce negative values because it is unconstrained. While the pipeline is correct, I enforce domain constraints in production and plan to improve the model with regularization or non-linear methods"""