from src.exception_handler import CustomException
from src.logger import logging
import os,sys
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
import pandas as pd
import numpy as np
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_object_path: str = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def _get_preprocessor_object(self):
        try:
            numerical_columns=["Age","Tenure","Usage Frequency", "Support Calls","Payment Delay","Total Spend","Last Interaction"]
            categorical_columns=["Gender","Subscription Type","Contract Length"]
            numerical_transformer=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='mean')),
                    ('scaler',StandardScaler()),
                ]
            )
            categorical_transformer=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('encoder',OneHotEncoder(sparse_output=False)),
                ]
            )

            preprocessor=ColumnTransformer(
                transformers=[
                    ('numerical_trans',numerical_transformer,numerical_columns),
                    ('categorical_trans',categorical_transformer,categorical_columns),
                ]
            )
            # save the preprocessor

            # return the preprocessor
            

        except Exception as e:
            raise CustomException(e,sys)
        return preprocessor

    def initiate_data_transformation(self,validated_train_data_path,validated_test_data_path):
        try:
            train_data=pd.read_csv(validated_train_data_path)
            test_data=pd.read_csv(validated_test_data_path)
            target_column="Churn"
            train_data[target_column]=train_data[target_column].astype("int")
            test_data[target_column]=test_data[target_column].astype("int")
            X_train=train_data.drop(columns=[target_column],axis=1)
            y_train=train_data[target_column]
            X_test=test_data.drop(columns=[target_column])
            y_test=test_data[target_column]
            preprocessor_obj=self._get_preprocessor_object()
            train_input_arr=preprocessor_obj.fit_transform(X_train)
            test_input_arr=preprocessor_obj.transform(X_test)

            logging.info("Saving the preprocessor object")
            save_object(self.data_transformation_config.preprocessor_object_path,
                        preprocessor_obj)

            return (
                train_input_arr,y_train.values,test_input_arr,y_test.values
            )
        except Exception as e:
            raise CustomException(e,sys)
