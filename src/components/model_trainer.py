import os,sys
from src.exception_handler import CustomException
from src.logger import logging
from dataclasses import dataclass
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier,AdaBoostClassifier,GradientBoostingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_score,recall_score,accuracy_score
from src.utils import get_classification_report,save_object

@dataclass
class ModelTrainerConfig:
    model_trainer_config: str = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    def __init__(self) :
        self.model_config=ModelTrainerConfig()
    
    def initiate_model_training(self,X_train,y_train,X_test,y_test):
        logging.info("Model Training Initiated")
        try:
            models={
                "Logistic Regression":LogisticRegression(),
                "Decision Tree":DecisionTreeClassifier(),
                "Random Forest":RandomForestClassifier(),
                "Extra Tree":ExtraTreesClassifier(),
                "Ada Boost":AdaBoostClassifier(),
                "Gradient Boost":GradientBoostingClassifier(),
                "K neighbors":KNeighborsClassifier()
            }
            classification_report=get_classification_report(models,X_train,y_train,X_test,y_test)
            # Find best model based on F1-score
            logging.info(f"Classification report: {classification_report}")
            best_model_name = max(classification_report, key=lambda x: classification_report[x]['accuracy'])
            best_model_report = classification_report[best_model_name]
            best_model=models[best_model_name].fit(X_train,y_train)
            print(best_model_name,best_model_report)

            logging.info("Saving the best model")
            save_object(
                self.model_config.model_trainer_config,
                best_model
            )
            return  best_model

        except Exception as e:
            raise CustomException(e,sys)