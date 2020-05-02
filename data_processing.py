#Here we will try to create a database of N-trusted sites

#Library for scraping data from websites
from psaw import PushshiftAPI



#Classic libraries
import pandas as pd 
 
#Our N_trusted list 
N_trusted=['nbcnews.com','in.reuters.com','bbc.co.uk','theguardian.com','reuters.com','edition.cnn.com','cbc.com','nationalpost.com','independent.co.uk','cnn.com','uk.reuters.com','time.com','washingtonexaminer.com','news.sky.com','newsweek.com','thesun.co.uk','washingtonpost.com','france24.com','vox.com','coronavirusin.world','dutchnews.nl','nytimes.com','twitter.com','youtube.com','metro.co.uk','bloomberg.com','google.com','japantimes.co.jp','foxnews.com','financialnews.com']

def data_scarping(subreddit):
    api = PushshiftAPI()

    # Create list of data
    scrape_list = list(api.search_submissions(subreddit=subreddit,
                                filter=['title', 'subreddit', 'num_comments', 'author', 'subreddit_subscribers', 'score', 'domain', 'created_utc'],
                                limit=10000))

    #Filter list to only show Subreddit titles and Subreddit category 
    clean_scrape_lst = []
    for i in range(len(scrape_list)):
        scrape_dict = {}
        scrape_dict['subreddit'] = scrape_list[i][5]
        scrape_dict['author'] = scrape_list[i][0]
        scrape_dict['domain'] = scrape_list[i][2]
        scrape_dict['title'] = scrape_list[i][7]
        scrape_dict['num_comments'] = scrape_list[i][3]
        scrape_dict['score'] = scrape_list[i][4]
        scrape_dict['timestamp'] = scrape_list[i][1]
        #We just keep news from N_trusted sources
        if (scrape_dict['domain'] in N_trusted):
            clean_scrape_lst.append(scrape_dict)

    # Return list of data
    return clean_scrape_lst


def data_base():
    #Here we create a data Frame
    # worldnews is the greates news center in Reddit with millions of user that's why we choose it for a start
    df = pd.DataFrame(data_scarping('worldnews'))
    #Save data in csv format
    df.to_csv('./database.csv')
    print(f'df shape:{df.shape}')
    df.head()