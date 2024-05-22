import os
import sys
from source.exception import CustomException
from source.utils.utils import download_file_from_s3,read_class_labels
from source.aws_connection.aws_connection import S3Client
from source.logging import logger
from source.configuration.entity import ModelIngestionConfig
import tensorflow as tf

class ModelIngestion:
    model=None

    def __init__(self, config: ModelIngestionConfig):
        self.config = config

    def download_model(self):
        logger.info("model downloading started")
        try:
            # create model directory if not present
            os.makedirs(self.config.model_dir,exist_ok=True)

            if self.config.model_name not in os.listdir(self.config.model_dir):
                download_file_from_s3(
                    object_name=self.config.s3_model_path,
                    file_name=self.config.model_path
                    )
                print("model not present")

                logger.info(f"model is downloaded successfully at {self.config.model_path}")
            else:
                logger.info(f"model is already present in {self.config.model_path}")

            if self.config.label_map_name not in os.listdir(self.config.model_dir):
                download_file_from_s3(
                    object_name=self.config.s3_label_map_path,
                    file_name=self.config.label_map_path
                    )
                print("label map not present")

                logger.info(f"label map is downloaded successfully at {self.config.model_path}")
            else:
                logger.info(f"label map is already present in {self.config.model_path}")

        except CustomException as e:
            raise CustomException(e,sys)
        
    def get_model(self):
        try:
            if ModelIngestion.model is None:
                logger.info(f"model is not available, model ingestion started")
                self.download_model()
                model=tf.keras.models.load_model(self.config.model_path)
                label_map = read_class_labels(self.config.label_map_path)
                ModelIngestion.model=(model,label_map)
                return ModelIngestion.model
            else:
                logger.info(f"model is alreday available")
                return ModelIngestion.model
            
        except CustomException as e:
            raise CustomException(e,sys)






        


