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

The program performs the following tasks:

1. **Initialization**: Initializes the Amazon Rekognition client using Boto3 and specifies the S3 bucket names for the user-uploaded image and the collection of reference images.

2. **Image Comparison**: Compares faces within the user-uploaded image (`user_image`) against each image in the collection bucket (`collection_objects`) using the `compare_faces` method from the Rekognition client.

3. **Result Collection**: Stores the matching results in a list (`results`) if the confidence score exceeds a predefined threshold.

4. **Result Sorting and Display**: Sorts the matching results by accuracy score and displays the file names of matching images along with their accuracy scores.

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

## Contributing

Contributions are welcome! Please feel free to open issues or pull requests for any improvements or features you'd like to see added.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the AWS team for providing excellent documentation and support for their services.
```
