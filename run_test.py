import sys
sys.path.insert(0, 'src')
import data_read 
import train_word2vec
import vector_avg
import get_sentences
import centroid_bow
import train
import write_result
import cPickle
from sklearn.externals import joblib

def compute_genre_test(word_centroid_map,num_clusters,forest,review):

	test_centroids = centroid_bow.get_bag_of_centroids_test(word_centroid_map,num_clusters,review)
	result = forest.predict(test_centroids)
	return result[0]

review = ''
with open("insert_answer", "r") as ins:
    array = []
    for line in ins:
        review += line
# Retrieve computed model
from gensim.models import Word2Vec
model = Word2Vec.load("src/Word2Vec_AnswerClass")
# Get centroids Bag of Words
with open('variables/num_clusters', 'rb') as f:
	num_clusters = cPickle.load(f)
with open('variables/word_centroid_map', 'rb') as f:
	word_centroid_map = cPickle.load(f)
# Test the saved RandomForest to get results on test data                                                                                                                                                                                                       
forest = joblib.load('models/forest')
print compute_genre_test(word_centroid_map,num_clusters,forest,review)