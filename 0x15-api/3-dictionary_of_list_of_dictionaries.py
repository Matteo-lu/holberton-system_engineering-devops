#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
    returns information about his/her TODO list progress"""


if __name__ == "__main__":
    import json
    import requests

    user_info = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    task_info = requests.get(
        'https://jsonplaceholder.typicode.com/todos')

    user_list = user_info.json()
    tasks_list = task_info.json()

    full_dict = {}
    for user in user_list:
        user_id = user['id']
        tasks_element = []
        for task in tasks_list:
            task_dict = {}
            if user_id == task['userId']:
                task_dict['username'] = user['name']
                task_dict['task'] = task['title']
                task_dict['completed'] = task['completed']
                tasks_element.append(task_dict)
        full_dict[str(user_id)] = tasks_element

    with open('todo_all_employees.json', 'w', encoding='UTF8') as f:
        json.dump(full_dict, f)
