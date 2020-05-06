import requests
import csv
import pandas as pd 
####################################
#Library to take a tittle thanks to its url
from mechanize import Browser 

####################################
#Library for API searchs
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
#function that gathers related news for a given title or keywords
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
#We will analyse a title and take keywords
#Tokenising title
def tokens(title):
	doc = nlp(title)
	return doc
#Remove non essentials words
def title_keywords(title):
	title_tokens = tokens(title) 
	keywords=[]
	for token in title_tokens:
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
	keywords = title_keywords(char)
	keywords_title=""
	for words in keywords:
		keywords_title += words.text+" "
	print(keywords_title)
	n_list = fact_checking(keywords_title)
	token_title = tokens(keywords_title)
	N = len(n_list)
	if N==0:
		return 0
	score =0
	#We count how many n_trusted sites released the information
	for i in range (len(n_list)):
		t_keywords=""
		title_i =title_keywords(n_list[i][3])
		for words in title_i:
			t_keywords += words.text + " "
		t_keywords =tokens(t_keywords)
		score += token_title.similarity(t_keywords)
	#we take the average score
	score = score/N
	return score*100


########################################################################################
########################################################################################
#If user gives us an url instead of a title we have to first take the title from the url and then process

def fact_checking_score_url(url):
	br = Browser()
	br.open(url)
	title = br.title()
	return fact_checking_score(title)




