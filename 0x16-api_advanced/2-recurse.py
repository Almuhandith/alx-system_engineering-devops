#!/usr/bin/python3
"""A recursive function that returns the tittles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Returns a list of the titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot/.json?after={}".format(subreddit, after)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"after": after, "limit": 100}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        after = results.get("after")
        for entry in results.get("children"):
            hot_list.append(entry.get("data").get("title"))

        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    return None
