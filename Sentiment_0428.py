from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
analyzer=SentimentIntensityAnalyzer()
#!{sys.executable} -m pip install textblob
#!{sys.executable} -m pip install vaderSentiment
import os
import sys
import codecs
import nltk
import csv

os.getcwd()
os.chdir('G:/My Drive/BAN 675/Group Project')

prevDate    = 0
noOfDay     = 0
scoreSum    = 0
dateCol     = 7
tweetCol    = 3
dateColDeath= 2
newDeathCol = 6
prevScore   = 0
prevDeath   = 0
tweeterDict = {}
newDeathDict= {}
analyze_file = "CovidTweetRefined_02.csv"
deathGrowth_file= "DeathRateGrowth.csv"

with codecs.open(analyze_file, 'r', encoding=u'utf-8', errors='ignore') as fsentiment:
    csvReader = csv.reader(fsentiment, delimiter=',')
    rowId = -1
    for row in csvReader:
        rowId = rowId + 1
        if rowId == 0:
            continue   # skip header row
        else:
            if rowId == 1:
                prevDate = row[dateCol]
                
            if prevDate != row[dateCol]:
                tweeterDict[prevDate] = scoreSum / noOfDay
                noOfDay = 1
                scoreSum = 0
            else:
                noOfDay = noOfDay + 1
            prevDate = row[dateCol]
            score = analyzer.polarity_scores(row[tweetCol])
            scoreSum = scoreSum + score['compound']
    
    tweeterDict[row[dateCol]] = scoreSum / noOfDay

with codecs.open(deathGrowth_file, 'r', encoding=u'utf-8', errors='ignore') as fDeath:
    csvReader = csv.reader(fDeath, delimiter=',')
    for row in csvReader:
        if row[dateColDeath] in tweeterDict:
            newDeathDict[row[dateColDeath]] = row[newDeathCol]    

    count = 0
    print("\nDate\tCompound Sentiment   Rating  % Change  New Death  % Change")
    for d in tweeterDict:
        count = count + 1;
        if tweeterDict[d] >= 0.05:
            status = 'Positive'
        elif tweeterDict[d] <= -0.05:
            status = 'Negative'
        else:
            status = 'Neutral '

        if d in newDeathDict:        
            if count == 1:
                print(d, '{:>13.3f}'.format(tweeterDict[d]*100),'%', status, '      N/A',
                      '{:>10}'.format(newDeathDict[d]), '      N/A')
            else:
                print(d, '{:>13.3f}'.format(round(tweeterDict[d]*100, 2)),'%', status, 
                      '{:>9.3f}'.format((tweeterDict[d]-prevScore)/prevScore*100),
                      '{:>10}'.format(newDeathDict[d]), '{:>9.2f}'.format((int(newDeathDict[d])-int(prevDeath))/int(prevDeath)*100))
            prevScore = tweeterDict[d]
            prevDeath = newDeathDict[d]
            
fsentiment.close()
fDeath.close()