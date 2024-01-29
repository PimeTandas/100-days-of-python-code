# Rock, Paper, Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Welcome Message
print("Welcome to Rock, Paper, Scissors: Type (0) for rock, (1) for Paper and (2) for Scissors.")

# Get user input and computer input
input1 = int(input())
input2 = random.randint(0, 2)

options = [rock, paper, scissors]
user_choice, computer_choice = options[input1], options[input2]

# Print the game output
print(f"User picks: {options[input1]}")
print(f"Computer picks: {options[input2]}")

if user_choice == computer_choice:
    print("Its a Draw!")
elif (user_choice == paper and computer_choice == scissors) or (user_choice == rock and computer_choice == paper) or (
        user_choice == scissors and computer_choice == rock):
    print("You Lose.")
else:
    print("You Win.")