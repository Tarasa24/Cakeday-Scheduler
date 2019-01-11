import praw
import json
import time

with open('../config.json') as f:
    config = json.load(f)

reddit = praw.Reddit(client_id=config['client_id'],
                     client_secret=config['client_secret'],
                     password=config['password'],
                     user_agent='Cakeday scheduler by /u/Tarasa24_CZE',
                     username=config['username'])


def post_image_URL(title, subreddit, url):
    reddit.subreddit(subreddit).submit(title, url=url)
    print("{}\n{}\n\nSuccessfully posted to {}".format(title, url, subreddit))

def created(name):
    user = reddit.redditor(name)
    return user.created_utc
