import random

print("ROCK? PAPER? SCISSORS? YOU DECIDE!!")
player = input("Choose: Rock, paper or scissors ").lower()
rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"
print(f"Computer plays {computer}")
if player == computer:
    print("ITS A TIE")
elif player == "rock":
    if computer == "scissors":
        print("Player1 WINS!")
    else:
        print("Computer Wins!")
elif player == "paper":
    if computer == "rock":
        print("Player1 WINS!")
    else:
        print("Computer Wins!")
elif player == "scissors":
    if computer == "paper":
        print("Player1 WINS!")
    else:
        print("Computer Wins!")
else:
    print("Enter valid entry")
