import random
moves = {"s":1,
         "w":0,
         "g":-1}

computer = random.randrange(-1,2)

user = input("Enter the move you wanna play s/w/g: ")
user_choice = moves[user]

if computer == -1 and user_choice == 0 or computer == 0 and user_choice == 1 or computer == 1 and user_choice == -1:
    print("User Wins!!")
elif user_choice == -1 and computer == 0 or user_choice == 0 and computer == -1 or user_choice == 1 and computer == -1:
    print("Computer Wins!!")
else:
    print("Draw!!")