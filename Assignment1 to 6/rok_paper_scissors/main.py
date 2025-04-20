import random

def get_computer_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def get_user_choice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("❌ Invalid input. Please type 'rock', 'paper', or 'scissors'.")

def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

def main():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    
    rounds = int(input("How many rounds would you like to play? "))
    user_score = 0
    computer_score = 0

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "user":
            print("✅ You win this round!")
            user_score += 1
        elif result == "computer":
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("🤝 It's a draw!")

        print(f"Score => You: {user_score} | Computer: {computer_score}")

    print("\n🎉 Game Over!")
    if user_score > computer_score:
        print("🏆 Congratulations! You won the game!")
    elif user_score < computer_score:
        print("💻 Computer wins the game. Better luck next time!")
    else:
        print("⚖️ It's a tie!")

if __name__ == '__main__':
    main()
