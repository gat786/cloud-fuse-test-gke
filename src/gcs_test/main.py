import gcs_test.setup as setup
import gcs_test.exports as exports
import os
from datetime import datetime

import logging

logger = logging.getLogger(__name__)


def main():
  logger.info("Starting File Read and Write Scripts")
  
  logger.info("Reading Files")
  read_files(exports.action_directory)
  logger.info("Completed Reading Files")
  
  logger.info("-" * 25)
  
  logger.info("Writing File")
  write_file(exports.action_directory)
  logger.info("Completed Writing File")

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
      print(file)
  except Exception as e:
    logger.error(e)
    logger.error(f"Unable to read files in {dir_to_read}")
    raise e
    
def write_file(dir_to_write: str):
  create_if_not_exists(dir_to_write)
  
  now = datetime.now()
  
  try:
    file_name = now.strftime("%Y%m%d+%H%M%S")
    with open(f"{dir_to_write}/{file_name}.txt", "w") as f:
      f.write(f"Hello, World! at {file_name}")
  except Exception as e:
    logger.error(e)
    logger.error(f"Unable to write file to {dir_to_write}")
    raise e
