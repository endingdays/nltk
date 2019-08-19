"""
    The process of classifying words into their parts of speech and labeling them accordingly is known as
    part-of-speech tagging, POS-tagging, or simply tagging. Parts of speech are also known as word classes or
    lexical categories. The collection of tags used for a particular task is known as a tagset.
"""

import nltk

text = nltk.word_tokenize("Back in elementary school you learnt the difference between nouns, verbs, adjectives, and adverbs.")
print('CC is a coordinating conjunction; RB - adverbs; IN is a preposition; '
      'NN - noun; JJ is an adjective: \n', nltk.pos_tag(text))

print('What DT, VBP, PRP and NNS stand for: ')
nltk.help.upenn_tagset('DT')
nltk.help.upenn_tagset('VBP')
nltk.help.upenn_tagset('PRP')
nltk.help.upenn_tagset('NNS')

# .similar() method takes a word w, finds all contexts w1w w2, then finds all words w' that appear in the same context
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print("text.similar('woman'): ")
text.similar('woman')
print("text.similar('buy'): ")
text.similar('buy')
