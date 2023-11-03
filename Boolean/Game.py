import random

player = input("Player, make your move: ")

rand_num = random.randint(0,2)
if rand_num == 0:
    computer = "Rock"
elif rand_num == 1:
    computer = "Paper"
else:
    computer = "Scissors"
print(f"computer plays {computer}" )  

if player == computer:
    print("It's a tie!")
elif player == "Rock":
    if computer == "Scissors":
        print("Player wins!")  
elif computer == "Paper":
    print("computer wins!")
elif player == "Paper":
    if computer == "Rock":
        print("Player wins!")
elif computer == "Scissors":
        print("computer wins!")
elif player == "Scissors":
        if computer == "Paper":
            print("Player wins!")
elif computer =="Rock":
            print("computer wins!")
else:
    print("Oops something went wrong")                  
        