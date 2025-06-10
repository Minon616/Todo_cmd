import json
import os

class TodoList:
    def __init__(self,file_path="task.json"):
        self.file_path = file_path
        self.tasks = []
        self.load_task()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_task()
        print(f'{task} Added successfully')

    def remove_task(self, index):
        self.display_list()
        #index -= 1  # Convert to 0-based index
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f'\n{removed} Removed successfully')
        else:
            print('Invalid task number')

    def display_list(self):
        if not self.tasks:
            print('List is empty')
        else:
            print('Your Todo list:')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task}')

    def save_task(self):
        try:
            with open (self.file_path,'w',encoding='utf-8' ) as f:
                json.dump(self.tasks, f, indent=2)
        except  Exception as e:
            print(f'value saved in task {e}')  

    def load_task(self):
         if os.path.exists(self.file_path):
             try:
                 with open(self.file_path, 'r', encoding='utf-8') as f:
                    self.tasks = json.load(f)
             except Exception as e:
                 print(f'Error loading tasks: {e}')
                 self.tasks = []
                     
        #print()
