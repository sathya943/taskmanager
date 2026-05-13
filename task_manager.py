# Python Taskmanager
def task_manager():
    tasks = []
    while True:
        # Display available options
        if len(tasks) == 0:
            print("No tasks to display.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")

def list_tasks():
    pass


# Main function
print(task_manager())


