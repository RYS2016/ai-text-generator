from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
print(sentence)
print(input_ids)
#I'm so excited to be learning about large language models
{'input_ids': [35, 26, 98, 102, 5564, 22, 39, 1899, 75, 392, 1243, 2626, 4, 3], 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2], 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
input_ids_pt = tokenizer(sentence, return_tensors ="pt")
print(input_ids_pt)
{'input_ids': tensor([[ 101, 1045, 1005, 1049, 2061, 7568, 2000, 2022, 4083, 2055, 2312, 2653,
         4275,  102]]), 'attention_mask': tensor([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])}


model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
with torch.no_grad():
    logits = model(**input_ids_pt).logits

predicted_class_id = logits.argmax().item()
model.config.id2label[predicted_class_id]
'POSITIVE'