#!/usr/bin/python3
"""Script to print the titles of first 10 hot posts"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints titles of the
first 10 hot posts listed for a given subreddit"""
    api_url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    userAgent = "Mozilla/5.0"
    limits = 10

    resp = requests.get(api_url, headers={"user-agent": userAgent},
                        params={"limit": limits})
    if not resp:
        print('None')
        return
    resp = resp.json()
    list_obj = resp['data']['children']
    for obj in list_obj:
        print(obj['data']['title'])
    return
