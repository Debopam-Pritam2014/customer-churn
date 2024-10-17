import os,sys
from src.exception_handler import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion,DataIngestionConfig
from src.components.data_validation import DataValidation,DataValidationConfig
from src.components.data_transformation import DataTransformation,DataTransformationConfig
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig

class TrainingPipeline:
    def __init__(self) :
        pass

    def initiate_training_pipeline(self):
        logging.info("Training Pipeline Invoked.")
        try:
            print("Data Ingestion Started...")
            data_ingesion=DataIngestion()
            train_data_path,test_data_path=data_ingesion.initiate_data_ingestion()
            print("Data Ingestion Done.")

            print("Data Validation Started...")
            data_validation=DataValidation()
            validated_train_data_path,validated_test_data_path=data_validation.initiate_data_validation(train_data_path=train_data_path,test_data_path=test_data_path)
            print("Data Validation Done.")

            print("Data Transformation Started...")
            data_transform=DataTransformation()
            X_train,y_train,X_test,y_test=data_transform.initiate_data_transformation(validated_train_data_path=validated_train_data_path,validated_test_data_path=validated_test_data_path)
            print("Data Transformation Done.")

            print("Model Training Started...")
            trainer=ModelTrainer()
            best_model=trainer.initiate_model_training(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test)

            logging.info("Training Pipeline Successfully Done.")
            print("Model Training Done.")
            return best_model
            
        except Exception as e:
            raise CustomException(e,sys)

