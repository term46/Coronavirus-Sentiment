# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 09:45:50 2020

@author: Stephen
"""
import numpy as np
import matplotlib.pyplot as plt
from twitterscraper.query import query_tweets
import datetime as dt
import pandas as pd
import os
import re
import nltk
from nltk.corpus import stopwords


from nltk.stem.porter import PorterStemmer

begin_date = dt.date(2020, 4, 17)
end_date = dt.date(2020, 4, 18)
limit = 500000
lang = 'en'


#do it on Trump and Coronavirus
#tweets = query_tweets('Trump (Covid OR Coronavirus OR Covid-19 OR Covid19)', begindate = begin_date, enddate=end_date, limit=limit, lang=lang)
tweets = query_tweets('coronavirus', begindate = begin_date, enddate=end_date, limit=limit, lang=lang)

df = pd.DataFrame(t.__dict__ for t in tweets)
df.to_csv('G:/My Drive/BAN 675/CovidApril17v2.csv', header=True)

#13658 april 17

#tweets = query_tweets('coronavirus', begindate = begin_date, enddate=end_date, limit=limit, lang=lang)

#df = pd.DataFrame(t.__dict__ for t in tweets)
#df.to_csv('G:/My Drive/BAN 675/TweetsCovid99.csv', header=True)


# =============================================================================
# os.chdir('G:/My Drive/BAN 675')
# 
# with open("Tweets.csv", 'r', encoding="utf-8") as f:
#     corpus =[]
#     for i in range(0, 1000):
#         review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
#         review = review.lower()
# =============================================================================
