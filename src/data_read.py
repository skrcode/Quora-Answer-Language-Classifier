import pandas as pd
from nltk.corpus import brown
import data_clean
import sys
import glob
import errno

def do():
	# Read data from train
	X_train = pd.DataFrame(columns=('review','type'))

	path = '../data/train_data/*'   
	files = glob.glob(path)
	train = ''
	for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
		with open(name) as f:
			for line in f:
				train+=line
				
	train = train.replace('\n',' ')
	train = train.split('.')

	netreview = ''
	i = 1
	for review in train:
		netreview += (review+'.')
		if i == 10:
			X_train = X_train.append({'review':netreview, 'type':'indian'}, ignore_index=True)
			i = 1
			netreview = ''
		else:
			i = i + 1
	if i!=1:
		X_train = X_train.append({'review':netreview, 'type':'indian'}, ignore_index=True)

	path = '../data/foo/*'   
	files = glob.glob(path)
	train = ''
	for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
		with open(name) as f:
			for line in f:
				train+=line
				
	train = train.replace('\n',' ')
	train = train.split('.')

	netreview = ''
	i = 1
	for review in train:
		netreview += (review+'.')
		if i == 10:
			X_train = X_train.append({'review':netreview, 'type':'non-indian'}, ignore_index=True)
			i = 1
			netreview = ''
		else:
			i = i + 1
	if i!=1:
		X_train = X_train.append({'review':netreview, 'type':'non-indian'}, ignore_index=True)

	# Read data from test
	file = '../data/test_data/test.csv'
	X_test = pd.read_csv( file, header=0,delimiter="," )
	return X_train,X_test