def main():
    print("🧠 Think of a number between 1 and 100.")
    print("I will try to guess it!\n")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0

    while True:
        if low > high:
            print("Hmm... It seems there's a mistake in your responses.")
            break

        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        user_feedback = input("Is your number higher, lower, or correct?: ").strip().lower()

        if user_feedback == "higher":
            low = guess + 1
        elif user_feedback == "lower":
            high = guess - 1
        elif user_feedback == "correct":
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts.")
            break
        else:
            print("❌ Please enter 'higher', 'lower', or 'correct' only.\n")


if __name__ == '__main__':
    main()
