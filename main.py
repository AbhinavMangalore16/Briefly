from src.Briefly.logging import logger
from src.Briefly.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.Briefly.pipeline.data_transform_pipeline import DataTransformPipeline
from src.Briefly.pipeline.model_training_pipeline import ModelTrainingPipeline

S1 = "STAGE01 - DATA INGESTION PIPELINE"
S2 = "STAGE02 - DATA TRANSFORMATION PIPELINE"
S3 = "STAGE03 - MODEL TRAINING PIPELINE"

try:
    logger.info(f"{S1} initiated")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.init_data_ingestion()
    logger.info(f"{S1} completed!")

except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f"{S2} initiated")
    data_transform_pipeline = DataTransformPipeline()
    data_transform_pipeline.init_data_transform()
    logger.info(f"{S2} completed!")
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f"{S3} initiated")
    training_model_pipeline = ModelTrainingPipeline()
    training_model_pipeline.init_model_training()
    logger.info(f"{S3} completed!")
except Exception as e:
    logger.exception(e)
    raise e