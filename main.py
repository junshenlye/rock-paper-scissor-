import random

options = ["rock", "paper", "scissor"]


def game():
  player_choice = str(input("Choose Rock, Paper or Scissor!")).lower()
  if player_choice in options:
    computer_choice = random.choice(options)
    if player_choice == computer_choice:
      print("Its a Tie!")
    elif player_choice == "rock" and computer_choice == "scissor":
      print("Congrates, You Won!. Rock Beats Scissor.")
    elif player_choice == "scissor" and computer_choice == "paper":
      print("Congrates, You Won!. Scissor Beats Paper")
    elif player_choice == "paper" and computer_choice == "rock":
      print("Congrates, You Won!. Paper Beats Rock.")
    else:
      computer_choice = computer_choice.capitalize()
      player_choice = player_choice.capitalize()
      print("You lost! {} beats {}.".format(computer_choice, player_choice))

  else:
    print("Invalid Option, Please Try Again!")


while True:
  game()