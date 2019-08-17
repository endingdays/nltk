# Before going further you should install NLTK 3.0:
#       pip install nltk
# Then install the data required for the book by typing the following two commands,
# then selecting the book collection from an available packages :
#       import nltk
#       nltk.download()
# to install the data required
#  BOOK consists of about 30 compressed files requiring about 100Mb disk space.
# The full collection of data (i.e., all in the downloader) is nearly ten times this size
# Once you run installed nltk and executed 2 commands above you are free to use collection of books, provided
# by nltk anywhere and whenever. Also typing
#       nltk.download()
# browse more data given by nltk creators


# ********** START: Block For Functions
def lexical_diversity(text):
    return len(set(text)) / len(text)


def percentage(text, word):
    return 100 * text.count(word) / len(text)
# ********** END: Block For Functions


#  loading some texts for us to explore:
from nltk.book import *

print('\nThis is text1: ', text1)

"""

# concordance view shows us every occurrence of a given word, together with some context
print('\nCONCORDANCE: ')
text1.concordance('monstrous')
# What words appear in a similar range of contexts
print('\nSIMILAR: ')
text1.similar("monstrous")
print('\nSIMILAR: ')
text2.similar("monstrous")

# common_contexts allows us to examine just the contexts that are shared by two or more words
print('\nCOMMON_CONTEXTS between "monstrous" and "very": ')
text2.common_contexts(["monstrous", "very"])

print('\nCOMMON_CONTEXTS between "small" and "little": ')
text7.common_contexts(["small", "little"])

# with dispersion_plot we can  determine the location of a word in the text
# below - some striking patterns of word usage over the last 220 years
text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America", "sex", "war", "President"])

# generating some random text in the various styles
text3.generate()
print('\nLength of a text3: ', len(text3))
print('\nLength of a set from text3, unique words: ', len(set(text3)))

# calculating a measure of the lexical richness of the text
print('\nRichness of vocabulary in text3: ', lexical_diversity(text3))

# how often a word occurs in a text, and what percentage of the text is taken up by a specific word
print('\nHow often a word occurs in a text: ', text5.count("here"))
print('\nWhat percentage of the text is taken up by a specific word: ', percentage(text5, 'lol'))



# frequency distribution tells us the frequency of each vocabulary item in the text
fdist1 = FreqDist(text1)
# inspecting the total number of words ("outcomes")
print('\nFrequency distribution of text1: ', fdist1)
#  most_common(50) gives us a list of the 50 most frequently occurring types in the text
print('\nMost common tokens are : ', fdist1.most_common(50))

# cumulative frequency plot for these words
fdist1.plot(50, cumulative=True)
#  the words that occur once only,
print('\nhapaxes: ', fdist1.hapaxes())
"""
#  let's look at the long words of a text, that are > 15
V = set(text7)
long_words = [w for w in V if len(w) > 10]
print('\nOur long words: ', sorted(long_words))

fdist5 = FreqDist(text5)
# making sure  that the words are longer than seven letters, and ooccur more than seven times
print('\nwords from the chat corpus that are longer than seven characters, that occur more than seven times: ',
      sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7))

# collocation is a sequence of words that occur together unusually often: red whine, hot water etc.
# To get a handle on collocations, start off by extracting from a text a list of word pairs, also known as bigrams
print('\nBigrams: ', list(bigrams(['water', 'hot', 'red', 'whine', 'cold', 'weather'])))

print('\nCounting length of each word in a text: ', [len(w) for w in text1])
fdist = FreqDist(len(w) for w in text1)
# how frequent the different lengths of word are
print('\nHow frequent the different lengths of word are', fdist.most_common())
print('\nThe most frequent word\'s length is: ', fdist.max())
print('\nPercentage of the msx\'s word: ', fdist.freq(3))