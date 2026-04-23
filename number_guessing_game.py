import random

print("\nWelcome to the Numbers Guessing Game!")

difficulty_ranges = {
    "easy":25,
    "medium":35,
    "hard":45,
}

print("\nRULES:\n1.You get a secret number assigned to you that you have to guess.\n2.You have 3 guesses!\n3.To win, you have to guess right!\n4.If you guess wrong 3 times, you lose!")
print('\nGame difficulties available: "Easy"= 1-25\n"Medium"= 1-35\n"Hard"= 1-45')

while True:
    difficulty = input('\nWhat difficulty would you like to play?\n"Easy"\n"Medium"\n"Hard"\nChoice:').strip().lower()
    if difficulty in difficulty_ranges:
        break
    else:
        print("Invalid choice, try again.")

print(f"You have chosen {difficulty.capitalize()} difficulty.")

max_num = difficulty_ranges[difficulty]
secret_number = random.randint(1, max_num)

game_over = False
lives = 3

#Main Game Loop
while not game_over:
    try:
        user_guess = int(input(f"Guess a number between 1 and {max_num}: "))
    except ValueError:
        print("Invalid input. Enter a number.")
        continue
    if user_guess < 1 or user_guess > max_num:
        print(f"Number outside of your chosen range:(1-{max_num}).")
        continue
    if user_guess == secret_number:
        print("You Win! You have guessed the right number.")
        game_over = True
    elif user_guess < secret_number:
        lives -= 1
        print(f"Too low, you have {lives} lives remaining.")
    else:
        lives -= 1
        print(f"Too high, you have {lives} lives remaining.")
    if lives <= 0:
        print("Game Over!")
        print(f"Correct number was: {secret_number}.")
        game_over = True
