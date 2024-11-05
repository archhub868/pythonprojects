# Simple To-Do List in Python

# Define an empty list to hold tasks
my_list = []


# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove a Task")
    print("4. Exit")



# Function to add a task to the list
# def add_task():
#     task = input("Enter the number of tasks that you want to add: ")
#     my_list.append(task)
#     print(f'Task "{task}" has been added to the list.')
# Function to add one or more tasks to the list

#Updated funtcion to add multiple tasks in the list


def add_task():
    tasks = input("Enter the tasks you want to add, separated by commas: ")
    # Split the input string by commas and strip any extra spaces from each task
    task_list = [task.strip() for task in tasks.split(',')]
    
    # Add each task to the todo_list
    for task in task_list:
        my_list.append(task)
        print(f'Task "{task}" has been added to the list.')


        
# Function to view all tasks in the list


def view_tasks():
    if not my_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(my_list, start=1):
            print(f"{index}. {task}")


# Function to remove a task from the list


def remove_task():
    view_tasks()
    if my_list:
        try:
            task_number = int(input("Enter the number of the task to remove: "))
            removed_task = my_list.pop(task_number - 1)
            print(f'Task "{removed_task}" has been removed from the list.')
        except (ValueError, IndexError):
            print("Invalid task number. Please try again.")


# Main loop
while True:
    display_menu()
    choice = input("\nEnter your choice (1-4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting My List. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

