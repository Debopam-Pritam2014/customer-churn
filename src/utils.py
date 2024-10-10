from src.exception_handler import CustomException
from src.logger import logging
import os,sys
import dill
import numpy as np
import pandas as pd
from sklearn.metrics import precision_score,recall_score,accuracy_score,f1_score

def save_object(filepath,obj):
    try:
        file_dir=os.path.dirname(filepath)
        os.makedirs(file_dir,exist_ok=True)
        with open(filepath ,"wb") as file:
            dill.dump(obj=obj,file=file)
        logging.info(f"{filepath} object saved successfully.")
    except Exception as e:
        raise CustomException(e,sys)
    
def get_classification_report(models,X_train,y_train,X_test,y_test):
    classification_report={}
    try:
        
        for model_name,model in models.items():
            model.fit(X_train,y_train)
            y_pred=model.predict(X_test)
            accuracy=accuracy_score(y_pred,y_test)
            precision=precision_score(y_pred,y_test)
            recall=recall_score(y_pred,y_test)
            f_score=f1_score(y_pred,y_test)
            classification_report[model_name]={
                "accuracy":accuracy,
                "precision":precision,
                "recall":recall,
                "f-score":f_score
            }
        logging.info("Model Training Successful.")
        return classification_report

    except Exception as e:
        raise CustomException(e,sys)
    
            
        