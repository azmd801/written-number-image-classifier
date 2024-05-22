from source.aws_connection.aws_connection import S3Client
from source.constants import S3_BUCKET
import json

s3_resource = S3Client().s3_resource

def download_file_from_s3(object_name, file_name):
    """
    Download a file from an S3 bucket

    :param bucket_name: Name of the S3 bucket
    :param object_name: Name of the object in S3
    :param file_name: Name of the file to save as locally
    :return: True if file was downloaded, else False
    """

    # Download the file
    try:
        s3_resource.Bucket(S3_BUCKET).download_file(object_name, file_name)
        print(f"File {object_name} from bucket {S3_BUCKET} downloaded as {file_name}")
        return True
    except Exception as e:
        print(f"Error downloading file: {e}")
        return False
    



def read_class_labels(filename):
    """
    Read class labels from a JSON file.

    Args:
        filename (str): The filename of the JSON file.

    Returns:
        dict: A dictionary containing the class labels.
    """
    with open(filename, 'r') as f:
        class_labels = json.load(f)
    return class_labels