import random
comp_choice = random.choice(["rock","paper","scissoirs"])
user_choice = input("Enter ur choice!")
print("computer choice" , comp_choice)
if comp_choice == user_choice:
    print("Tie")
elif user_choice == "rock" and comp_choice == "scissors":
    print("Win")
elif user_choice == "paper" and comp_choice == "rock":
    print("Win")
elif user_choice == "scissors" and comp_choice == "paper":
    print("Win")
else:
    print("You lost!")