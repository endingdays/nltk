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

#  loading some texts for us to explore: 
from nltk.book import *

print('this is text1: ', text1)