from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_from_disk

import torch
import pandas as pd
from tqdm import tqdm
import evaluate
from src.Briefly.entity import ModelEvaluationConfig


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config 
    def batch_chunking(self, list_of_elements, batch_size):
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i : i + batch_size]
    def evaluate_test(self, dataset, metric, model, tokenizer,
                               batch_size=16, device="cuda" if torch.cuda.is_available() else "cpu",
                               column_text="article",
                               column_summary="highlights"):
        article_batches = list(self.batch_chunking(dataset[column_text], batch_size))
        target_batches = list(self.batch_chunking(dataset[column_summary], batch_size))

        for article_batch, target_batch in tqdm(
            zip(article_batches, target_batches), total=len(article_batches)):

            inputs = tokenizer(article_batch, max_length=1024,  truncation=True,
                            padding="max_length", return_tensors="pt")

            summaries = model.generate(input_ids=inputs["input_ids"].to(device),
                            attention_mask=inputs["attention_mask"].to(device),
                            length_penalty=0.8, num_beams=8, max_length=128)
            ''' parameter for length penalty ensures that the model does not generate sequences that are too long. '''

            decoded_summaries = [tokenizer.decode(s, skip_special_tokens=True,clean_up_tokenization_spaces=True) for s in summaries]

            decoded_summaries = [d.replace("", " ") for d in decoded_summaries]


            metric.add_batch(predictions=decoded_summaries, references=target_batch)
        score = metric.compute()
        return score
    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model_google_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)

        dataset_samsum_pt = load_from_disk(self.config.dataset_path)
        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rouge_metric = evaluate.load('rouge')
        score = self.evaluate_test(
            dataset_samsum_pt['test'][0:10], rouge_metric, model_google_pegasus, tokenizer, batch_size = 2, column_text = 'dialogue', column_summary= 'summary'
        )

        rouge_dict = {rn: score[rn] for rn in rouge_names}
        met = pd.DataFrame(rouge_dict, index=[f'pegasus'])
        met.to_csv(self.config.metrics_file, index = False)