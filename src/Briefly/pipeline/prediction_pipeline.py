from src.Briefly.config.configuration import ConfigManager
from transformers import AutoTokenizer
from transformers import pipeline

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigManager().get_model_evaluation()
    def predict(self, input_text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
        pipeline_ml = pipeline("Text Summarization by Briefly", model = self.config.model_path, tokenizer=tokenizer)
        
        print("Dialogue:")
        print(input_text)
        output_summary = pipeline_ml(input_text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output_summary)
        return output_summary