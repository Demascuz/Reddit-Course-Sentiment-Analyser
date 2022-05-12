import pandas as pd
import numpy as np

# misc
import datetime as dt
from pprint import pprint
from itertools import chain

# reddit crawler
import praw

# sentiment analysis
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize, RegexpTokenizer # tokenize words
from nltk.corpus import stopwords

# visualization
import matplotlib.pyplot as plt
#%matplotlib inline!!! need to delete at end
plt.rcParams["figure.figsize"] = (10, 8) # default plot size
import seaborn as sns
sns.set(style='whitegrid', palette='Dark2')
from wordcloud import WordCloud


#nltk.download('vader_lexicon') # get lexicons data
#nltk.download('punkt') # for tokenizer
#nltk.download('stopwords')

r = praw.Reddit(user_agent='DemApollus',
                client_id='KrnUePjuO_J50XuOWNIyRw',
                client_secret='OswzYFW1nBcQWSfZPQVHmOXRglUcvw',
                check_for_async=False)

subreddit = r.subreddit('technews')

news = [*subreddit.top(limit=None)] # top posts all time

print(len(news))