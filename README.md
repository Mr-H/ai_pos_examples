# ai_pos_examples
Parts of Speech - Example Code 

## nltk example 

Source: https://pythonexamples.org/nltk-pos-tagging/

pip install nltk

```
import nltk

# Download required nltk packages

# Required for tokenization
nltk.download('punkt')

# Required for parts of speech tagging
nltk.download('averaged_perceptron_tagger')

# Input text
sentence = """Today morning, Arthur felt very good."""

# Tokene into words
tokens = nltk.word_tokenize(sentence)

# Parts of speech tagging
tagged = nltk.pos_tag(tokens)

# Print tagged tokens
print(tagged)
```
Then output looks like this 
[('Today', 'NN'), ('morning', 'NN'), (',', ','), ('Arthur', 'NNP'), ('felt', 'VBD'), ('very', 'RB'), ('good', 'JJ'), ('.', '.')]

## Gaussian Naive Bayes Example 

pip install pandas
pip install numpy
pip install scikit-learn

Source: https://dataaspirant.com/gaussian-naive-bayes-classifier-implementation-python/

```
# Required Python Machine learning Packages
import pandas as pd
import numpy as np
# For preprocessing the data
from sklearn.preprocessing import Imputer
from sklearn import preprocessing
# To split the dataset into train and test datasets
from sklearn.cross_validation import train_test_split
# To model the Gaussian Navie Bayes classifier
from sklearn.naive_bayes import GaussianNB
# To calculate the accuracy score of the model
from sklearn.metrics import accuracy_score

```





