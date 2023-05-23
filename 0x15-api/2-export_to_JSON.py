#!/usr/bin/python3
"""
this script uses the JSONPlaceholder REST API for a given employee ID
returns information about his/her TODO list progress
"""
import json
import requests
import sys


def main():
    """main entry of the program"""
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(f'{url}users/{user_id}').json()
    todos = requests.get(f'{url}todos', params={"userId": user_id}).json()
    username = user.get("username")
    data = {
            user_id: [
                {
                    "tasks": title.get("title"),
                    "completed": title.get("completed"),
                    "username": username
                } for title in todos
                ]
            }

    with open(f"{user_id}.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == "__main__":
    """this code will not execute when imported"""
    main()
