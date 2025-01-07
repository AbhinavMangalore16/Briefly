import torch
import os
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, DataCollatorForSeq2Seq, TrainingArguments, Trainer
from src.Briefly.entity import TrainingModelConfig
from datasets import load_from_disk

class TrainingModel:
    def __init__(self, config:TrainingModelConfig):
        self.config = config
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_checkpoint)
        model_google_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_checkpoint).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_google_pegasus)

        dataset_samsum_pt = load_from_disk(self.config.data_path)

        training_arguments = TrainingArguments(
            output_dir=self.config.root_dir, 
            num_train_epochs=1,
            warmup_steps=500,
            per_device_train_batch_size=1, 
            per_device_eval_batch_size=1,
            weight_decay=0.01, logging_steps=10,
            evaluation_strategy='steps', eval_steps=500, 
            save_steps=1e6,
            gradient_accumulation_steps=16
        )
        trainer = Trainer(model=model_google_pegasus, args=training_arguments,
                  processing_class=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=dataset_samsum_pt["test"],
                  eval_dataset=dataset_samsum_pt["validation"])
        trainer.train()
        model_google_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))