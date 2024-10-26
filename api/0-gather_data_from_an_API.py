#!/usr/bin/python3
"""
Module to fetch and display tasks for a specific employee from the
JSONPlaceholder API based on their user ID.
"""

import requests
from sys import argv

if __name__ == "__main__":
    userId = argv[1]
    user_url = (
        "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    )
    todo_url = (
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(userId)
    )

    # Fetch user information and tasks
    user_info = requests.get(user_url).json()
    todos_info = requests.get(todo_url).json()

    # Extract employee name and completed tasks
    employee_name = user_info.get("name", "Unknown Employee")
    completed_tasks = [task for task in todos_info if task["completed"]]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_info)

    # Print results
    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_number_of_tasks
        )
    )

    for task in completed_tasks:
        print("\t {}".format(task["title"]))
