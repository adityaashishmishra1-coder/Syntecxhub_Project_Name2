import random

best_score = None

while True:
    print("\n===== NUMBER GUESSING GAME =====")
    print("Select Difficulty Level:")
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 500)")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("Thanks for playing!")
        break

    if choice == "1":
        max_num = 50
    elif choice == "2":
        max_num = 100
    elif choice == "3":
        max_num = 500
    else:
        print("Invalid choice! Please try again.")
        continue

    secret_number = random.randint(1, max_num)
    attempts = 0

    print(f"\nI have selected a number between 1 and {max_num}.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts.")

                if best_score is None or attempts < best_score:
                    best_score = attempts
                    print(f"🏆 New Best Score: {best_score} attempts!")

                print(f"Best Score: {best_score}")
                break

        except ValueError:
            print("Please enter a valid number.")

    replay = input("\nDo you want to play again? (yes/no): ").lower()

    if replay != "yes":
        print("Thanks for playing!")
        break