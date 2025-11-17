'''
Maintains a file todo.txt, each line is a task.
Script allows user to:
Add a task
List tasks with numbering
Mark a task as done (for simplicity: remove or annotate)
Write changes back to file.
'''

from pathlib import Path
script_dir = Path(__file__).parent.resolve()
todo_file = script_dir / "to-do.txt"

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
    with open(todo_file, "rt") as f:
        print(f"\nTo Do List:\n")
        i = 1
        for line in f:
            print(f"{i}. {line.strip()}")
            i += 1
        print()
    return

# Adds a task
def add_task() -> None:
    task_input = input("Input task: ")

    with open(todo_file, "rt") as f:
        task_list = [ line.strip() for line in f ]
    
    if task_input.lower() in ( t.lower() for t in task_list ):
        print("\nTask already exists!")
        return
    
    with open(todo_file, "at") as f:
        if task_list:
            f.write('\n' + task_input)
        else:
            f.write(task_input)
        print(f"\n\"{task_input}\" added successfully!\n")

    return None

#Edits task
def edit_task() -> None:
    with open(todo_file, "rt") as f:
        i = 1
        print()
        for line in f:
            print(f"{i}. {line.strip()}")
            i += 1
        f.seek(0)
        task_list = [ line.strip() for line in f ]

    print("\nWhich task would you like to edit?")
    while True:
        task_num_str = input("Enter task number: ")

        try:
            task_num = int(task_num_str) - 1
        except ValueError:
            print("Please enter a number!")
            continue

        if task_num < 0 or task_num > len(task_list) - 1:
            print(f"Please enter a number between 1-{len(task_list)}!")
            continue
        break

    if "Completed" in task_list[task_num]:
        print(f"\nMark \"{task_list[task_num][:-12]}\" as uncompleted?")
        while True:
            choice = input("Y/N: ").lower()
            if choice != 'y' and choice != 'n':
                print("Not a choice, please enter 'Y' or 'N'")
                continue
            break
            
        if choice == 'y':
            task_list[task_num] = task_list[task_num][:-12]
            print(f"\n\"{task_list[task_num]}\" marked as uncompleted!\n")
        else:
            return
        
    else:
        print(f"\nMark \"{task_list[task_num]}\" as completed?")
        while True:
            choice = input("Y/N: ").lower()
            if choice != 'y' and choice != 'n':
                print("Not a choice, please enter 'Y' or 'N'")
                continue
            break

        if choice == 'y':
            task_list[task_num] += " - Completed"
            print(f"\n\"{task_list[task_num][:-12]}\" marked as completed!\n")
        else:
            return
    
    with open(todo_file, "wt") as f:
            f.write('\n'.join(task_list))

    return

#Deletes a task
def delete_task() -> None:
    with open(todo_file, "rt") as f:
        task_list = [ line.strip() for line in f ]
    
    i = 1
    print()
    for line in task_list:
        print(f"{i}. {line.strip()}")
        i += 1
    
    print("\nWhich task would you like to delete?")
    while True:
        task_num_str = input("Enter task number: ")

        try:
            task_num = int(task_num_str) - 1
        except ValueError:
            print("Please enter a number!")
            continue

        if task_num < 0 or task_num > len(task_list) - 1:
            print(f"Please enter a number between 1-{len(task_list)}!")
            continue
        break

    if "Completed" in task_list[task_num]:
        print(f"Delete \"{task_list[task_num][:-12]}\"?")
        while True:
            choice = input("Y/N: ").lower()
            if choice != 'y' and choice != 'n':
                print("Not a choice, please enter 'Y' or 'N'!")
                continue
            break
        if choice == 'y':
            print(f"\n\"{task_list[task_num][:-12]}\" successfully deleted!\n")
            task_list.pop(task_num)
    else:
        print(f"Delete \"{task_list[task_num]}\"?")
        while True:
            choice = input("Y/N: ").lower()
            if choice != 'y' and choice != 'n':
                print("Not a choice, please enter 'Y' or 'N'!")
                continue
            break
    
        if choice == 'y':
            print(f"\n\"{task_list[task_num]}\" succesfully deleted!\n")
            task_list.pop(task_num)
    
    with open(todo_file, "wt") as f:
            f.write('\n'.join(task_list))
            
    return

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
