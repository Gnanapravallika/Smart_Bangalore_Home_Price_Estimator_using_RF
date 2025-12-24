# Smart_Bangalore_Home_Price_Estimator_using_RF

## Project Overview

This project is an end-to-end machine learning application that predicts house prices in Bangalore based on property features such as location, total square feet, number of bedrooms (BHK), and bathrooms.

The goal of this project is not just prediction accuracy, but to demonstrate real-world ML system design, including:

Data preprocessing

Model selection

Backend API development

Frontend integration

End-to-end testing

## Problem Statement

Real estate pricing depends on multiple interacting factors such as location, size, and amenities.
This project aims to build a machine learning system that can estimate house prices using historical Bangalore housing data and expose the model via a REST API for real-time predictions.

## Solution Approach
## 1. Data Processing

Cleaned real-world housing data with missing values and inconsistent formats.

Converted categorical and textual fields (e.g., location, size) into numerical features.

## Performed feature engineering such as:

Extracting BHK

Calculating price per square foot

Removed outliers using domain-based and statistical methods.

## 2. Model Development

Initially experimented with linear models.

Switched to Random Forest Regressor to:

Capture non-linear relationships

Avoid invalid negative price predictions

Improve stability and realism of predictions

## 3. Backend (FastAPI)

Built a FastAPI backend to serve the trained ML model.

Implemented a /predict endpoint that accepts JSON input and returns predicted house prices.

Added CORS support for frontend-backend communication.

## 4. Frontend

Designed a simple, clean browser-based UI using HTML, CSS, and JavaScript.

Integrated frontend with FastAPI using REST API calls.

Added input validation, loading states, and user-friendly error handling.

# System Architecture
User (Browser)
     |
     v
Frontend (HTML + CSS + JS)
     |
     v
FastAPI Backend (REST API)
     |
     v
Machine Learning Model (Random Forest)
     |
     v
Predicted House Price

## Tech Stack

## Machine Learning

Python

Pandas, NumPy

Scikit-learn (Random Forest Regressor)

## Backend

FastAPI

Uvicorn

## Frontend

HTML

CSS

JavaScript (Fetch API)

## How to Run the Project Locally
## 1.Clone the Repository
git clone https://github.com/your-username/Smart_Bangalore_Home_Price_Estimator_using_RF.git
cd Smart_Bangalore_Home_Price_Estimator_using_RF

## 2. Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate

## 3. Install Dependencies
pip install -r requirements.txt

## 4. Run Backend (FastAPI)
uvicorn backend.main:app


Backend will be available at:

http://127.0.0.1:8000

## 5.Run Frontend
cd frontend
python -m http.server 5500


Open in browser:

http://127.0.0.1:5500

## Example API Input
{
  "location": "Whitefield",
  "sqft": 1200,
  "bhk": 2,
  "bath": 2
}

Example Output
{
  "predicted_price_lakhs": 72.5
}

## Limitations

Predictions are estimates based on historical data and may not reflect current market prices.

Model performance depends on the quality and coverage of training data.

Location names not seen during training are handled using fallback logic.

## Future Improvements

Improve model performance with hyperparameter tuning

Add explainability (feature importance visualization)

Deploy backend and frontend on cloud platforms

Enhance UI with charts and location-based insights

## Key Learnings

Importance of data cleaning and feature engineering in real-world datasets

Model choice impacts both prediction quality and business validity

Building ML systems requires integration beyond notebooks

Frontend-backend communication and CORS handling are critical in production systems

Author
Gnana Pravallika Perugu
Machine Learning & AI Enthusiast
