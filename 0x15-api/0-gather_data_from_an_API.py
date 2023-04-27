#!/usr/bin/python3
"""
A python script that retrieves and prints the
progress of an employee's TODO list
"""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    if len(sys.argv) != 2:
        print("Usage: python todo_list.py [employee_id]")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    response = requests.get("{}/todos?userId={}".format(base_url, employee_id))
    tasks = response.json()

    num_completed_tasks = sum(1 for task in tasks if task['completed'])
    total_num_tasks = len(tasks)

    response = requests.get("{}/users/{}".format(base_url, employee_id))
    employee = response.json()
    employee_name = employee['name']

    print("Employee {} is done with".format(employee_name), end=' ')
    print("tasks({}/{}):".format(num_completed_tasks, total_num_tasks))

    for task in tasks:
        if task['completed']:
            print("\t{}".format(task['title']))
