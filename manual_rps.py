import random

from numpy import integer

rps = ["Rock", "Paper", "Scissors"]

def get_computer_choice():
    return random.choice(rps)

def get_user_choice():
    return input("Please choose Rock, Paper or Scissors:\n")

def get_winner(computer_choice, user_choice):
    pairs = [("Rock", "Scissors"), ("Scissors", "Paper"), ("Paper", "Rock")]
    if (computer_choice, user_choice) in pairs:
        print("Computer wins")
    elif (user_choice, computer_choice) in pairs:
        print("User wins")
    else:
        print("It's a draw")

def play():
    computer_rps = get_computer_choice()

    user_rps = get_user_choice().capitalize()
    while user_rps not in rps:
        print("\nSorry that input is invalid.")
        user_rps = get_user_choice().capitalize()

    print(f"\nComputer picks: {computer_rps}")
    print(f"User picks: {user_rps}")

    get_winner(computer_rps, user_rps)

play()