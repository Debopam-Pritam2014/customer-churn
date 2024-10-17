from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.pipeline.testing_pipeline import PredictionPipeline


application=Flask(__name__)

app=application

# Create route for home

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def predict_data():
    if request.method=='GET':
        return render_template("home.html")
    else:
        prediction_obj=PredictionPipeline(
            Age=request.form.get("age"),
            Gender=request.form.get("gender"),
            Tenure=request.form.get("tenure"),
            CreditScore=request.form.get("CreditScore"),
            IsActiveMember=request.form.get("IsActiveMember"),
            Geography=request.form.get("Geography"),
            NumOfProducts=request.form.get("NumOfProducts"),
        )
        prediction=prediction_obj.predict()
        return render_template("home.html",results=prediction[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
        



