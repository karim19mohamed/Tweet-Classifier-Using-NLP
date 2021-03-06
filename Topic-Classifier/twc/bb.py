import os
import re
import nltk
import glob
import random
import pickle
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title, show

raw_data_path = "data/raw"
os.chdir(raw_data_path)
raw_files = glob.glob("*.txt")
print(raw_files)

m=[]
for u in raw_files:
    #u.split('.txt')
    m.append(u.replace('.txt',''))
    
    #m=m+1
    print(m)
    
documents= []
all_words  = []
ax=[]
stp = stopwords.words('english')
import sys
for f in raw_files:
    n=0
    t = open(f, encoding="utf8").read()
    for p in t.split('\n'):
        n=n+1 
    ax.append(n)
print(ax)

x=[88,83,84]
y=['SVM','Naive','MNB']

fig = plt.figure(figsize=(8,6))
#plt.xlim(xmax=6)
#plt.xlim(xmin=-1)
#plt.margins(x=0)
plt.bar(y,x, label='Bars',align='center')

#plt.bar(m,ax, label='Bars',align='center')
#plt.xlabel('class')
#plt.ylabel('number of training data')
#plt.show()
plt.xlabel('Classifier')
plt.ylabel('Accuracy')
#plt.savefig('E:\\Hell\\Year 5\\Spring\\NLP\\Project\\Tweet-Classifier\\twc\\result.png')
plt.savefig('E:\\Hell\\Year 5\\Spring\\NLP\\Project\\Tweet-Classifier\\twc\\foo.png')

        
"""  
		p = re.sub(r'[^\w\s]','',p)
		p = re.sub(" \d+", " ", p)
		p = [i.lower() for i in list(set(nltk.word_tokenize(p)) - set(stp))]
		all_words+=p
		documents.append((p, f[:-4]))

random.shuffle(documents)

word_features = list(all_words)

print("Sample:")
print(documents[1])
print(word_features[1])
def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % str(word)] = (word in document_words)
	return features

featuresets = [(document_features(d), c) for (d,c) in documents]

train_set, test_set = featuresets[100:], featuresets[:100]

print(len(train_set), len(test_set))

classifier = nltk.NaiveBayesClassifier.train(train_set)
print("NaiveBayes accuracy:", (nltk.classify.accuracy(classifier, test_set))*100)


LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(train_set)
print("LinearSVC_classifier accuracy:", (nltk.classify.accuracy(LinearSVC_classifier, test_set))*100)


os.chdir("../../")


save_word_features = open("data/trained/word_features.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()

save_classifier = open("data/trained/SVC.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

save_classifier = open("data/trained/NAIVE.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()




# #-----more accurate-----

MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(train_set)
print("MNB_classifier accuracy:", (nltk.classify.accuracy(MNB_classifier, test_set))*100)

save_classifier = open("data/trained/MNB.pickle","wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

"""