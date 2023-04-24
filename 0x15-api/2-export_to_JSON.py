#!/usr/bin/python3
""" Script that export data in the CSV format """
import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"


    if len(sys.argv) != 2:
        print("Usage: python todo_list.py [employee_id]")
        sys.exit(1)

    employee_id = int(sys.argv[1])


    response = requests.get(f"{base_url}/todos?userId={employee_id}")
    tasks = json.loads(response.text)


    response = requests.get(f"{base_url}/users/{employee_id}")
    employee = json.loads(response.text)
    employee_name = employee['name']
    employee_username = employee['username']

    tasks_dict = {"USER_ID": []}
    for task in tasks:
        tasks_dict["USER_ID"].append({
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_username
            })

    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(tasks_dict, jsonfile)

    print(f"Employee {employee_name} TODO list progress has been exported to {filename}.")
