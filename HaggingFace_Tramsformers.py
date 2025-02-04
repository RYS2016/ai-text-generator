from transformers import pipeline

sentiment_classifier = pipeline("sentiment-analysis")
sentiment_classifier("I'm so excited to be learning about large language models")
#[{'label': 'POSITIVE', 'score': 0.9997096657752991}]

#choose a specific model we want to use:
ner = pipeline("ner", model = "dslim/bert-base-NER")
ner("Her name is Anna and she works in New York City for Morgan Stanley")

#using a Facebook model
zeroshot_classifier = pipeline("zero-shot-classification", model = "facebook/bart-large-mnli")

sequence_to_classify = "one day I will see the world"
candidate_labels = ['travel', 'cooking', 'dancing']
zeroshot_classifier(sequence_to_classify, candidate_labels)
#output:
{'sequence': 'one day I will see the world',
 'labels': ['travel', 'dancing', 'cooking'],
 'scores': [0.9938651919364929, 0.0032737581059336662, 0.0028610501904040575]}