# transforming file from s3 raw and saving it into s3 processed in parquet file 


# importing all modules 
import json
import boto3
import base64
import re                    # for Regex
import pandas as pd             
import io                    # Memory mein file-like buffer banane ke liye.
import pyarrow as pa         # Pandas DataFrame ko Parquet format mein convert karne ke liye
import pyarrow.parquet as pq

# reading log file from s3 
def read_log_from_s3 (bucket,key):
    s3 = boto3.client('s3')
    response = s3.get_object(Bucket=bucket, Key=key)
    log_data = response['Body'].read().decode('utf-8')
    return log_data

# save this parquet format file in S3 
def save_parquet_to_s3(df,bucket,key):
   
    # convert dataframe to parquet 
    table = pa.Table.from_pandas(df,preserve_index=False) # DataFrame → PyArrow Table
    parquet_buffer = io.BytesIO()                         # making empty buffern in Memory 
    pq.write_table(table, parquet_buffer)                 # PyArrow Table converted in parquet and saved into buffer

    # upload to s3 
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=key, Body=parquet_buffer.getvalue())
    print(f"parquet saved to s3")

# this is lambda function 
def lambda_handler(event,context):
    # get bucket and key from s3 event trigger 
    record = event['Records'][0]
    bucket_name = record['s3']['bucket']['name']
    # file in normal from 
    input_key = record['s3']['object']['key']  #where we are taking it 
      

    # step -02 read log data 
    # Step 2: Read log data
    raw_logs = read_log_from_s3(bucket_name, input_key)
    lines = [ line.strip() for line in raw_logs.split('---') if line.strip()]
    lines[1]

    log_pattern = re.compile(
        r'(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?P<log_level>[A-Za-z0-9_]+)\] '
        r'(?P<component>[^\s]+) - TicketID=(?P<ticket_id>[^\s]+) SessionID=(?P<session_id>[^\s]+)\s*'
        r'IP=(?P<ip>.*?) \| ResponseTime=(?P<response_time>-?\d+)ms \| CPU=(?P<cpu>[\d.]+)% \| EventType=(?P<event_type>.*?) \| Error=(?P<error>\w+)\s*'
        r'UserAgent="(?P<user_agent>.*?)"\s*'
        r'Message="(?P<message>.*?)"\s*'
        r'Debug="(?P<debug>.*?)"\s*'
        r'TraceID=(?P<trace_id>.*)'
    )

    parsed_lines = []
    for line in lines:
           match = log_pattern.search(line)
           if match:
              parsed_lines.append(match.groupdict())
    #parsed_lines[0]

    # creating Dataframe 
    df = pd.DataFrame(parsed_lines)
   

    # DATA CLEANING 
    df = df.drop('trace_id',axis=1)  # 01   we dont need trace_id 
    df = df.astype({'response_time': 'int64', 'cpu': 'float'})  # these all will be specified
    #df.info()

    df['error'] = df['error'].str.lower().map({'true':True,'false':False})
    df['timestamp'] = pd.to_datetime(df['timestamp'] , format='%Y-%m-%d %H:%M:%S', errors='coerce').astype('datetime64[ms]')

    # here you see INFO AND INF0 both are diffrent 
    # fix_log_level = {'INF0':'INFO', 'DEBG':'DEBUG','warnING':'WARNING','ERROR':'ERROR'}
    # df['log_level'] = df['log_level'].replace(fix_log_level)
    # df.log_level.value_counts()

    # now we will save the data in parquet format 
    output_file_name = input_key.split('/')[2].replace('.log', '.parquet') # making file in parquet form 
    output_key = f'support-logs/processed/{output_file_name}' # destination 
    save_parquet_to_s3(df, bucket_name, output_key)

# after this add trigger in s3 bucket on a put event for automating this 


