import requests
import csv
import pandas as pd 
from psaw import PushshiftAPI

#######################################
#NLP library
import spacy
#from nltk.corpus import stopwords

#######################################
#we define a list of english stopwords
dirty_list=[]
stopWords =[]
file =open("english","r")
dirty_list = file.readlines()
for words in dirty_list:
	clean_words=''
	k =len(words)
	clean_words =words[:k-1]
	stopWords.append(clean_words)
file.close()
########################################
nlp = spacy.load("en_core_web_md")

########################################
import numpy as np 
########################################

#Our N_trusted list 
N_trusted=['nbcnews.com','in.reuters.com','bbc.co.uk','theguardian.com','reuters.com','edition.cnn.com','cbc.com','nationalpost.com',
'independent.co.uk','cnn.com','uk.reuters.com','time.com','washingtonexaminer.com','news.sky.com','newsweek.com','thesun.co.uk',
'washingtonpost.com','france24.com','vox.com','coronavirusin.world','dutchnews.nl','nytimes.com','twitter.com','youtube.com',
'metro.co.uk','bloomberg.com','google.com','japantimes.co.jp','foxnews.com','financialnews.com']

###################################################################################
###################################################################################
#function that gathers related news for a given tittle or keywords
def fact_checking(char):
	api = PushshiftAPI()
	scraped_data = list(api.search_submissions(q=char,subreddit='worldnews',
		filter=['title', 'author', 'domain']))

	#we will keep just articles from N_trusted sources
	data_filter=[]
	for i in range (len(scraped_data)):
		if scraped_data[i][2] in N_trusted:
			data_filter.append(scraped_data[i])

	#we create a data_base after collecting data
	file = pd.DataFrame([thing.d_ for thing in data_filter])
	file.to_csv('data.csv')
	return data_filter

###############################################################################
###############################################################################
#We will analyse a tittle and take keywords
#Tokenising tittle
def tokens(tittle):
	doc = nlp(tittle)
	return doc
#Remove non essentials words
def tittle_keywords(tittle):
	tittle_tokens = tokens(tittle) 
	keywords=[]
	for token in tittle_tokens:
		if token.text not in stopWords:
			keywords.append(token)
	return keywords

def sentence_mean(sentence):
	doc = nlp(sentence)
	return np.mean([(X.vector) for X in doc],axis=0)

####################################################################################
####################################################################################
#Thanks to the number of N_trusted sources dealing with a information we will give a score to the new
def fact_checking_score(char):
	keywords = tittle_keywords(char)
	keywords_tittle=""
	for words in keywords:
		keywords_tittle += words.text+" "
	n_list = fact_checking(keywords_tittle)
	token_tittle = tokens(keywords_tittle)
	N = len(n_list)
	if N==0:
		return 0
	score =0
	#We count how many n_trusted sites released the information
	for i in range (len(n_list)):
		t_keywords=""
		tittle_i =tittle_keywords(n_list[i][3])
		for words in tittle_i:
			t_keywords += words.text + " "
		t_keywords =tokens(t_keywords)
		score += token_tittle.similarity(t_keywords)
	#we take the average score
	score = score/N
	return score*100





