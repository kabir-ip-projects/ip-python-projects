correct_user = "admin"
correct_pass = "1234"

tries = 3

while tries > 0:
    user = input("Username: ")
    password = input("Password: ")

    if user == correct_user and password == correct_pass:
        print("Login successful")
        break
    else:
        tries = tries - 1
        print("Wrong details. Attempts left:", tries)

if tries == 0:
    print("Account locked")
