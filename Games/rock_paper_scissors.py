import random

group = ["rock","paper","scissors"]
win_counter = 0
lose_counter = 0

while True:
    user_input = input("Type rock,paper or scissors: ").lower()

    if user_input == random.choice(group):
        print("Win")
        win_counter +=1
        print(f"You have total wins of: {win_counter}")

    elif user_input == "q":
        break
    else:
        lose_counter +=1
        print(f"Lose, you have total loses of {lose_counter}")
    
    
