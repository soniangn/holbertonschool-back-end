#!/usr/bin/python3
""" uses an API and for a given employee ID,
    returns information about his/her TODO list progress.
    Export data in the CSV format.
"""
import csv
import json
import requests
import sys


if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_id = f'https://jsonplaceholder.typicode.com/users/{USER_ID}'
    api_response_employee = requests.get(url_id)
    employee_json = api_response_employee.json()
    USERNAME = employee_json.get('name')

    url_tasks = f'https://jsonplaceholder.typicode.com/todos'
    api_response_tasks = requests.get(url_tasks)
    task_json = api_response_tasks.json()

    with open(f'{USER_ID}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in task_json:
            writer.writerow([USER_ID, USERNAME,
                             task.get('completed'), task.get('title')])
