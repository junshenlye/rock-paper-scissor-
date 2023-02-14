import random

options = ["rock", "paper", "scissor"]
def check_winners(player, computer):
    if player == computer:
      print("Its a Tie!")
    elif player == "rock" and computer == "scissor":
      print("Congrates, You Won!. Rock Beats Scissor.")
    elif player == "scissor" and computer == "paper":
      print("Congrates, You Won!. Scissor Beats Paper")
    elif player == "paper" and computer == "rock":
      print("Congrates, You Won!. Paper Beats Rock.")
    else:
      computer = computer.capitalize()
      player = player.capitalize()
      print("You lost! {} beats {}.".format(computer, player))

while True:
  player_choice = str(input("Choose Rock, Paper or Scissor:")).lower()
  if player_choice in options:
    computer_choice = random.choice(options)
    check_winners(player_choice, computer_choice)
  else:
    print("Invalid Option, Please Try Again!")
  
