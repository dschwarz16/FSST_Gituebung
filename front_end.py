from backend import generate_number

def main():
    """
    Main function for the FSST Gituebung project.
    This function handles the user input and compares the guessed number with the generated number.
    """
    number = generate_number()
    guess = None
    print(f"Welcome to the number guessing game!, I have selected a number between 1 and 100.")
    print(f"And you have to guess it!")
    while True:
        try:
            guess = (input("Please enter your guess or 'exit': "))
            if guess == "exit":
                raise KeyboardInterrupt
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100")
                continue

            if guess == number:
                print("Congratulations! You guessed the number!")
            elif abs(guess - number) <= 10:
                print("Close! But not quite. Try again!")
            else:
                print(f"Sorry, the number was {number}. Better luck next time!")
                break

        except ValueError:
            print("Please enter a valid number")
            continue

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("Bye!")
            break