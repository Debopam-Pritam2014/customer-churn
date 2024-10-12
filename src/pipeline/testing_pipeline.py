import sys
from src.exception_handler import CustomException
from src.logger import logging
from src.utils import load_object
import numpy as np
import pandas as pd



class PredictionPipeline:
    def __init__(self,Age,Gender:str,Tenure,Usage_Frequency,
                 Support_Calls,Payment_Delay,Subscription_Type,
                 Contract_Length,Total_Spend,Last_Interaction) :
        # all the custom values
        self.Age=Age
        self.Gender=Gender
        self.Tenure=Tenure
        self.Usage_Frequency=Usage_Frequency
        self.Support_Calls=Support_Calls
        self.Payment_Delay=Payment_Delay
        self.Subscription_Type=Subscription_Type
        self.Contract_Length=Contract_Length
        self.Total_Spend=Total_Spend
        self.Last_Interaction=Last_Interaction

    def _get_dataframe(self):
        """
        Creates a DataFrame from the input data.
        """
        try:
            data_dict = {
                "Age": [self.Age],
                "Gender": [self.Gender],
                "Tenure": [self.Tenure],
                "Usage Frequency": [self.Usage_Frequency],
                "Support Calls": [self.Support_Calls],
                "Payment Delay": [self.Payment_Delay],
                "Subscription Type": [self.Subscription_Type],
                "Contract Length": [self.Contract_Length],
                "Total Spend": [self.Total_Spend],
                "Last Interaction": [self.Last_Interaction]
            }
            return pd.DataFrame(data_dict)
        except Exception as e:
            raise CustomException(e,sys)
    
    def predict(self):
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

