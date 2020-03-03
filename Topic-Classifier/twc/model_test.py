import pickle
import nltk

classifierMNB = pickle.load(open('data/trained/MNB.pickle', 'rb'))
classifierNAIVE = pickle.load(open('data/trained/NAIVE.pickle', 'rb'))
classifierSVC = pickle.load(open('data/trained/SVC.pickle', 'rb'))
classifiers=[classifierMNB,classifierNAIVE,classifierSVC]


word_features = pickle.load(open('data/trained/word_features.pickle', 'rb'))

def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

def predict_topic(s,j):
    token = nltk.word_tokenize(s.lower())
    classifier=classifiers[j]
    
    return classifier.classify(document_features(token))

clas=['MNB.csv','NAIVE.csv','SVM.csv']
for j in range(3):
    cls=clas[j]
    with open('test.txt', 'r') as f:
        with open(cls, 'w') as ff:
            for i in f:    
                #print(i)
                topic = predict_topic(i,j)
                print(topic,',',i, file=ff)
                #print(,file=ff)
        #topic = predict_topic("""Well, that is taxation law of India (other side).In India 52,911 
		 #			Profitable Companies Pay 0% Tax in India!""")

#print('-----------------------------------------------------------------')
#print(topic)