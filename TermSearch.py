#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 23:40:28 2021

@author: EmilioMartinez
"""

import os 
import tweepy 
import pandas as pd


# Authenticate to Twitter
twitter_authentication = tweepy.OAuthHandler("API Key", 
    "API Secret") #API Key, API Secret are generated 

twitter_authentication.set_access_token("Access Token", 
    "Access Token Secret") #Access Token, Access Token Secret are generated


#Create the api object,  this makes the api wait if the rate limit is reached and also prints a message if the rate limit is reached
api = tweepy.API(twitter_authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 


if api.verify_credentials(): 
    print("Authentication Succesful")
else:
    print("Authentication Unsucessful")


# Define the search term and the date_since date as variables 
term_to_search = "" #chose term to search
date_since = ""  #chose date since yyyy-m-d

#remove retweet from tweets that appear
filtered_search = term_to_search + " -filter:retweets" 

tweets = tweepy.Cursor(api.search, q=filtered_search,ang="en", since=date_since).items(8)

#create a list of tweets that are collected
all_tweets = [tweet.text for tweet in tweets]

#create data frame of these tweets
tweet_text = pd.DataFrame(data=all_tweets, 
                    columns=["tweet content"])


