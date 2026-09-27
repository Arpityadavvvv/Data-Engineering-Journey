import os
import pandas as pd
import boto3                          # boto3 allows Python to communicate with AWS services.
from io import StringIO                # This lets us create a file-like object in memory.
from sqlalchemy import create_engine    # Used to create a connection between Python and MySQL.
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv() #

# ------------------------------------------------------------------------------------------------------------------------

```jsx
db_config = {
"host": "localhost",
"port": "3306",
"user": "root",  # change
"password": "root", # change
"database": "careplus_support_db"
}

S3_BUCKET = "careplus-deproject"
S3_PREFIX = "support-tickets/raw/"

DATE_TRACKER_FILE = "date_tracker.txt"

import os

AWS_CONFIG = {
"aws_access_key_id": os.getenv("AWS_ACCESS_KEY"),
"aws_secret_access_key": os.getenv("SECRET_KEY"),
"region_name": os.getenv("REGION")
}
```

# ------------------------------------------------------------------------------------------------------------------------

'''
"Take the database configuration, build a MySQL connection URL from it,
and create a SQLAlchemy engine so Python can
communicate with the MySQL database."

'''
# Create a connection/engine that Python can use to communicate with MySQL.
def get_engine(config):
return create_engine(f"mysql+pymysql://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}")


Take the CSV text from memory and upload it to this location in S3

def upload_to_s3(df, bucket, key):
csv_buffer = StringIO()
df.to_csv(csv_buffer, index=False)

# Connect to S3
s3 = boto3.client('s3', **AWS_CONFIG)

# AWS, take this CSV data and put it in this S3 bucket at this location.
s3.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())
print(f"✅ Uploaded to s3://{bucket}/{key}")

def read_last_date(file_path):   # file_path is the location/name of the file you want
if os.path.exists(file_path):    # this file only contain date
with open(file_path, 'r') as f:  # Read the date.
return f.read().strip()
return "2025-06-30"  # Starting point before 1st July

# read the date and write 
def update_last_date(file_path, new_date):
with open(file_path, 'w') as f: # Important: write mode will replace the existing content.
f.write(new_date)

'''
date_tracker.txt
↓
2025-07-02
↓

- 1 day
↓
2025-07-03
'''
# Next date to process
def get_next_date(last_date_str):
last_date = datetime.strptime(last_date_str, "%Y-%m-%d")
next_date = last_date + timedelta(days=1)
return next_date.strftime("%Y-%m-%d")

# ---------------------------------------------------------------------------------------------------------------------
# Run the entire ETL ingestion process
def run_ingestion():
engine = get_engine(db_config)                 # Python → MySQL
last_date = read_last_date(DATE_TRACKER_FILE)  # last_date = 2025-07-01
next_date = get_next_date(last_date)           # next_date = 2025-07-02


# Query only that day’s data
query = f"""
    SELECT * FROM support_tickets
    WHERE DATE(created_at) = '{next_date}';
"""

# Give me all support tickets created on July 2, 2025.
df = pd.read_sql(query, engine)
print(df.shape)
print(df.head())

if df.empty: # No data → Don't upload anything
    print(f"⚠️ No data found for {next_date}. Skipping upload.")
    return

# Upload to S3
s3_key = f"{S3_PREFIX}support_tickets_{next_date}.csv" # support-tickets/raw/support_tickets_2025-07-02.csv
upload_to_s3(df, S3_BUCKET, s3_key)

# Update date tracker
update_last_date(DATE_TRACKER_FILE, next_date)
print(f"📅 Updated tracker to {next_date}")

# Run

if **name** == "**main**":
run_ingestion()
