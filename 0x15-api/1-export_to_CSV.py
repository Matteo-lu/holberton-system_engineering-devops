#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress"""


import csv
import requests
import sys

user_id = sys.argv[1]

payload = {'userId': user_id}
user_info = requests.get(
    'https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
task_info = requests.get(
    'https://jsonplaceholder.typicode.com/todos', params=payload)

user_dict = user_info.json()
tasks_list = task_info.json()

name_task = []
data = []
user_name = user_dict['name']
for task in tasks_list:
    task_name = task['completed']
    task_title = task['title']
    data = [user_id, user_name, task_name, task_title]
    name_task.append(data)

with open(user_id + '.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerows(name_task)
