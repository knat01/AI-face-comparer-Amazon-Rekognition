# AI Face Comparer with Amazon Rekognition

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![AWS Rekognition](https://img.shields.io/badge/AWS%20Rekognition-Ready-orange)
![License](https://img.shields.io/badge/License-MIT-green)

This project utilizes Amazon Rekognition, an AWS service powered by deep learning, to compare faces within user-uploaded images against a collection of reference images stored in Amazon S3 buckets. It provides an accurate and efficient solution for face matching tasks with adjustable confidence thresholds.

## Table of Contents

- [Functionality](#functionality)
- [How to Use](#how-to-use)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Functionality

### Initialization

- **Amazon Rekognition Client:** The program starts by initializing the Amazon Rekognition client using Boto3, AWS's SDK for Python. The client requires AWS credentials (like AWS Access Key and Secret Access Key) which should be securely stored and accessed.
- **S3 Bucket Access:** It specifies the names of two Amazon S3 buckets: one for the user-uploaded image (user_image) and the other for the collection of reference images (collection_objects). The program ensures it has the necessary permissions to access these buckets.

### Image Comparison

- **Fetching Images:** The program retrieves the user-uploaded image and iterates through each image in the collection bucket.
- **Face Comparison:** For each reference image, the program uses the `compare_faces` method of the Rekognition client. This method detects faces in both the user image and the reference image and compares them.
- **Threshold Setting:** A confidence threshold is set to determine whether a match is considered valid. Only matches that exceed this threshold are processed further.

### Result Collection

- **Storing Results:** Each valid match (i.e., exceeding the confidence threshold) is stored in a list (`results`). This list holds details like the reference image name, matched face details, and the confidence score.
- **Handling Multiple Faces:** If the user image contains multiple faces, the program compares each face against the reference images, aggregating all valid matches.

### Result Sorting and Display

- **Sorting:** The results are sorted by their confidence score, ensuring that the most accurate matches are listed first.
- **Display:** The program then displays or outputs the sorted list, showing the reference image file names and their corresponding accuracy scores.

### Additional Functionalities

- **Duplicate Management:** It includes logic to handle situations where multiple faces in the user image match with the same face in the reference images, or vice versa, ensuring each match is distinct.
- **Error Handling:** The program robustly handles and logs errors that might occur during the face comparison process, like API errors or connectivity issues.
- **User Interaction:** Throughout the process, users are kept informed about the progress and any issues encountered. This could be through a command-line interface, a graphical UI, or notifications.

## How to Use

To use this program:

1. Set up your AWS credentials in `config.py`.
2. Replace the placeholder bucket names (`your_bucket`) in the script with your actual S3 bucket names.
3. Run the script using Python (`python face_comparer.py`).

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```
Contributing
Contributions are welcome! Please feel free to open issues or pull requests for any improvements or features you'd like to see added.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
Special thanks to the AWS team for providing excellent documentation and support for their services.
