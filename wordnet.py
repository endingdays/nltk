from nltk.corpus import wordnet as wn
"""
    WordNet is a semantically-oriented dictionary of English, similar to a traditional thesaurus but with a 
    richer structure NLTK includes the English WordNet, with 155,287 words and 117,659 synonym sets
"""

print("synonym for word 'motorcar': ", wn.synsets('motorcar'))

# car.n.01 is called a synset, or "synonym set", a collection of synonymous words (or "lemmas")
print("\nLemmas for 'car.n.01': ", wn.synset('car.n.01').lemma_names())
print("\nDefinition for 'car.n.01': ", wn.synset('car.n.01').definition())
print("\nExamples for 'car.n.01': ", wn.synset('car.n.01').examples())

# pairing of a synset with a word is called a lemma: car.n.01.automobile, car.n.01.motorcar etc
print(wn.synset('car.n.01').lemmas())
print(wn.lemma('car.n.01.automobile'))
print(wn.lemma('car.n.01.automobile').synset())
print(wn.lemma('car.n.01.automobile').name())

print("Synsets for word 'car': ", wn.synsets('car'))
for synset in wn.synsets('car'):
    print(synset.lemma_names())