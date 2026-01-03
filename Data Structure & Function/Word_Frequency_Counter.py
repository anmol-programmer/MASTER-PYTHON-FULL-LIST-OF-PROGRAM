from collections import Counter

def word_frequency(sentence):
    return dict(Counter(sentence.split()))
