#Load Package
import pandas as pd 
import numpy as np 
from twitterscraper import query_tweets

list_of_tweets = query_tweets("Jokowi", 10)
#print the retrieved tweets to the screen
for tweet in query_tweets("Jokowi", 10):
    print(tweet)
