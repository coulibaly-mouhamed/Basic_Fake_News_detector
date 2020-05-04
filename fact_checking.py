import requests
import csv
import pandas as pd 
from psaw import PushshiftAPI

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


####################################################################################
#Thanks to the number of N_trusted sources dealing with a information we will give a score to the new
def fact_checking_score(char):
	n_list = fact_checking(char)
	n =0
	sites=[]
	N = len(N_trusted)
	#We count how many n_trusted sites released the information
	for i in range (len(n_list)):
		if n_list[i][2] not in sites:
			sites.append(n_list[i][2])
			n +=1
	if n>(N/3):
		return 100
	return n/N*100



