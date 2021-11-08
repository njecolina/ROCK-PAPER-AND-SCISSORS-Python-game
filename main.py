import random

print("Welcome to ROCK, PAPER AND SCISSORS Python game! :)")

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

player = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

choice = int(player)

if choice == 0:
  print("\n" + rock + "\nYou choose a ROCK")
elif choice == 1:
  print("\n" + paper + "\nYou choose a PAPER")
elif choice == 2:
  print("\n" + scissors + "\nYou choose a SCISSORS")

comp_choice = random.randint(0, 2)

if comp_choice == 0:
  print("\n" + rock + "\nComputer choose a ROCK")
elif comp_choice == 1:
  print("\n" + paper + "\nComputer choose a PAPER")
elif comp_choice == 2:
  print("\n" + scissors + "\nComputer choose a SCISSORS")

if comp_choice == choice:
  print("It's a draw! :O")
elif comp_choice == 0 and choice == 2:
  print("Rock wins against scissors - YOU LOSE!")
elif comp_choice == 0 and choice == 1:
  print("Paper wins against rock - YOU WIN!")
elif comp_choice == 1 and choice == 2:
  print("Scissors win against paper - YOU WIN!")
elif comp_choice == 1 and choice == 0:
  print("Paper wins against rock - YOU LOSE!")
elif comp_choice == 2 and choice == 1:
  print("Scissors win against paper - YOU LOSE!")
elif comp_choice == 2 and choice == 0:
  print("Rock wins against scissors - YOU WIN!")
