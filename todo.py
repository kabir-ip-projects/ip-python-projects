todo = []

while True:
    print("\n1.Add Task  2.View Tasks  3.Remove Task  4.Exit")
    ch = input("Choice: ")

    if ch == "1":
        task = input("Enter task: ")
        todo.append(task)
        print("Task added")

    elif ch == "2":
        if len(todo) == 0:
            print("No tasks")
        else:
            for i in range(len(todo)):
                print(i+1, ".", todo[i])

    elif ch == "3":
        num = int(input("Enter task number to remove: "))
        if num <= len(todo):
            todo.pop(num-1)
            print("Task removed")
        else:
            print("Invalid number")

    elif ch == "4":
        break

    else:
        print("Wrong choice")
