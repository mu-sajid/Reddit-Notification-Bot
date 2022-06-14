import praw
import config
from twilio.rest import Client


'''         Log into bot, separate config file with username, password, client_id, client_secret.
            Comments intended to ensure each individual step works.  '''

def bot_login():
    r = praw.Reddit(username = config.username, password = config.password,
            client_id = config.client_id, client_secret = config.client_secret,
            user_agent = "Test")
    return r


'''         Reply to a specific comment in 'r/test' if a keyword is found. Sends a text message using trilio
            if comment is found. '''

def run_bot(r):
    client = Client("ACxxxxxxxxxxxxx", 'xxxxxxxxxxxxxxxx')              #Account SID / Auth Token
    for comment in r.subreddit('test').comments(limit=100):             
        if "dog" in comment.body:
            comment.reply("Found dog")
            client.messages.create(to="+1917xxxxxxxx",                  # To your phone num, from Twilio num
                       from_="+1857xxxxxxx", 
                       body="Dog found on r/test")

r = bot_login()
run_bot(r)