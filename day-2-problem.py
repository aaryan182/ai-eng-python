# Create class TodoList with features: add task delete task view tasks 
# mark completed count tasks

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add(self, task):
        self.tasks.append({"task": task, "done": False})
        
    def complete(self, index):
        self.tasks[index]["done"] = True
        
    def delete(self, index):
        self.tasks.pop(index)
        
    def show(self):
        for i, item in enumerate(self.tasks):
            status = "check" if item["done"] else 'not done'
            print(i, status, item["task"])