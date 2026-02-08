import nltk
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sample_text="I am learning right now"
tokens= nltk.word_tokenize(sample_text.lower())
print('Tokens:',tokens)

sentence = "I am learning AI"
tokens = word_tokenize(sentence)
# Unigram
unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

# Bigram
bigrams = list(ngrams(tokens, 2))
print('Bigrams:', bigrams)

# Trigram
trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)
