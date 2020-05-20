###################################################
from manage_class import *
###################################################
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
####################################################
#Import ML library sklearn
import sklearn 
#import datasets, classifiers and performance metrics
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
import sklearn.datasets.samples_generator
#####################################################
#####################################################
#Library for API searchs
from psaw import PushshiftAPI
from newsapi import NewsApiClient
#####################################################
import mechanize
from mechanize import Browser 
#init
newsapi = NewsApiClient(api_key='4e18ca1d616e42348999bdee41f66a36')
########################################################
#N_trusted sites 
N_trusted=['nbcnews','reuters','bbc-news','theguardian','reuters','cnn','cbc','nationalpost',
'independent','cnn','uk-reuters','time','washingtonexaminer','news.sky','newsweek','thesun',
'washingtonpost','france24','vox','dutchnews','nytimes','twitter',
'metro','bloomberg','japantimes','financialnews']

hoax=['LinkBeef','Opindia',]
############################################################################################
def convert(char):
	num_char=''
	for letter in char:
		num_char += str(ord(letter))
	return int(num_char)
############################################################################################
#fill with N_trusted sources and also Fake news we will use API search to fill it
def create_features_labels(keywords):
	#we create features 
	features=[]
	labels=[]
	for source in N_trusted:
		#we choose not to add q=keywords input because the research is not efficient
		top_headlines = newsapi.get_top_headlines(sources =source,language ='en')
		num_domain = convert(source)
		score=100
		for i in range (len(top_headlines['articles'])):
			article_title = top_headlines['articles'][i]['title']
			num_art = convert(article_title)
			features.append[[num_domain,num_art]]
			labels.append(score)

	for source in hoax:
		top_headlines = newsapi.get_top_headlines(sources =source,language ='en')
		num_domain = convert(source)
		score=100
		for i in range (len(top_headlines['articles'])):
			article_title = top_headlines['articles'][i]['title']
			num_art = convert(article_title)
			features.append[[num_domain,num_art]]
			labels.append(score)
	
	return [features,labels]


#Loading features and labels
features = create_features_labels[0]
labels = create_features_labels[1]


clf = tree.DecisionTreeClassifier()
#learning model
clf = clf.fit(features,labels)
clf.predict([[news]])
