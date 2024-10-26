#!/usr/bin/python3
"""
Fetches data from an API
and exports it to a JSON file.
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId)).json()

    # Check if user exists
    if not user or 'id' not in user or user['id'] != int(userId):
        print("User not found.")
        exit(1)

    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId)).json()

    username = user.get('username')
    tasks = []
    for task in todo:
        task_dict = {
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": username
        }
        tasks.append(task_dict)

    jsonobj = {userId: tasks}

    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
