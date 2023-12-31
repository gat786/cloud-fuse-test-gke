import gcs_test.setup as setup
import gcs_test.exports as exports
import os
from datetime import datetime

import logging

logger = logging.getLogger(__name__)


def main():
  logger.info("Starting File Read and Write Scripts")
  
  logger.info("Writing File")
  write_file(exports.action_directory)
  logger.info("Completed Writing File")
  
  logger.info("-" * 25)
  
  logger.info("Reading Files")
  read_files(exports.action_directory)
  logger.info("Completed Reading Files")
  

def create_if_not_exists(dir_to_create: str):
  if not os.path.exists(dir_to_create):
    os.makedirs(dir_to_create)
    logger.info(f"Created directory {dir_to_create}")
  else:
    logger.info(f"Directory {dir_to_create} already exists")

def read_files(dir_to_read: str):
  create_if_not_exists(dir_to_read)
  
  try:
    files = os.listdir(dir_to_read)
    for file in files:  
      logging.info(file)
  except Exception as e:
    logger.error(e)
    logger.error(f"Unable to read files in {dir_to_read}")
    raise e
    
def write_file(dir_to_write: str):
  create_if_not_exists(dir_to_write)
  
  now = datetime.now()
  
  try:
    file_name = now.strftime("%Y%m%d+%H%M%S")
    file_path = f"{dir_to_write}/{file_name}.txt"
    with open(file_path, "w") as f:
      f.write(f"Hello, World! at {file_name}")
    
    logger.info(f"Successfully wrote file to {file_path}")
  except Exception as e:
    logger.error(e)
    logger.error(f"Unable to write file to {dir_to_write}")
    raise e
