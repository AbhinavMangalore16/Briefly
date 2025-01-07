from src.Briefly.config.configuration import ConfigManager
from src.Briefly.components.data_transform_comp import DataTransform
from Briefly.logging import logger

class DataTransformPipeline:
    def __init__(self):
        pass
    def init_data_transform(self):
        config = ConfigManager()
        data_transform_config = config.get_datatransform_config()
        data_transform = DataTransform(data_transform_config)
        data_transform.dataset_transform()