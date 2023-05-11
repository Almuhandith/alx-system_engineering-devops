#!/usr/bin/python3
"""Function that prints the titles of first 10 posts"""

def top_ten(subreddit):
    """Returns first 10 posts listed in a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
