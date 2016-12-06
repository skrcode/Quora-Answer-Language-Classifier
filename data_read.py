import pandas as pd
import re
from nltk.corpus import brown
import data_clean
import nltk
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
import numpy as np
def browndata(X_train):
	for genre in ['adventure','fiction']:
		print genre
		article = brown.paras(categories=genre)

		for review in article:
			X_train = X_train.append({'review' : review, 'category':'other'}, ignore_index=True)
	return X_train

def do(bookfile):
	X_train = pd.DataFrame(columns=('review','category'))
	X_train = browndata(X_train)
	train_sentences = []
	for review_list in X_train['review']:
		
		for r in review_list:
			rlist = []
			for rr in r:
				x = re.sub("[^a-zA-Z]"," ", rr.decode('utf-8')).lower()
				for i in x.split(' '):
					if i != '':
						rlist.append(i)
			train_sentences.append(rlist)
			#for r in rlist:
			#	review = []
			#	for rdash in r:
			#		review_text = re.sub("[^a-zA-Z]"," ", rdash.decode('utf-8')).lower()
			#		review.append(review_text)
			#	train_sentences.append(review)

	f = open(bookfile)
	X = f.read().decode('utf-8').replace('\n',' ')
	y= re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s',X)
	test_sentences = train_sentences
	i = 0
	rev = []
	for review in y:
		i = i + 1
		x = data_clean.review_to_sentences(review, tokenizer, remove_stopwords = False)
		test_sentences += x
		if i%3 == 0:
			X_train = X_train.append({'review' : rev, 'category':'indian'}, ignore_index=True)
			rev = []
		else:
			rev+=x
	if len(x):
		X_train = X_train.append({'review' : rev, 'category':'indian'}, ignore_index=True)
	X_train = X_train.iloc[np.random.permutation(len(X_train))]
	return X_train,test_sentences