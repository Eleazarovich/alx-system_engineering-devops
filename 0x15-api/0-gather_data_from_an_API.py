#!/usr/bin/python3
"""
this script uses the JSONPlaceholder REST API for a given employee ID
returns information about his/her TODO list progress
"""
import requests
import sys


url = "https://jsonplaceholder.typicode.com/"
user_id = sys.argv[1]
user = requests.get(f'{url}users/{user_id}').json()
todos = requests.get(f'{url}todos', params={"userId": user_id}).json()

response = []
for title in todos:
    if title.get("completed") is True:
        response.append(title.get("title"))

print(f"Employee {user.get('name')} is done with tasks({len(response)}/\
{len(todos)}):")
for i in response:
    print("\t", i)
