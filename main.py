from src.Briefly.logging import logger
from src.Briefly.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.Briefly.pipeline.data_transform_pipeline import DataTransformPipeline

S1 = "STAGE01 - DATA INGESTION PIPELINE"
S2 = "STAGE02 - DATA TRANSFORMATION PIPELINE"

try:
    logger.info(f"{S1} initiated")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.init_data_ingestion()
    logger.info(f"{S1} completed!")

    logger.info(f"{S2} initiated")
    data_transform_pipeline = DataTransformPipeline()
    data_transform_pipeline.init_data_transform()
    logger.info(f"{S2} completed!")


except Exception as e:
    logger.exception(e)
    raise e
