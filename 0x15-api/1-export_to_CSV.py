#!/usr/bin/python3
"""
this script uses the JSONPlaceholder REST API for a given employee ID
returns information about his/her TODO list progress
"""
import csv
import requests
import sys


def main():
    """main entry of the program"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f'{url}users/{user_id}').json()
    todos = requests.get(f'{url}todos', params={"userId": user_id}).json()
    username = user.get('username')
    
    with open(f"{user_id}.csv", "w", newline="") as csv_file:
        data = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for title in todos:
            data.writerow([user_id, username, title.get("completed"),\
                    title.get("title")])


if __name__ == "__main__":
    """this code will not execute when imported"""
    main()
