#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    userId = argv[1]
    user = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
    todo = "https://jsonplaceholder.typicode.com/todos?userId={}".format(userId)
    
    user_info = requests.get(user).json()
    todos_info = requests.get(todo).json()

    employee_name = user_info["name"]
    task_completed = list(filter(lambda obj: (obj["completed"] is True), todos_info))
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, number_of_done_tasks, total_number_of_tasks))
    [print("\t " + task["title"]) for task in task_completed]
