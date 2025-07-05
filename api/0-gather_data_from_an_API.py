#!/usr/bin/python3
"""Fetches and displays TODO list progress of an employee using REST API"""

import requests
import sys


def fetch_employee_todos(employee_id):
        """Fetch employee name and tasks from the JSONPlaceholder API"""
            base_url = 'https://jsonplaceholder.typicode.com'
                user_url = f'{base_url}/users/{employee_id}'
                    todos_url = f'{base_url}/todos?userId={employee_id}'

                        user_response = requests.get(user_url)
                            todos_response = requests.get(todos_url)

                                employee_name = user_response.json().get('name')
                                    todos = todos_response.json()

                                        total_tasks = len(todos)
                                            done_tasks = [task for task in todos if task.get('completed')]

                                                print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
                                                    for task in done_tasks:
                                                                print(f"\t {task.get('title')}")


                                                                if __name__ == "__main__":
                                                                        if len(sys.argv) != 2:
                                                                                    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
                                                                                            sys.exit(1)
                                                                                                employee_id = int(sys.argv[1])
                                                                                                    fetch_employee_todos(employee_id)
