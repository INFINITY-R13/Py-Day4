# Rock-Paper-Scissors

import random

game_variables = ['Rock', 'Paper', 'Scissor']

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissor. \n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number.")
else:    
    print(f"You chose {game_variables[user_choice]}.")

    computer_choice = random.randint(0,2)
    print(f"Computer chose {game_variables[computer_choice]}.")


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose.")    
    elif computer_choice > user_choice:
        print("You lose.")    
    elif computer_choice < user_choice:
        print("You win!")        
    elif user_choice == computer_choice:
        print("It's a Draw.")    
    













