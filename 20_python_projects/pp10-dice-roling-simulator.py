# ==================================================================================================================================================================== #
# DICE ROLING SIMULATOR. 
# ==================================================================================================================================================================== #

import random 

def roll_dice():
    
    roll = input("Roll the dice? (Yes / No): ")
    
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        print("Dice rolled: Dice1 equal {} and Dice 2 equal {}.".format(dice1, dice2))
        
        roll = input("Roll again? (Yes / No)? ")

roll_dice()