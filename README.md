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
pip install sklearn

```
```





