'''
Maintains a file todo.txt, each line is a task.
Script allows user to:
Add a task
List tasks with numbering
Mark a task as done (for simplicity: remove or annotate)
Write changes back to file.
'''

# Create simple GUI
def menu() -> int:
    print("Hello, what would you like to do?\n")
    print("1. Display To-Do list")
    print("2. Add Task")
    print("3. Edit Task")
    print("4. Delete Task")
    print("5. Quit")
    choice = input("Enter choice: ")

    return choice

# Displays the text file
def display() -> None:
    with open(r"Python Basic Project\Task Manager CLI\to-do.txt", "rt") as f:
        f.seek(0)
        print(f"\nTo Do List:\n{f.read()}\n")
    return None

# Adds a task
def add_task():
    task_input = input("Input task: ")

    with open(r"Python Basic Project\Task Manager CLI\to-do.txt", "rt") as f:
        task_list = [ line.strip() for line in f ]
    
    if task_input.lower() in ( t.lower() for t in task_list ):
        print("\nTask already exists!")
        return
    
    with open(r"Python Basic Project\Task Manager CLI\to-do.txt", "at") as f:
        f.write('\n' + task_input)
        print("\nTask added succesfully!")

    return None

def edit_task():
    with open(r"Python Basic Project\Task Manager CLI\to-do.txt", "rt") as f:
        i = 1
        print('\n')
        for line in f:
            print(f"{i}. {line.strip()}")
            i += 1
        f.seek(0)
        task_list = [ line.strip() for line in f ]

    print("\nWhich task would you like to edit?")
    while True:
        task_line_str = input("Enter line number: ")

        try:
            task_line = int(task_line_str) - 1
        except ValueError:
            print("Please enter a number!")
            continue

        if task_line < 0 or task_line > len(task_list) - 1:
            print(f"Please enter a number between 1-{len(task_list)}!")
            continue
        break

    if "Completed" in task_list[task_line]:
        print(f"\nMark \"{task_list[task_line][:-12]}\" as uncompleted?")
        while True:
            choice = input("Y/N: ").lower()
            if choice != 'y' and choice != 'n':
                print("Not a choice, please enter 'Y' or 'N'")
                continue
            break
            
        if choice == 'y':
            task_list[task_line] = task_list[task_line][:-12]
            print(f"\n\"{task_list[task_line]}\" marked as uncompleted!")
        else:
            return
        
    else:
        print(f"\nMark \"{task_list[task_line]}\" as completed?")
        while True:
            choice = input("Y/N: ").lower()
            if choice != 'y' and choice != 'n':
                print("Not a choice, please enter 'Y' or 'N'")
                continue
            break

        if choice == 'y':
            task_list[task_line] += " - Completed"
            print(f"\n\"{task_list[task_line][:-12]}\" marked as completed!")
        else:
            return
    
    with open(r"Python Basic Project\Task Manager CLI\to-do.txt", "wt") as f:
            f.write('\n'.join(task_list))

    return

def delete_task():
    return None

while True:
    choice_str = menu()

    # Debug thing I learned
    try:
        choice = int(choice_str)
    except ValueError:
        print("\nPlease enter a number.\n")
        continue

    match choice:
        case 1:
            display()
        case 2:
            add_task()
        case 3:
            edit_task()
        case 4:
            delete_task()
        case 5:
            break
        case _:
            print("\nNot a choice, please try again!\n")
