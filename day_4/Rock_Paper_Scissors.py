import random

actions_ascii = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""","""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""","""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

user_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_num = random.randint(0,2)

if 0<= user_num <=2:
    print(f"You chose:\n{actions_ascii[user_num]}")

print(f"Computer chose:\n{actions_ascii[comp_num]}\n")

if user_num == comp_num:
    print("You draw.")
elif user_num == 0:
    if comp_num == 1:
        print("You lose.")
    else: print("You win!")
elif user_num == 1:
    if comp_num == 0:
        print("You win!")
    else: print("You lose.")
elif user_num == 2:
    if comp_num == 0:
        print("You lose.")
    else: print("You win!")
else: print("You typed an invalid number. You lose.")


