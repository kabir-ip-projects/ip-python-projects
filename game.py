secret = 7
attempts = 3

while attempts > 0:
    guess = int(input("Guess the number (1-10): "))

    if guess == secret:
        print("You won!")
        break
    else:
        attempts = attempts - 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("Game over. Number was", secret)
