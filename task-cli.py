import sys
import json
import os

TASKS_FILE = "tasks.json"
# function definitions
def load_tasks(): 
    if not os.path.exists(TASKS_FILE):
        return []
    
    with open(TASKS_FILE, "r") as file:
        return json.load(file)
    

def save_task(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=2)


def get_next_id(tasks):
    if len(tasks) == 0:
        return 1
    
    max_id = 0

    for task in tasks:
        if task["id"] > max_id:
             max_id = task["id"]

    return max_id + 1



command = sys.argv[1]

if command == "add":
    if len(sys.argv) < 3:
        print("Error: missing task description")
    else:
        description = sys.argv[2]
        tasks = load_tasks()
        task = {
            "id": get_next_id(tasks),
            "description": description,
            "status": "todo"
        }
        tasks.append(task)
        save_task(tasks)
        print("Task added successfully")
elif command == "list":
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks found")
    else: 
        for task in tasks:
            print(f'{task["id"]}. [{task["status"]}] {task["description"]}')
elif command == "delete":
    if len(sys.argv) < 3:
        print("Error: missing task ID")
    else:
        try:
            task_id = int(sys.argv[2])
            tasks = load_tasks()
            new_task = []
            for task in tasks:
                if task["id"] != task_id:
                    new_task.append(task)
            
            if len(new_task) == len(tasks):
                print("Error: task not found")
            else:
                 save_task(new_task)
                 print("Task deleted successfully")
        except ValueError:
            print("Error: task ID must be a number")
elif command == "update":
    if len(sys.argv) < 4:
        print("Error: missing task ID or description")
    else:
        try:
            task_id = int(sys.argv[2])
            new_description = sys.argv[3]

            tasks = load_tasks()
            found = False

            for task in tasks:
                if task["id"] == task_id:
                    task["description"] = new_description
                    found = True
            
            if found:
                save_task(tasks)
                print("Task updated successfully")
            else:
                print("Error: task not found")
        except ValueError:
            print("Error: task ID must be a number")

else:
    print("Unknown command:", command)