from src.Briefly.logging import logger
from src.Briefly.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.Briefly.pipeline.data_transform_pipeline import DataTransformPipeline
from src.Briefly.pipeline.model_training_pipeline import ModelTrainingPipeline
from src.Briefly.pipeline.model_evaluation_pipeline import ModelEvaluatePipeline

STAGES = {
    "S1": "STAGE01 - DATA INGESTION PIPELINE",
    "S2": "STAGE02 - DATA TRANSFORMATION PIPELINE",
    "S3": "STAGE03 - MODEL TRAINING PIPELINE",
    "S4": "STAGE04 - MODEL EVALUATION PIPELINE",
}

def execute_pipeline(stage_name, pipeline_class, pipeline_method):
    try:
        logger.info(f"{stage_name} initiated")
        pipeline_instance = pipeline_class()
        getattr(pipeline_instance, pipeline_method)()
        logger.info(f"{stage_name} completed!")
    except Exception as e:
        logger.exception(f"Error during {stage_name}: {e}")
        raise e

if __name__ == "__main__":
    execute_pipeline(STAGES["S1"], DataIngestionPipeline, "init_data_ingestion")
    execute_pipeline(STAGES["S2"], DataTransformPipeline, "init_data_transform")
    execute_pipeline(STAGES["S3"], ModelTrainingPipeline, "init_model_training")
    execute_pipeline(STAGES["S4"], ModelEvaluatePipeline, "init_evaluate_model")
