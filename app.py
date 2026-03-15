from flask import Flask, request, jsonify
app =Flask(__name__)

class Task:
    def __init__(self):
        pass
        
    my_tasks = [{"id": 1, "title":"Development Software 4", "description":"Complete the project for DS4", "priority":"High", "status":"Completed"},
             {"id": 2, "title":"AI & Software Engineer Stack", "description":"Learn or practice concepts related to AI", "priority":"High", "status":"Pending"},
               {"id": 3, "title":"Read Research", "description":"Read at least one paper or article related to your research", "priority":"Medium", "status":"Pending"}, 
               {"id": 4, "title":"Self Presentation", "description":"Prepare and practice explaining yourself or your projects", "priority":"Low", "status":"Pending"}]
    
    def show_tasks(self):
        for task in Task.my_tasks:
            print(f"id: {task['id']}"),
            print(f"title: {task['title']}"),
            print(f"description: {task['description']}"),
            print(f"priority: {task['priority']}"),
            print(f"status: {task['status']}")


task = Task()


@app.route('/home')
def home():
    return "Welcome to the home page!"

@app.route('get_tasks', methods=['GET'])
def get_tasks():
    return jsonify({"My Tasks": task.show_tasks()})