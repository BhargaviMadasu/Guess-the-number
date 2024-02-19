import random
from prettytable import PrettyTable

def guess_the_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 50)

    # Set up the table
    table = PrettyTable()
    table.field_names = ["Attempt", "Guess", "Result"]

    print("Welcome to Guess the Number!")
    print("I've picked a number between 1 and 50. Try to guess it.")

    attempts = 0
    while True:
        # Get user input
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Check the guess
        if guess == secret_number:
            result = "Congratulations! Correct!"
            table.add_row([attempts, guess, result])
            print(table)
            break
        elif guess < secret_number:
            result = "Too low. Try again."
        else:
            result = "Too high. Try again."

        # Add row to the table
        table.add_row([attempts, guess, result])

        # Display the table
        print(table)

if __name__ == "__main__":
    guess_the_number()
