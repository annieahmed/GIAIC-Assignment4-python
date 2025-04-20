import random

WORDS = ["python", "hangman", "challenge", "programming", "computer", "science", "developer"]


MAX_TRIES = 6

def choose_word():
    return random.choice(WORDS)

def display_word(secret_word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])

def main():
    print("🎯 Welcome to the Hangman Game!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 0
    won = False

    print(f"\nThe word has {len(secret_word)} letters.")
    
    while attempts < MAX_TRIES:
        print("\n" + display_word(secret_word, guessed_letters))
        print(f"❌ Wrong guesses left: {MAX_TRIES - attempts}")
        guess = input("🔤 Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("📛 You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✅ Good guess!")
        else:
            print("❌ Wrong guess.")
            attempts += 1

        
        if all(letter in guessed_letters for letter in secret_word):
            won = True
            break

    print("\n🎮 Game Over!")
    if won:
        print(f"🏆 Congratulations! You guessed the word: {secret_word}")
    else:
        print(f"😢 You ran out of attempts. The word was: {secret_word}")

if __name__ == "__main__":
    main()
