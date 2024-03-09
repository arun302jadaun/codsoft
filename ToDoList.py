


tasks = []

def add_task():
    task = input("Enter a new task : ")
    tasks.append(task)
    print("Task added successfully. ")

def view_task():
    if len(tasks)==0:
        print("No task. ")
    else:
        print("List of task. ") 
        for i,task in enumerate(tasks):
            print(f'{i+1}.{task}')


def delete_task():

    if len(tasks)==0:
        print("No task to delete.")
    else:
        print("Tasks: ")
        for i, task in enumerate(tasks):
            print(f'{i+1}. {tasks}')
        choice = int(input("enter the task number to delete:"))

        if 0< choice <= len(tasks):
            del tasks[choice-1]
            print("Task deleted successfully. ")
        else:
            print("Invalid task number.")


def main():
    while True:
        print("\n===== To-Do-List Application=====")
        print("1. Add Task")
        print("2. View task")
        print("3. Delete task")
        print("4. Quit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thank You For Using the To-Do-List Application. ")
            break
    else:
        print('Invalid choice. Please try again.')


if __name__=="_main_":
    main()                                                               
