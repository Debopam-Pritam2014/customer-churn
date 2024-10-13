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
            Usage_Frequency=request.form.get("usage_frequency"),
            Support_Calls=request.form.get("support_calls"),
            Payment_Delay=request.form.get("payment_delay"),
            Subscription_Type=request.form.get("subscription_type"),
            Contract_Length=request.form.get("contract_length"),
            Total_Spend=request.form.get("total_spend"),
            Last_Interaction=request.form.get("last_interaction"),
        )
        prediction=prediction_obj.predict()
        return render_template("home.html",results=prediction[0])
    
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)
        



