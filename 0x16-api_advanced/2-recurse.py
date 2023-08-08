#!/usr/bin/python3
"""Script that returns a list containing titles of hot articles"""


import requests
import time


def recurse(subreddit, hot_list=[], after=""):
    """recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit"""
    api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0"
    headers = {"User-Agent": userAgent}
    client = requests.session()
    client.headers = headers
    parameters = {"limit": 100, "after": after}
    resp = client.get(api_url, params=parameters)

    if resp.status_code == 200:
        after = resp.json().get("data").get("after")
        for hot in resp.json().get("data").get("children"):
            hot_list.append(hot.get("data").get("title"))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
