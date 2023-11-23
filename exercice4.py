import numpy as np

import json
import tensorflow as tf

# Paramètres modifiables
vocab_size = 1000
embedding_dim = 16
max_length = 120
trunc_type='post'
padding_type='post'
oov_tok = "<OOV>"
training_size = 20000

# Dataset
with open("sarcasm.json", 'r') as f:
    datastore = json.load(f)


sentences = []
labels = []
urls = []
for item in datastore:
    sentences.append(item['headline'])
    labels.append(item['is_sarcastic'])

training_sentences = sentences[0:training_size]
testing_sentences = sentences[training_size:]
training_labels = labels[0:training_size]
testing_labels = labels[training_size:]

# tokenizer


# text to sequences et padding
training_sequences = _
testing_sequences = _
training_padded = _
testing_padded = _



# model training with RNN or LSTM
model = _


# evaluation

results = model.evaluate(testing_padded, testing_labels)
print(results)

# sauvegarde
model.save("exercice4.h5")

