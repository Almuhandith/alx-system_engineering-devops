#!/usr/bin/python3
"""Script that uses JSONPlaceholder API to get information about employee"""
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    if len(sys.argv) != 2:
        print("Usage: python todo_list.py [employee_id]")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    response = requests.get(f"{base_url}/todos?userId={employee_id}")
    tasks = response.json()

    num_completed_tasks = sum(1 for task in tasks if task['completed'])
    total_num_tasks = len(tasks)

    response = requests.get(f"{base_url}/users/{employee_id}")
    employee = response.json()
    employee_name = employee['name']

    print(f"Employee {employee_name} is done with", end=' ')
    print(f"tasks({num_completed_tasks}/{total_num_tasks}):")

    for task in tasks:
        if task['completed']:
            print(f"\t {task['title']}")
