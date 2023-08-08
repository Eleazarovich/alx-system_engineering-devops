#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    data = requests.get(url, headers={'User-agent': 'Eleazarovich'},
                        allow_redirects=False)

    if data.status_code == 200:
        count = 0
        title_list = data.json().get('data').get('children')
        for title in title_list:
            if count == 10:
                break
            print(title.get('data').get('title'))
            count += 1
    else:
        print("None")
