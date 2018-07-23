import getpass
print("Its time for some ROCK PAPER SCISSORS!!")
player1 = getpass.getpass("Player1 choose: rock, paper or scissors: ")
#print("*******NO CHEATING*********\n\n" * 35) this was a dumb idea
player2 = getpass.getpass("Player2 choose: rock, paper or scissors: ")

if player1 == player2:
	print("ITS A TIE")
elif player1 == "rock" and player2 == "scissors":
	print("PLAYER1 WINS!")
elif player1 == "paper" and player2 == "rock":
	print("PLAYER1 WINS!")
elif player1 == "scissors" and player2 == "paper":
	print("PLAYER1 WINS!")
else:
	print("PLAYER2 WINS!")
