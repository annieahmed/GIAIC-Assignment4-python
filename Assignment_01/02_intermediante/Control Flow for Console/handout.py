import random

# Constants
NUM_ROUNDS = 5
MIN_NUM = 1
MAX_NUM = 100

def get_valid_input():
    """Get user input and ensure it's either 'higher' or 'lower'"""
    while True:
        user_guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        if user_guess in ['higher', 'lower']:
            return user_guess
        print("Please enter either higher or lower.")

def play_round(round_num, score):
    print(f"Round {round_num}")
    user_number = random.randint(MIN_NUM, MAX_NUM)
    computer_number = random.randint(MIN_NUM, MAX_NUM)

    print(f"Your number is {user_number}")
    guess = get_valid_input()

    if guess == "higher" and user_number > computer_number:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    elif guess == "lower" and user_number < computer_number:
        print(f"You were right! The computer's number was {computer_number}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}")

    print(f"Your score is now {score}\n")
    return score

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round(round_num, score)

    print("Thanks for playing!")

    
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == '__main__':
    main()
