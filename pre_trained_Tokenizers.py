from transformers import AutoTokenizer

#specify the model you want to use:
model = "bert-base-uncased"
#then we call the pre-trained tokenizer for this model:
tokenizer = AutoTokenizer.from_pretrained(model)
#let's run a sentence to check how it works
sentence = "I'm so excited to be learning about large language models"
#then call our tokenizer over our sentence
input_ids = tokenizer(sentence)
#let's inspect them
print(input_ids)
{'input_ids': [101, 1045, 1005, 1049, 2061, 7568, 2000, 2022, 4083, 2055, 2312, 2653, 4275, 102], 
 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #used when we want to distinguish one sentence from another
 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
#Breaking our sentence into tokens:
tokens = tokenizer.tokenize(sentence)
#let's inspect them
print(tokens)
['i', "'", 'm', 'so', 'excited', 'to', 'be', 'learning', 'about', 'large', 'language', 'models']
#These tokens are then converted into a numerical value based on a predefined vocabulary specific to the model
token_ids = tokenizer.convert_tokens_to_ids(tokens)
print(token_ids)
[1045, 1005, 1049, 2061, 7568, 2000, 2022, 4083, 2055, 2312, 2653, 4275]
#We can also decode these token IDs back into tokens to check this
decoded_ids = tokenizer.decode(token_ids)
print(decoded_ids)
#i'm so excited to be learning about large language models

#decode to check their meaning
#These are special tokenz added by out tokenizer
tokenizer.decode(101)
'[CLS]'
tokenizer.decode(102)
'[SEP]'

#Another LLM
model2 = "xlnet-base-cased"
tokenizer2 = AutoTokenizer.from_pretrained(model2)
input_ids = tokenizer2(sentence)
print(input_ids)
{'input_ids': [35, 26, 98, 102, 5564, 22, 39, 1899, 75, 392, 1243, 2626, 4, 3], 
 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
   'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}
#let's see the difference
tokens = tokenizer2.tokenize(sentence)
print(tokens)
['▁I', "'", 'm', '▁so', '▁excited', '▁to', '▁be', '▁learning', '▁about', '▁large', '▁language', '▁models']

token_ids = tokenizer2.convert_tokens_to_ids(tokens)
print(token_ids)
[35, 26, 98, 102, 5564, 22, 39, 1899, 75, 392, 1243, 2626]

tokenizer2.decode(4)
'<sep>'
tokenizer2.decode(3)
'<cls>'