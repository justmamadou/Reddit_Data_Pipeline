import sys

import praw
from praw import Reddit


def connect_to_reddit(client_id, secret, user_agent) -> Reddit:
    try:
        reddit = praw.Reddit(client_id=client_id,
                             client_secret=secret,
                             user_agent=user_agent)
        print("Connected to Reddit.")
        return reddit
    except Exception as e:
        print(e)
        sys.exit(1)

def extract_posts(reddit_instance: Reddit, subreddit: str, time_filter: str, limit=None):
    subreddit = reddit_instance.subreddit(subreddit)
    posts = subreddit.top(time_filter= time_filter, limit=limit)

    posts_lists = []

    print(posts)
    #for post in posts:
