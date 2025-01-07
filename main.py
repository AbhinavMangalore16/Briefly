from src.Briefly.logging import logger
from src.Briefly.pipeline.data_ingestion_pipeline import DataIngestionPipeline

S1 = "STAGE01 - DATA INGESTION PIPELINE"

try:
    logger.info(f"{S1} initiated")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.init_data_ingestion()
    logger.info(f"{S1} completed!")

except Exception as e:
    logger.exception(e)
    raise e
