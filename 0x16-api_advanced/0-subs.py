#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries the Reddit API
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    data = requests.get(url, headers={'User-agent': 'Eleazarovich'})

    if data.status_code == 200:
        return data.json().get('data').get('subscribers')
    else:
        return 0
