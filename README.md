# Coronavirus-Sentiment

This project aims to see if there is a correlation between the # of new deaths per day from the coronavirus and the sentiment of the tweets about the virus.

Twitter file:
This is a python file that takes the Twitter API to pull tweets about the coronavirus.
We were only allowed to pull 5000 tweets at a time, so it took us multiple days to pull all the tweets for our dataset and then saved it all into a csv file.

Sentiment file:
This is a python file that uses the csv file of the tweets, then uses the vader library to calculate the sentiment of the tweets.

Correlation file:
We take a correlation of the # of new deaths posted on the CDC website and compared it to the sentiment of the coronavirus tweets.
