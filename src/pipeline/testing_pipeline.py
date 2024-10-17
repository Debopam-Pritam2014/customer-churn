import sys
from src.exception_handler import CustomException
from src.logger import logging
from src.utils import load_object
import numpy as np
import pandas as pd



class PredictionPipeline:
    def __init__(self,Age,Gender:str,Tenure,CreditScore,
                 IsActiveMember,Geography,NumOfProducts) :
        # all the custom values
        self.Age=Age
        self.Gender=Gender
        self.Tenure=Tenure
        self.CreditScore=CreditScore
        self.IsActiveMember=IsActiveMember
        self.Geography=Geography
        self.NumOfProducts=NumOfProducts

    def _get_dataframe(self):
        """
        Creates a DataFrame from the input data.
        """
        try:
            data_dict = {
                "Age": [self.Age],
                "Gender": [self.Gender],
                "Tenure": [self.Tenure],
                "CreditScore": [self.CreditScore],
                "IsActiveMember": [self.IsActiveMember],
                "Geography": [self.Geography],
                "NumOfProducts": [self.NumOfProducts],
            }
            return pd.DataFrame(data_dict)
        except Exception as e:
            raise CustomException(e,sys)
    
    def predict(self):
        logging.info("Predict method invoked.")
        """
        Makes predictions using the trained model.
        """
        try:
            logging.info("Loading the model.")
            model=load_object("artifacts\model.pkl")

            logging.info("Loading the Preprocessor.")
            preprocessor=load_object("artifacts\preprocessor.pkl")

            data=self._get_dataframe()
            prediction_data=preprocessor.transform(data)
            logging.info("Processed the data.")
            result=model.predict(prediction_data)
            return result

        except Exception as e:
            raise CustomException(e,sys)

