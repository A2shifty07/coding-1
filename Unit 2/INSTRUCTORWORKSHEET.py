# Thursday, october 22, 2026
def vending_machine():
    # Vending machine menu stored as a dictionary
    menu = {
        "B3": "Nacho Chips",
        "G4": "BBQ Chips",
        "G7": "Plain Chips",
        "D3": "Water",
        "G5": "Cola Soda"
    }

    print("Welcome to the Vending Machine!")
    print("Enter a code (e.g., D3) or 'q' to quit.\n")

    # Start the loop
    while True:
        user_input = input("Enter vending machine code: ").upper()

        # Check for quit condition
        if user_input == "Q":
            print("Stopping vending machine. Goodbye!")
            break

        # Check if the code exists in the menu
        if user_input in menu:
            print(f"Dispensing: {menu[user_input]}\n")
        else:
            print("Invalid code. Please try again.") 

# Friday, October 23, 2026

import random

def dice_game():
    score = 0
    choice = input("Enter 'r' to roll or 'q' to quit: ").lower()

    while choice == 'r':
        roll = random.randint(1, 7)
        print(f"You rolled: {roll}")

        if roll == 7:
            score += 10
            print("You win! +10 points")
        else:
            score -= 5
            print("You lost! -5 points")

        print(f"Current score: {score}")
        choice = input("Roll again? (r to roll, q to quit): ").lower()

    print(f"Game over! Final score: {score}")