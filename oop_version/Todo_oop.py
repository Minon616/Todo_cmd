class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'{task} Added successfully')

    def remove_task(self, index):
        self.display_list()
        #index -= 1  # Convert to 0-based index
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
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
        print()
