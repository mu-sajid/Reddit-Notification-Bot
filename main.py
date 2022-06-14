import praw
import config
import random
import os
from twilio.rest import Client


'''         Log into bot, separate config file with username, password, client_id, client_secret.
            Comments intended to ensure each individual step works.  '''

def bot_login():
    print("Logging in...")
    r = praw.Reddit(username = config.username, password = config.password,
            client_id = config.client_id, client_secret = config.client_secret,
            user_agent = "Test")
    #print("Logged in,", config.username)
    return r


'''         Reply to a specific comment in 'r/test' if a keyword is found. Sends a text message using trilio
            if comment is found. '''

def run_bot(r):
    client = Client("AC214217b8d532d28159434b6ef9c5bae8", '035f5e197ef4464bdcb0e8b37641d272')
    #print("Finding any comments with keyword")
    for comment in r.subreddit('test').comments(limit=100):
        if "dog" in comment.body:
            #print("Found comment with word 'dog'. Replying..")
            comment.reply("Found dog")
            client.messages.create(to="+19174365675", 
                       from_="+18573758560", 
                       body="Dog found on r/test")
            #print("Replied to comment " + comment.id)

r = bot_login()
run_bot(r)