import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # make log of respective file name with .log extension
log_path = os.path.join(os.getcwd(),"logs") #it will creates the log file on current working dir

# to execute the code
os.makedirs(log_path,exist_ok=True)

# complete path
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE) 

# setting the content of log file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)