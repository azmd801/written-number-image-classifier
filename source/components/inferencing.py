from source.components.model_ingestion import ModelIngestion
from source.configuration.configuration import ConfigurationManager
from source.exception import CustomException
from source.logging import logger
import numpy as np
import sys


class Inference:
    def __init__(self):
        self.config = ConfigurationManager().get_model_ingestion_config()
        self.model_ingestion = ModelIngestion(self.config)

    def predict(self,data):
        try:
            model,label_map = self.model_ingestion.get_model()
            predictions = model.predict(data)
            predictions = np.argmax(predictions)
            predictions = label_map[str(predictions)]
            logger.info(f"Model returned {predictions} for the querry")

            return predictions
        
        except CustomException as e:
            raise CustomException
        
