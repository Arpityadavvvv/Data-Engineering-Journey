### : Data Ingestion for Logs into S3 raw folder

import os                                    # os for intract with system 
import boto3                                 # boto3 for intract with aws  
from datetime import datetime, timedelta     # for all time related things 

# ---------- CONFIG ----------
LOGS_FOLDER = "day-wise-logs-data/"           # ye file path
DATE_TRACKER_FILE = "log_date_tracker.txt"    

S3_BUCKET = "careplus-deproject" # this should match the exact bucket name you have setup in AWS S2
S3_PREFIX = "support-logs/raw/"  # this is inside bucket support-logs and inside it is raw 

from dotenv import load_dotenv   # load from env
load_dotenv()
os.getenv("REGION")


# AWS se Related all information hai yeh 
AWS_CONFIG = {
    "aws_access_key_id": os.getenv("AWS_ACCESS_KEY"),
    "aws_secret_access_key": os.getenv("SECRET_KEY"),
    "region_name": os.getenv("REGION")
}


# ---------- UTILITY FUNCTIONS ----------

# function for reading the last date 
def read_last_date(file_path):
    if os.path.exists(file_path):          # files exist or not if true then 
        with open(file_path, 'r') as f:    # open file and read it as f
            return f.read().strip()        # read and strip it 
    return "2025-06-30"                    # if not exist (then start from this date)


# function for updating the last date
def update_last_date(file_path, new_date): # get the new date 
    with open(file_path, 'w') as f:        # then write it in path  
        f.write(new_date)
        

# function for get_next date 
def get_next_date(last_date_str):                              
    last_date = datetime.strptime(last_date_str, "%Y-%m-%d")     # getting lastdate in format 
    next_date = last_date + timedelta(days=1)                    # getting the nextdate in format 
    return next_date.strftime("%Y-%m-%d")                        # convert nextdate from str to time in format 


# funcition for uploading file in s3 
def upload_log_file_to_s3(file_path, bucket, key):       # parameters are file_path,buxcket s3 and object key (which means exact location)
    s3 = boto3.client('s3', **AWS_CONFIG)                #  making instance of S3 
    with open(file_path, 'r', encoding='utf-8') as f:    #  read the file as f 
        content = f.read()                               #  content = reading all from file 
    s3.put_object(Bucket=bucket, Key=key, Body=content)  #  using putobject by giving parameter like bucket name , object key  and body 
    print(f"✅ Uploaded log file to s3://{bucket}/{key}")

# ---------- MAIN INGESTION LOGIC ----------
def run_log_ingestion():                             
    last_date = read_last_date(DATE_TRACKER_FILE)        # reading last with the help of function 
    next_date = get_next_date(last_date)                 # reading next date by calling function
    print(last_date, next_date)                       

    file_name = f"support_logs_{next_date}.log"      
    log_file_full_path = os.path.join(LOGS_FOLDER, file_name)    # full new path after joining  (day-wise-logs-data/support_logs_2025-07-11.log)
    print(log_file_full_path)
    

    s3_key = f"{S3_PREFIX}support_logs_{next_date}.log"
    upload_log_file_to_s3(log_file_full_path, S3_BUCKET, s3_key)   # calling the s3 uploading the function 
    update_last_date(DATE_TRACKER_FILE, next_date)
    print(f"📅 Updated tracker to {next_date}") 


# ---------- RUN ----------
if __name__ == "__main__":
    run_log_ingestion()                # Python sets its __name__ variable to "__main__" and calls run_log_ingestion().


## Ticket ingestion file is almost same as this 
