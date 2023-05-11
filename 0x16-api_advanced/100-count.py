#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, kwargs={}, after=None):
    url = "https://www.reddit.com/r/{}/hot/.json?after={}".format(subreddit, after)
    headers = {"User-Agent": "custom"}
                
    data = requests.get(url, headers=headers, allow_redirects=False)
    if data.status_code == 200:
        after = data.json().get("data").get("after")
        data = data.json().get("data").get("children")
        for entry in data:
            parse_list = entry.get("data").get("title").lower().split()
            for word in parse_list:
                for element in word_list:
                    if word == element:
                        if element in kwargs:
                            kwargs[element] += 1
                        else:
                            kwargs[element] = 1

        if after:
            count_words(subreddit, word_list, kwargs, after)
        else:
            sorted_dict = {k: v for k, v in sorted(kwargs.items(), key=lambda item: item[1], reverse=True)}
            [print("{}: {}".format(k, v)) for k, v in sorted_dict.items()] 
    else:
        return (None)
