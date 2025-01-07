from src.Briefly.config.configuration import ConfigManager
from src.Briefly.components.model_training_comp import TrainingModel

class ModelTrainingPipeline:
    def __init__(self):
        pass
    def init_model_training(self):
        config = ConfigManager()
        training_model_config = config.get_training_model_config()
        training_model_config = TrainingModel(config=training_model_config)
        training_model_config.train()