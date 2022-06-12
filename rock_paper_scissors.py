import random

moves = ("rock", "paper", "scissors")
while True:
    computer = random.choice(moves)
    player = input("rock, paper or scissors: ")
    

    if player == computer:
        print(computer)
        print(player)
        print("Tie!")
        continue
    elif player == "rock":
        if computer == "paper":
            print(computer)
            print(player)
            print("computer wins!")
            break
        else:
            print(computer)
            print(player)
            print("player wins!")
            break
    elif player == "paper":
        if computer == "scissors":
            print(computer)
            print(player)
            print("computer wins!")
            break
        else:
            print(computer)
            print(player)
            print("player wins!")    
            break
    elif player == "scissors":
        if computer == "rock":
            print(computer)
            print(player)
            print("computer wins!")
            break
        else:
            print(computer)
            print(player)
            print("player wins!")
            break
    else:
        print("Invalid move, Try Again!")
        continue
    
