import nltk
import random
from nltk.corpus import names


# We start by just looking at the final letter of a given name.
# The following feature extractor function builds a dictionary containing relevant information about a given name:
def gender_features(word):
    return {'last_letter': word[-1]}


#  list of examples and corresponding class labels.
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])
# mixing everything up to make model better
random.shuffle(labeled_names)
# e use the feature extractor to process the names data, and divide the resulting list of feature sets into a
# training set and a test set. The training set is used to train a new "naive Bayes" classifier.
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]

train_set, test_set = featuresets[500:], featuresets[:500]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(classifier.classify(gender_features('Pasha')))
