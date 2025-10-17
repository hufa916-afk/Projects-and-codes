tasks = []

while True:
    print("\n1. Add Task  2. View Tasks  3. Remove Task  4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        tasks.append(input("Enter task: "))
    elif choice == "2":
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
    elif choice == "3":
        index = int(input("Enter task number to remove: "))
        tasks.pop(index - 1)
    elif choice == "4":
        break
