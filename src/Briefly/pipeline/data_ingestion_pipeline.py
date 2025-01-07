from src.Briefly.config.configuration import ConfigManager
from src.Briefly.components.data_ingestion_comp import DataIngestion
from Briefly.logging import logger


class DataIngestionPipeline:
    def __init__(self):
        pass

    def init_data_ingestion(self):
        config_manager = ConfigManager()
        data_ingestion_config = config_manager.get_dataingestion_config()

        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()