import boto3
import os
from dotenv import load_dotenv

load_dotenv(".env")

# Configuration AWS
s3 = boto3.client(
    's3',
   aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='eu-north-1'
)

def get_file_from_s3(bucket_name, file_key):
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    return response['Body'].read().decode('utf-16')
