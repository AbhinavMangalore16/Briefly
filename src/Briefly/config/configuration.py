from src.Briefly.utils.common import read_yaml, create_dirs
from src.Briefly.constants import *

from src.Briefly.entity import DataIngestionConfig, DataTransformConfig, TrainingModelConfig, ModelEvaluationConfig

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
    def get_training_model_config(self) -> TrainingModelConfig:
        config = self.config.training_model
        params = self.params.TrainingArguments

        create_dirs([config.root_dir])
        training_model_config = TrainingModelConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            model_checkpoint=config.model_checkpoint,
            num_train_epochs=params.num_train_epochs,
            per_device_train_batch_size=params.per_device_train_batch_size,
            per_device_eval_batch_size= params.per_device_eval_batch_size,
            warmup_steps=params.warmup_steps,
            weight_decay=params.weight_decay,
            logging_steps=params.logging_steps,
            evaluation_strategy=params.evaluation_strategy,
            eval_steps=params.eval_steps,
            save_steps=params.save_steps,
            gradient_accumulation_steps=params.gradient_accumulation_steps
        )
        return training_model_config
    def get_model_evaluation(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        create_dirs([config.root_dir])
        model_eval_config = ModelEvaluationConfig(
            root_dir= config.root_dir,
            dataset_path= config.dataset_path,
            model_path=config.model_path, 
            tokenizer_path=config.tokenizer_path,
            metrics_file=config.metrics_file
        )
        return model_eval_config

            