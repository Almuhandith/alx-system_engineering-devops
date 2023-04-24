#!/usr/bin/python3
"""Script that export data in the CSV format"""
import csv
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

    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([employee_id, employee_username, task['completed'], task['title']])

        print(f"Employee {employee_name} TODO list progress has been exported to {filename}.")
