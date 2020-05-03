import requests
import csv
import pandas as pd 
from psaw import PushshiftAPI

 
###################################################################################
#function that gathers related news for a given tittle or keywords
def fact_checking(char):
	api = PushshiftAPI()
	scraped_data = list(api.search_submissions(q=char,subreddit='worldnews',
		filter=['title', 'author', 'domain']))
	#we create a data_base after collecting data
	file = pd.DataFrame([thing.d_ for thing in scraped_data])
	file.to_csv('data.csv')


####################################################################################

