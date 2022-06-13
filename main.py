import random

user_action = input("Enter a choice (R, P, S): ")
possible_actions = ["R", "P", "S"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "R":
    if computer_action == "S":
        print("Rock smashes Scissors! You win!")
    else:
        print("Paper covers Rock! You lose.")
elif user_action == "P":
    if computer_action == "R":
        print("Paper covers Rock! You win!")
    else:
        print("Scissors cuts Paper! You lose.")
elif user_action == "S":
    if computer_action == "P":
        print("Scissors cuts Paper! You win!")
    else:
        print("Rock smashes Scissors! You lose.")