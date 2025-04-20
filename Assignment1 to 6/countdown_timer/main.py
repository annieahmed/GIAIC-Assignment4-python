import time

def countdown_timer(seconds):
    while seconds:
        mins = seconds // 60
        secs = seconds % 60
        time_format = f"{mins:02d}:{secs:02d}"
        print("⏳ Time Left:", time_format, end='\r')  
        time.sleep(1)
        seconds -= 1

    print("⏰ Time's up!            ")

def main():
    print("🕒 Countdown Timer")
    try:
        user_input = int(input("⏱️ Enter time in seconds: "))
        if user_input <= 0:
            print("⚠️ Please enter a positive number.")
        else:
            countdown_timer(user_input)
    except ValueError:
        print("⚠️ Please enter a valid integer.")

if __name__ == "__main__":
    main()

