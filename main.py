from src.pipeline.training_pipeline import TrainingPipeline
import sys
from src.exception_handler import CustomException

def invoke_training_pipeline():
    try:
        training_pipeline=TrainingPipeline()
        training_pipeline.initiate_training_pipeline()
    
    except Exception as e:
        raise  CustomException(e,sys)
def invoke_testing_pipeline():
    try:
        pass
        # testing_pipeline=TrainingPipeline()
        # testing_pipeline.initiate_training_pipeline()
    
    except Exception as e:
        raise  CustomException(e,sys)

if __name__=="__main__":
    invoke_training_pipeline()