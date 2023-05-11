#!/usr/bin/python3
"""Function that prints the titles of first 10 posts"""
import requests


def top_ten(subreddit):
    """Returns first 10 posts listed in a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for entry in data.get("children"):
            print(entry.get("data").get("title"))
    else:
        print("None")
        return
