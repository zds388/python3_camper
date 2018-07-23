import getpass
import random
print("Its time for some ROCK PAPER SCISSORS!!")
player = getpass.getpass("Player1 choose: rock, paper or scissors: ").lower()

rand_num = random.randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	computer = "scissors"

if player != "rock" and player != "paper" and player != "scissors":
	print("Please enter valid input")
else:
	print(f"Computer plays {computer}")
	if player == computer:
		print("ITS A TIE")
	elif player == "rock" and computer == "scissors":
		print("PLAYER1 WINS!")
	elif player == "paper" and computer == "rock":
		print("PLAYER1 WINS!")
	elif player == "scissors" and computer == "paper":
		print("PLAYER1 WINS!")
	else:
		print("COMPUTER WINS!")
