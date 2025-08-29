import random

def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total

player1 = input("Enter the name of Player 1: ")
player2 = input("Enter the name of Player 2: ")

roll1 = roll_dice()  
roll2 = roll_dice()  

print(f"{player1} rolled a {roll1}")
print(f"{player2} rolled a {roll2}")

if roll1 > roll2:
    print(f"{player1} wins!")
elif roll2 > roll1:
    print(f"{player2} wins!")
else:
    print("It's a tie!")
