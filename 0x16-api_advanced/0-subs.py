#!/usr/bin/python3
"""
this script  queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API and returns the number of subscribers"""
    headers = {'User-agent': 'Eleazarovich'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get('data', {}).get('subscribers', 0)
    else:
        return 0
