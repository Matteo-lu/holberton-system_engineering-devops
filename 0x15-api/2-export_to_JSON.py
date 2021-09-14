#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress"""


if __name__ == "__main__":
    import json
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

    name_task = {}
    data = {}
    my_list = []
    for task in tasks_list:
        data['task'] = task['title']
        data['completed'] = task['completed']
        data['username'] = user_dict['username']
        my_list.append(data)
        name_task[str(user_id)] = my_list

    with open(user_id + '.json', 'w', encoding='UTF8') as f:
        json.dump(name_task, f)
