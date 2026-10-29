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
        if user_input == "q":
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







# monday, October 26, 2026 

def rock_paper_scissors():
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    cpu_options = ['r', 'p', 's']

    user_score = 0
    cpu_score = 0
    rounds_played = 0

    while rounds_played < 3:
        user_input = input("Enter r (rock), p (paper), s (scissors), or q (quit): ").lower()

        if user_input == 'q':
            print("You chose to quit the game.")
            break

        if user_input not in choices:
            print("Invalid input. Please try again.")
            continue

        cpu_choice = random.choice(cpu_options)
        print(f"You chose {choices[user_input]}. CPU chose {choices[cpu_choice]}.")

        # Determine outcome
        if user_input == cpu_choice:
            print("It's a tie!")
        elif (user_input == 'r' and cpu_choice == 's') or \
             (user_input == 'p' and cpu_choice == 'r') or \
             (user_input == 's' and cpu_choice == 'p'):
            print("You win this round!")
            user_score += 1
        else:
            print("CPU wins this round!")
            cpu_score += 1

        rounds_played += 1
        print(f"Score → You: {user_score} | CPU: {cpu_score}\n")

    print("Game Over!")
    print(f"Final Score → You: {user_score} | CPU: {cpu_score}") 

    # How the game works
# Two players face each other and agree to play Rock, Paper, Scissors. They typically decide whether they will play a single round or multiple rounds.
# Both players raise one hand and prepare to make a choice. They usually count together by saying “Rock, Paper, Scissors, shoot!” or a similar phrase.
# On the final word, both players simultaneously form one of three hand signs. The three possible signs are Rock (a closed fist), Paper (an open hand), and Scissors (a fist with the index and middle fingers extended).
# Each sign has a specific relationship to the others. Rock beats Scissors, Scissors beats Paper, and Paper beats Rock.
# Rock beats Scissors because a rock can break a pair of scissors.
# Scissors beat Paper because scissors can cut paper.
# Paper beats Rock because paper can wrap around a rock.
# If both players choose the same sign, the round ends in a tie. No one wins, and the players may choose to repeat the round.
# The winner of the round is the player whose sign defeats the other according to the rules.
# If the game is played in multiple rounds, players keep track of how many rounds each person wins. The player with the most wins at the end is the overall winner.
# Players may repeat the game as many times as they like. The rules remain the same for every round