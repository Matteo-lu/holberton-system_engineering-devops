#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress"""


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

done_counter = 0
tasks_counter = 0
name_task = []
for task in tasks_list:
    if task['completed'] is True:
        done_counter += 1
        name_task.append(task['title'])
    tasks_counter += 1

print('Employee {} is done with tasks({}/{}):'.format(
    user_dict['name'], done_counter, tasks_counter))

for title in name_task:
    print('\t{}'.format(title))
