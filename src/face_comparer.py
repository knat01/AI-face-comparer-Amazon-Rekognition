import boto3
import botocore

# Initialize the Rekognition client
rekognition_client = boto3.client('rekognition', region_name='us-east-2')  # Change the region as needed

# Specify the S3 bucket name for user-uploaded image and the collection bucket
user_image_bucket = 'your_bucket'
collection_bucket = 'your_bucket'

# Create Rekognition image objects with S3 URLs for the user-uploaded image
user_image_name = 's5.jpg'  # Name of the user's uploaded image
user_image = {'S3Object': {'Bucket': user_image_bucket, 'Name': user_image_name}}

# Set the confidence threshold for face matching
confidence_threshold = 90  # Adjust this value as needed

# List all objects in the collection bucket
collection_objects = boto3.client('s3').list_objects_v2(Bucket=collection_bucket)

# Initialize a list to store results
results = []

# Perform the face comparison with each image in the collection
for collection_object in collection_objects.get('Contents', []):
    target_image = {'S3Object': {'Bucket': collection_bucket, 'Name': collection_object['Key']}}
    try:
        response = rekognition_client.compare_faces(SourceImage=user_image, TargetImage=target_image)
    except botocore.exceptions.ClientError as e:
        print(f"Error comparing faces with {collection_object['Key']}: {e}")
        # Handle the error gracefully
        continue

    if response.get('FaceMatches'):
        for match in response['FaceMatches']:
            confidence = match['Similarity']
            if confidence >= confidence_threshold:
                results.append({
                    'File Name': collection_object['Key'],
                    'Accuracy Score': confidence
                })

# Sort the results by accuracy score
results.sort(key=lambda x: x['Accuracy Score'], reverse=True)

# Display the results
if results:
    for result in results:
        print(f"File Name: {result['File Name']}, Accuracy Score: {result['Accuracy Score']}")
else:
    print("No matching images found.")
