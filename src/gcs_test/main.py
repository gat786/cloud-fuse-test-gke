import os
from datetime import datetime

def main():
  print("Hello, World!")

def read_files(dir_to_read: str):
  files = os.listdir(dir_to_read)
  for file in files:  
    print(file)
    
def write_file(dir_to_write: str):
  now = datetime.now()
  
  file_name = now.strftime("%Y%m%d+%H%M%S")
  with open(f"{dir_to_write}/{file_name}.txt", "w") as f:
    f.write(f"Hello, World! at {file_name}")
  
