# This is a Todo list
# This project will be implemented in the future 
# Phase 01 : 

Todo_list = []

print("********SYSTEM START********")

def add_task():
    task = input('Enter a task: ')
    Todo_list.append(task)
    print()
    print(f'{task} Added successfully')
    

def remove_task():
    display_list()
    task_index = int(input('Enter task to be removed: '))

    if 1 <= task_index <= len(Todo_list):
        Todo_list.pop(task_index -1)
        print()
        print(f'{task_index}. Removed successfully')
    else:
        print('task not found')    

def display_list():
    if not Todo_list:
        print('Todo list is empty')
        return

    print('\n Your Todo list')
    for index,task in enumerate(Todo_list, start = 1):
        print(f'{index}.{task}')   
        #print()
def exit_programme():
    print('Exitting...')
    exit()


while True:
    print()
    print('1. Add task')
    print('2. Remove task')
    print('3. Display list')
    print('4. Exit')
    print('==============================')
    choice = input('Enter a choice: ')

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        display_list()
    elif choice == '4':
        exit_programme()
    else:
        print('Invalid input:')                





    
