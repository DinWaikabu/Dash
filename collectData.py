#Load Package
import pandas as pd 
import numpy as np 
import psycopg2 as psy
from twitterscraper import query_tweets
#collect data from twitter

tweets = query_tweets("Anis Baswedan", 10)

for tweet in tweets:
    print(tweets)

#load data database