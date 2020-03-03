import tweepy
import pickle
import nltk
import re
#twc\data\trained\MNB.pickle
#classifier = pickle.load(open('data/trained/MNB.pickle', 'rb'))

classifier = pickle.load(open('data/trained/NAIVE.pickle', 'rb'))

#classifier = pickle.load(open('data/trained/SVC.pickle', 'rb'))

word_features = pickle.load(open('data/trained/word_features.pickle', 'rb'))

def document_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
		features['contains(%s)' % word] = (word in document_words)
	return features

def tweet_clean(t):
		t = t.replace("#", "")
		t = t.replace("@", "")
		t = re.sub(r"[^\w\s]","",t)
		t = re.sub(" \d+", " ", t)
		return t


def is_actionable(t):
	t = tweet_clean(t)
	tags = [i[1] for i in nltk.pos_tag(t.split())]
	if len(t.split())>4:
		if 'NN' and 'VBD' or 'VB' in tags:
			return True
		else:
			False
	else:
		False


def predict_topic(s):
	s = tweet_clean(s)
	token = nltk.word_tokenize(s.lower())
	return classifier.classify(document_features(token))


class Tweetifier:
	def __init__(self, user, count=10):
		self.consumer_key = "RPx7Jhfb9LISk03Jpr0oKrzhB"
		self.consumer_secret = "2iui05j4CyYvIpbTVyG0MrEDpJWwDZZGm8lHHaajCxM3YzHsLA"

		self.access_token = "1962132122-glIIRzQJMr85UjJFe1WRN57sbmE0tIGfV8oAByE"
		self.access_token_secret = "43JqbCuMpbLSjL7VDQfnknup0TlXUccY8wtk1aXPLdyzP"

		self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		self.auth.set_access_token(self.access_token, self.access_token_secret)

		self.count = count
		self.user = user

		self.tweets = []
		self.topic_bucket = {}

	def crawl(self):
		try:
			api = tweepy.API(self.auth)
			for status in tweepy.Cursor(api.user_timeline, id=self.user, retweets=True).items(self.count):
				self.tweets.append(status.text)
		except Exception as e:
			print(e)

	def classify(self):
		for t in self.tweets:
			if is_actionable(t):
				topic = predict_topic(t)
				if self.topic_bucket.get(topic):
					self.topic_bucket[topic].append(t)
				else:
					self.topic_bucket[topic] = [t]


if __name__=="__main__":
    t = Tweetifier("HarvardHBS", count=10)
    t.crawl()
    t.classify()
    output=t.topic_bucket
    classes=['business', 'entertainment', 'health', 'politics', 'sports', 'technology']
    with open('Naiveout_HarvardHBS.txt', 'w',encoding='utf-8') as f:
        for i in range(6):
            print(classes[i], file=f)
            print(output.get(classes[i]), file=f)
    print(t.topic_bucket)
#for i in t.topic_bucket:
#    print(i)

	
