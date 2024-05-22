from source.constants import *
from source.configuration.entity import ModelIngestionConfig

class ConfigurationManager:
     
     def __init__(self):
          pass
     
     def get_model_ingestion_config(self):
          model_ingestion_config = ModelIngestionConfig(
               model_dir=MODEL_DIR,
               s3_bucket=S3_BUCKET,
               s3_model_path=S3_MODEL_PATH,
               s3_label_map_path=S3_LABEL_MAP_PATH,
               model_name=MODEL_NAME,
               label_map_name=LABEL_MAP_NAME,
               model_path=os.path.join(MODEL_DIR,MODEL_NAME),
               label_map_path = os.path.join(MODEL_DIR,LABEL_MAP_NAME)
               )
          
          return model_ingestion_config