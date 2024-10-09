from src.exception_handler import CustomException
from src.logger import logging
import os,sys
import dill

def save_object(filepath,obj):
    try:
        file_dir=os.path.dirname(filepath)
        os.makedirs(file_dir,exist_ok=True)
        with open(filepath ,"wb") as file:
            dill.dump(obj=obj,file=file)
        logging.info(f"{filepath} object saved successfully.")
    except Exception as e:
        raise CustomException(e,sys)
    
            
        