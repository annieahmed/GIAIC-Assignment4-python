import random

def main():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?\n")

    
    secret_number = random.randint(1, 100)

    attempts = 0
    guess = None

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < secret_number:
                print("Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("Too high! Try a lower number.\n")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts. Great job!\n")
        except ValueError:
            print("Please enter a valid number.\n")


if __name__ == '__main__':
    main()
