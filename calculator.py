print("SMART CALCULATOR")

while True:
    print("\n1.Add  2.Subtract  3.Multiply  4.Divide  5.Exit")
    ch = input("Choice: ")

    if ch == "5":
        print("Bye")
        break

    if ch == "1" or ch == "2" or ch == "3" or ch == "4":
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if ch == "1":
            print("Result =", a + b)
        elif ch == "2":
            print("Result =", a - b)
        elif ch == "3":
            print("Result =", a * b)
        elif ch == "4":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print("Result =", a / b)
    else:
        print("Invalid choice")
