import os
import boto3

from source.constants import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    REGION_NAME,
    )


class S3Client:

    s3_resource = None

    def __init__(self):

        if S3Client.s3_resource == None:
            __access_key_id = AWS_ACCESS_KEY_ID

            __secret_access_key = AWS_SECRET_ACCESS_KEY

            if __access_key_id is None:
                raise Exception(
                    f"Environment variable: {AWS_ACCESS_KEY_ID} is not not set."
                )

            if __secret_access_key is None:
                raise Exception(
                    f"Environment variable: {AWS_SECRET_ACCESS_KEY} is not set."
                )
          
            S3Client.s3_resource = boto3.resource(
                "s3",
                aws_access_key_id=__access_key_id,
                # aws_access_key_id='ddddd',
                aws_secret_access_key=__secret_access_key,
                region_name=REGION_NAME,
            )

        self.s3_resource = S3Client.s3_resource