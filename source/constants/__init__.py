import os

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
REGION_NAME = 'us-east-1'

S3_BUCKET = 'written-number-classifier'

S3_MODEL_PATH = 'model_registry/prod_model.h5'

S3_LABEL_MAP_PATH = 'artifact/label-artifact/labels.json'

MODEL_DIR = 'model'

MODEL_NAME = 'prod_model.h5'

LABEL_MAP_NAME = 'labels.json'