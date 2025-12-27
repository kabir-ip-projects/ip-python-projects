total = 0
count = 0

while True:
    marks = input("Enter marks (or stop): ")

    if marks == "stop":
        break

    marks = int(marks)
    total = total + marks
    count = count + 1

if count > 0:
    avg = total / count
    print("Average =", avg)

    if avg >= 90:
        print("Grade: A+")
    elif avg >= 75:
        print("Grade: A")
    elif avg >= 60:
        print("Grade: B")
    else:
        print("Grade: C")
else:
    print("No data entered")
