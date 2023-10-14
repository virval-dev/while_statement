number = 23
running = True
guess_limit = 10

while running:
    guess = int(input("Enter an integer: "))
    if guess == number:
        print("You guessed it!")
        # this causes the while loop and program to stop
        running = False
    elif guess < number:
        print("No, it's a little higher than that...\n")
        guess_limit -= 1
    elif guess > number:
        print("No, it's a little lower than that...")
        guess_limit -= 1
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
        guess_limit -= 1
else:
    print("The while loop is over!")
    print("Guess the number between 1 - 100 only, please!")
    print("Done!")
