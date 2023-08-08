#!/usr/bin/python3
"""Script that returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and
    returns the number of subscribers"""
    api_url = "https://reddit.com/r/{}/about.json".format(subreddit)
    userAgent = "Mozilla/5.0"

    resp = requests.get(api_url, headers={"user-agent": userAgent})
    if not resp:
        return 0
    value = resp.json().get('data').get('subscribers')
    if value:
        return value
    else:
        return 0
