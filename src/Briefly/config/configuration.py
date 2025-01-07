from src.Briefly.utils.common import read_yaml, create_dirs
from src.Briefly.constants import *

from src.Briefly.entity import DataIngestionConfig, DataTransformConfig

class ConfigManager: 
    def __init__(self, config_path: Path = CONFIG_PATH, params_path: Path = PARAMS_PATH):
        self.config = read_yaml(config_path) 
        self.params = read_yaml(params_path)

        create_dirs([self.config.artifacts_root])
    def get_dataingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_dirs([config.root_dir,])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    def get_datatransform_config(self) -> DataTransformConfig:
        config = self.config.data_transform

        create_dirs([config.root_dir])

        data_transform_config = DataTransformConfig(
            root_dir=config.root_dir,
            dataset_path=config.dataset_path,
            tokenizer=config.tokenizer,
        )
        return data_transform_config
