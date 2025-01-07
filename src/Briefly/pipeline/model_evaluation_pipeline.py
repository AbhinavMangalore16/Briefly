from src.Briefly.config.configuration import ConfigManager
from src.Briefly.components.model_evaluation_comp import ModelEvaluation

class ModelEvaluatePipeline:
    def __init__(self):
        pass
    def init_evaluate_model(self):
        config = ConfigManager()
        training_model_config = config.get_training_model_config()
        training_model_config = ModelEvaluation(config=training_model_config)
        training_model_config.train()