# Logging is basically to store the logs, it will store the customexecption also

import os
import logging
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# Whenever we want to override the functionality we can use BasicConfig

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d - %(name)s - %(levelname)s - %(message)s ",
    level=logging.INFO, #for information level logging only we use this
    
)