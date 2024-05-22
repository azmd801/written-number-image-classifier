import tensorflow as tf
# from source.components.inferencing import Inference
from pathlib import Path
import numpy as np
from source.logging import logger
# from source.utils.utils import download_file_from_s3
# from source.aws_connection.aws_connection import S3Clientc




# s3://written-number-classifier/artifact/model-artiact/best_model.keras
# s3_resource = S3Client().s3_resource
# print(s3_resource)

# download_file_from_s3(
#     s3_resource,
#     'written-number-classifier',
#     'artifact/model-artiact/best_model.keras',
#     'model.keras',

# )

image = tf.keras.utils.load_img(
                    path=Path("test_image/image_2.png"),
                    color_mode='grayscale',
                    target_size=(256,256,1),
                    interpolation='nearest'
                    )

image=np.array(image).reshape(1,256,256,1)

logger.info(f"{image.tolist()}")

# inference = Inference()

# print(inference.predict(image))