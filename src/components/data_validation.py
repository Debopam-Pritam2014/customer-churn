from src.exception_handler import CustomException
from src.logger import logging
from dataclasses import dataclass
import os,sys
import pandas as pd

@dataclass
class DataValidationConfig:
    validated_train_data_path : str= os.path.join('data_validation','data_train.csv')
    validated_test_data_path : str= os.path.join('data_validation','data_test.csv')

class DataValidation:
    def __init__(self):
        self.data_validation_config=DataValidationConfig()
    
    def initiate_data_validation(self,train_data_path,test_data_path):
        logging.info("Data Validation Initiated.")
        try:
            train_data=pd.read_csv(train_data_path)
            test_data=pd.read_csv(test_data_path)
            os.makedirs(os.path.dirname(self.data_validation_config.validated_train_data_path),exist_ok=True)
            expected_types={
                "Surname":pd.api.types.is_object_dtype,
                "CreditScore":pd.api.types.is_numeric_dtype,
                "Geography":pd.api.types.is_object_dtype,
                "Gender":pd.api.types.is_object_dtype,
                "Age":pd.api.types.is_numeric_dtype,
                "Tenure":pd.api.types.is_numeric_dtype,
                "Balance":pd.api.types.is_numeric_dtype,
                "NumOfProducts":pd.api.types.is_numeric_dtype,
                "HasCrCard":pd.api.types.is_numeric_dtype,
                "IsActiveMember":pd.api.types.is_numeric_dtype,
                "EstimatedSalary":pd.api.types.is_numeric_dtype,
                "Exited":pd.api.types.is_numeric_dtype,
            }
            for column,dtypes in expected_types.items():
                if not dtypes(train_data[column]):
                    raise CustomException(e,sys)
                if not dtypes(test_data[column]):
                    raise CustomException(e,sys)
            
            logging.info("Data Validation Successful.")
            # dropping the null values
            train_data.dropna(inplace=True)
            train_data.to_csv(self.data_validation_config.validated_train_data_path,index=False,header=True)
            test_data.to_csv(self.data_validation_config.validated_test_data_path,index=False,header=True)
            logging.info("Validated Data Saved Successfully.")
            return(
                self.data_validation_config.validated_train_data_path,
                self.data_validation_config.validated_test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        

        