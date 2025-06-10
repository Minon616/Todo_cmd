from Todo_oop import TodoList

def main():
    todo = TodoList()

    while True:
        print('=================')
        print('1. Add Task')
        print('2. Remove Task')
        print('3. Display Task')
        print('4. Exit')
        print('==================')

        choice = input('Enter choice: ')

        if choice == '1':
            task = input('Enter Task: ')
            todo.add_task(task)

        elif choice == '2':
            todo.display_list()
            try:
                index = int(input('Enter the number of task to be removed: '))
                todo.remove_task(index)
            except ValueError:
                print('Enter a valid number')

        elif choice == '3':
            todo.display_list()

        elif choice == '4':
            print('Exiting....')
            break

        else:
            print('Invalid input. Try again:')

main()
