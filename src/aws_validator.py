import boto3

# Replace these with your AWS credentials
aws_access_key_id = 'your_creds'
aws_secret_access_key = 'your_creds'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# Test AWS connection by listing S3 buckets
try:
    response = s3.list_buckets()
    print("Successfully connected to AWS. Your buckets:")
    for bucket in response['Buckets']:
        print(bucket['Name'])
except Exception as e:
    print(f"Failed to connect to AWS: {e}")
