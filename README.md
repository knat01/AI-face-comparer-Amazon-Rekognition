**AI Face Comparer with Amazon Rekognition**



This project is a Python script that utilizes Amazon Rekognition, an AWS service powered by deep learning, to compare faces within user-uploaded images against a collection of reference images stored in Amazon S3 buckets. It provides an accurate and efficient solution for face matching tasks with adjustable confidence thresholds.

Functionality
The program performs the following tasks:

Initialization: Initializes the Amazon Rekognition client using Boto3 and specifies the S3 bucket names for the user-uploaded image and the collection of reference images.

Image Comparison: Compares faces within the user-uploaded image (user_image) against each image in the collection bucket (collection_objects) using the compare_faces method from the Rekognition client.

Result Collection: Stores the matching results in a list (results) if the confidence score exceeds a predefined threshold.

Result Sorting and Display: Sorts the matching results by accuracy score and displays the file names of matching images along with their accuracy scores.

How the Code Works
Initialization: The script initializes the Rekognition client with the specified AWS region and sets up the S3 buckets for user-uploaded images and the collection of reference images.

Image Comparison Loop: It iterates through each object in the collection bucket and compares the faces within the user-uploaded image with faces in each reference image using the compare_faces method.

Result Processing: If a face match is found with a confidence score greater than or equal to the specified threshold, the result is stored in the results list.

Result Presentation: Finally, the script sorts the matching results by accuracy score in descending order and displays the file names of matching images along with their accuracy scores.

Getting Started
To use this program:

Set up your AWS credentials in config.py.
Replace the placeholder bucket names (your_bucket) in the script with your actual S3 bucket names.
Run the script using Python (python face_comparer.py).
Contributions
Contributions are welcome! Please feel free to open issues or pull requests for any improvements or features you'd like to see added.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Special thanks to the AWS team for providing excellent documentation and support for their services.
