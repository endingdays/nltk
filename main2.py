import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown

print('Printing file identifiers of Project Gutenberg for books: \n', gutenberg.fileids())

emma = gutenberg.words('austen-persuasion.txt')
print('\nChoosing "Persuasion" of Jane Austen and printing it\'s length: ', len(emma))

# to apply concordance from main.py we need to employ such statements:
# emma = nltk.Text(gutenberg.words('austen-emma.txt'))
# print('\nConcordance on other texts, other then from nltk.book (with word "surprize"): \n')
# emma.concordance('surprize')

# displaying other information about each text, by looping over all the values of fileid
print('FileId | num_chars |  num_sents | num_words | num_vocab')
for fileId in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileId))
    num_sents = len(gutenberg.sents(fileId))
    num_words = len(gutenberg.words(fileId))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileId)))
    print(fileId, num_chars, num_sents, num_words, num_vocab)

print('Categories of Brown Corpus: \n', brown.categories())

# comparing genres in their usage of modal verbs
print('Comparing news-genres in their usage of modal verbs:')
news_text = brown.words(categories='news')
fdist = nltk.FreqDist(w.lower() for w in news_text)
modal_verbs=['can', 'could', 'may', 'must','might', 'will']
for m in modal_verbs:
    print(m + ':', fdist[m], end=' ')

print('\nCounting a selection of WH words, such as what, when, where, who, and why: ')
mystery_text = brown.words(categories='mystery')
fdist1 = nltk.FreqDist(w.lower() for w in news_text if w.startswith('wh'))
wh_words = ['what', 'where', 'why', 'when', 'who']
for m in wh_words:
    print(m + ':', fdist1[m], end=' ')


print('\nConditional frequency distribution: \n')
# A conditional frequency distribution needs to pair each event with a condition
# Each pair has the form (condition, event) -> here condition is NEWS AND ROMANCE, and event a WORD
genre_word = [(genre, word) for genre in ['news', 'romance'] for word in brown.words(categories=genre)]
print('len(genre_word): ', len(genre_word), ', genre_word[:4]: ', genre_word[:4])
cfd = nltk.ConditionalFreqDist(genre_word)
print("cfd['romance'].most_common(20): ", cfd['romance'].most_common(20))
print("\ncfd['romance']['to']: ", cfd['romance']['to'])
