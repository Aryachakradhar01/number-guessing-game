import random

score = 0

while True:
    print("\n Welcome to Number Guessing Game!")
    print("Choose difficulty:")
    print("1. Easy (1–50, 10 attempts)")
    print("2. Medium (1–100, 7 attempts)")
    print("3. Hard (1–200, 5 attempts)")

    choice = input("Enter 1 / 2 / 3: ")

    if choice == "1":
        max_number = 50
        attempts = 10
    elif choice == "2":
        max_number = 100
        attempts = 7
    elif choice == "3":
        max_number = 200
        attempts = 5
    else:
        print(" Invalid choice. Try again?.")
        continue

    secret_number = random.randint(1, max_number)
    print(f"\nI have chosen a number between 1 and {max_number}.")
    print(f"You have {attempts} attempts. Good luck! 🍀")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        attempts -= 1

        if guess < secret_number:
            print("⬇️ Too low!")
        elif guess > secret_number:
            print("⬆️ Too high!")
        else:
            print("🎉 Correct! You guessed it!")
            score += 10
            print(f"🏆 Score: {score}")
            break

        print(f"Attempts left: {attempts}")

    else:
        print(f"\n💀 Game Over! The number was {secret_number}")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("\n👋 Thanks for playing!")
        print(f"Final Score: {score}")
        break
