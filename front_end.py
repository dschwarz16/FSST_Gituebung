from backend import generate_number

def main():
    """
    Main function for the FSST Gituebung project.
    This function handles the user input and compares the guessed number with the generated number.
    """
    number = generate_number()
    guesses = 0
    print(f"Welcome to the number guessing game!, I have selected a number between 1 and 100.")
    print(f"And you have to guess it!")
    while True:
        try:
            guess = (input("\n\n Please enter your guess or 'exit': "))
            if guess == "exit":
                raise KeyboardInterrupt
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100")
                continue

            guesses += 1
            if guesses > 10:
                print("You guessed to often")
                print(f"Sorry, the number was {number}. Better luck next time! \n\n\n\n")
                break

            if guess == number:
                print("Congratulations! You guessed the number!")
                return
            elif abs(guess - number) <= 5:
                print("You're on fire! So close!")
            elif abs(guess - number) <= 10:
                print("Close! But not quite. Try again!")
            elif abs(guess - number) <= 20:
                print("You're getting warmer! Keep trying!")
            elif abs(guess - number) <= 30:
                print("You're luke warm already ! Try again!")
            elif abs(guess - number) <= 40:
                print("Are you really that bad? Try again!")
            elif abs(guess - number) <= 50:
                print("You're freezing! Try again!")
            elif abs(guess - number) <= 60:
                print("You're ice cold! Try again!")
            else:
                print("You're way off!!")


        except ValueError:
            print("Please enter a valid number")
            continue

if __name__ == "__main__":
    while True:
        try:
            main()
            print("\n"*20)
            print("Do you want to play again? (y/n)")
            play_again = input()
            if play_again.lower() == "y":
                continue
            elif play_again.lower() == "n":
                print("Thanks for playing!")
                break
            else:
                print("Please enter a valid answer")
        except KeyboardInterrupt:
            print("Bye!")
            break