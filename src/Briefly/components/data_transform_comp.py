import os
from src.Briefly.entity import DataTransformConfig
from transformers import AutoTokenizer
from datasets import load_from_disk


class DataTransform:
    def __init__(self, config:DataTransformConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer)
    def features_maker(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'] , max_length = 1024, truncation = True )

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length = 128, truncation = True )

        return {
            'input_ids' : input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }
    def dataset_transform(self):
        samsum_data = load_from_disk(self.config.dataset_path)
        samsum_data_pt = samsum_data.map(self.features_maker, batched=True)
        samsum_data_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))