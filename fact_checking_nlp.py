import spacy
import pytextrank
####################################

####################################
#Library for API searchs
from psaw import PushshiftAPI
from newsapi import NewsApiClient
#Init
newsapi = NewsApiClient(api_key='4e18ca1d616e42348999bdee41f66a36')
####################################
import csv
import numpy as np 
####################################
import mechanize
from mechanize import Browser 
from manage_class import *
# example text
#text = "Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types systems and systems of mixed types."
#atext ="Boris Johnson has been tested positve to coronavirus "
# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_sm")

# add PyTextRank to the spaCy pipeline
tr = pytextrank.TextRank()
nlp.add_pipe(tr.PipelineComponent, name="textrank", last=True)

#Our N_trusted list 
N_trusted='nbcnews.com,in.reuters.com,bbc.co.uk,theguardian.com,reuters.com,edition.cnn.com,cbc.com,nationalpost.com,independent.co.uk,cnn.com,uk.reuters.com,time.com,washingtonexaminer.com,news.sky.com,newsweek.com,thesun.co.uk,washingtonpost.com,france24.com,vox.com,coronavirusin.world,dutchnews.nl,nytimes.com,twitter.com,metro.co.uk,bloomberg.com,google.com,japantimes.co.jp,foxnews.com,financialnews.com,edition.cnn.com'

###################################################################################
###################################################################################
#function that gathers related news for a given title or keywords
def data_scraping(char):
	#scraped_data = newsapi.get_everything(q=char,language='en',domains=N_trusted,page=3)
	api = PushshiftAPI()
	scraped_data = list(api.search_submissions(q=char,subreddit='worldnews',
		filter=['title', 'domain'],limit=500))

	#Building database
	data =[] 
	n = len(scraped_data)
	print(n)
	for i in range (n):
		if scraped_data[i][1] in N_trusted:
			data.append(news(headline=scraped_data[i][2],domain=scraped_data[i][1]))
	return data

####################################################################################
####################################################################################
#Thanks to the number of N_trusted sources dealing with a information we will give a score to the new
def score(nlp_title,database):
	#Tokenize the title
	N = len(database)
	if N==0:
		return 0
	score =0
	#We count how many n_trusted sites released the information
	for title in database:
		title_test_tokens= nlp(title.headline)
		#we evaluate the similarity between headlines
		score += nlp_title.similarity(title_test_tokens)
	#we take the average score
	score = score/N
	return score*100

def fact_checking_score_url(url):
	br = Browser()
	try:
		br.open(url)
		article_title = br.title()
		print(article_title)
		return fact_checking(article_title)
	except mechanize._mechanize.BrowserStateError:
		raise(not_a_link())
	
	
def fact_checking(title):
	if (len(title) >0):
		title_nlp = nlp(title)
		keywords = ""
		n = len(title_nlp._.phrases)
		i=0
		for words in title_nlp._.phrases:
			keywords += words.text +" "
		dataset=data_scraping(keywords)
		return(score(title_nlp,dataset))
	else:
		print("Your input is invalid please give us a title")
		raise(invalid_input())


	
		
