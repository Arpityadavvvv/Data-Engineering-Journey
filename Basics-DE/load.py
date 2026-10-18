# addding the proccesed data into amazon resdhift by creting schema by query and then copying data into it 
# Redshift design
/* CREATING THE TABLE SCHEMA  */
CREATE TABLE public.support_tickets(
ticket_id       VARCHAR(100),
created_at      TIMESTAMP,
resolved_at     TIMESTAMP,
agent          VARCHAR(100),
priority       VARCHAR(100),
num_interactions BIGINT,
issue_category VARCHAR(100),
channel        VARCHAR(100),
status         VARCHAR(500)
);

/* adding data to that schema from s3 source proccesed */
copy public.support_tickets
from 's3://careplus-deproject/support-tickets/processed/'
IAM_ROLE 'arn:aws:iam::428085218544:role/service-role/AmazonRedshift-CommandsAccessRole-20261015T163028'
FORMAT AS PARQUET
REGION 'eu-north-1';
# similary you can do for logs too

# lambda function for this

import psycopg2
# Redshift Serverless configuration
REDSHIFT_HOST = 'default-workgroup.428085218544.us-east-1.redshift-serverless.amazonaws.com'
REDSHIFT_PORT = '5439'
REDSHIFT_DATABASE = 'careplus_db'  # Replace with your Redshift database name
REDSHIFT_USER = 'admin'  # Replace with your Redshift username
REDSHIFT_PASSWORD = 'Arpit#2002'  # Replace with your Redshift password
REDSHIFT_TABLE = 'public.support_tickets'  # Replace with your table name
IAM_ROLE = 'arn:aws:iam::428085218544:role/service-role/AmazonRedshift-CommandsAccessRole-20261015T163028'

def lambda_handler(event, context):
    # 1: read data from the bucket
    # Get bucket and object key from the S3 event trigger
    record = event['Records'][0]
    bucket_name = record['s3']['bucket']['name']
    input_key = record['s3']['object']['key']

    print(f"📥 Triggered by: s3://{bucket_name}/{input_key}")

    s3_input_path = f's3://{bucket_name}/{input_key}'

    # Connect to Redshift Serverless using psycopg2
    conn = psycopg2.connect(
            host=REDSHIFT_HOST,
            port=REDSHIFT_PORT,
            dbname=REDSHIFT_DATABASE,
            user=REDSHIFT_USER,
            password=REDSHIFT_PASSWORD
    )

    # COPY SQL query to load data from S3 into the Redshift table
    copy_sql = f"""
        COPY {REDSHIFT_TABLE}
        FROM '{s3_input_path}'
        IAM_ROLE '{IAM_ROLE}'
        FORMAT AS PARQUET
        REGION 'eu-north-1';
        """

    # Execute the query
    cursor = conn.cursor()
    cursor.execute(copy_sql)

    # Commit the changes (important for COPY operations)
    conn.commit()

    # Log success
    print(f"Data successfully copied from {s3_input_path} to {REDSHIFT_TABLE}")


    # Close the cursor and the connection
    cursor.close()
    conn.close()

   # after again adding the trigger in s3 it will automaticlaly fires when someone upload raw file into s3 

    
    
