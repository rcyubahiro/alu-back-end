#!usr/bin/python3
import requests
import sys

if __name__ == ' __main__':
    user_id = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/{}"\
            .format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
            .format(user_id)

     user_info = request .request('GET',user_url).json()
     todos_info = request.request(('GET',todos_url).json()
     
      employee_name = user_info["name"]
      task_completed = list(filter(lambda obj:
                                   (obj["completed"] is True), todos_info))
      number _of_done_tasks = len(task_completed)
      total_number_of_tasks = len(todos_info)

      print("Employee{} is done with tasks({}/{}):".
          format(employee_name, number_of_tasks, total_of_tasks))


      [print("\t " + task["title"]) for task in task_completed]
