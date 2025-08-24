import random
roll = random.randint(1,6)
guess = int(input("Enter you choise: "))
if guess == roll:
    print("Correct!it rolled " , roll)
else:
    print("Incorrect!It rolled " , roll)