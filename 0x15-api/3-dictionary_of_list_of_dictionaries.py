#!/usr/bin/python3
""" Script that export data in the CSV format """
import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"


    response = requests.get(f"{base_url}/todos")
    tasks = json.loads(response.text)


    response = requests.get(f"{base_url}/users")
    users = json.loads(response.text)

    tasks_dict = {}
    for user in users:
        userid = user["id"]
        username = user["username"]
        usertasks = []
        for task in tasks:
            if task["userId"] == user_id:
                user_tasks.append({
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": username
                    })
        tasks_dict[user_id] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(tasks_dict, jsonfile)

    print(f"All tasks from all employees have been exported to {filename}.")
