from dataclasses import dataclass
# from pathlib import Path

@dataclass(frozen=True)
class ModelIngestionConfig:
    model_dir: str
    s3_bucket: str
    s3_model_path: str
    s3_label_map_path: str
    model_name: str
    label_map_name: str
    model_path: str
    label_map_path: str

    