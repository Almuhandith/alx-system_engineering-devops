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

    response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
    tasks = json.loads(response.text)

    response = requests.get("{}/users/{}".format(base_url, employee_id))
    employee = json.loads(response.text)
    employee_name = employee['name']
    employee_username = employee['username']

    filename = "{}.csv".format(employee_id)
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            writer.writerow([employee_id, employee_username, task['completed'], task['title']])

        print("Employee {} TODO list progress has been exported to {}.".format(employee_name, filename))
