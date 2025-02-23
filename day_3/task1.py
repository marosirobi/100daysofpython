print("Welcome to the rollercoaster!")
height = int(input("Please enter your height in centimeters: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("Please enter your age: "))

    if age < 12:
        print("The cost of the ticket is $5")
        bill = 5
    elif age <=18:
        print("The cost of the ticket is $7")
        bill = 7
    elif 45 <= age <= 55:
        print("The cost of the ticket is free")
    else:
        print("The cost of the ticket is $12")
        bill = 12

    want_photo = input("Do you want photo?(y/n) ")
    if  want_photo == "y":
        bill += 3

    print(f"Your final bill is: $ {bill}")
else:
    print("You can't ride the rollercoaster!")





# if int(input("I need a number: ")) % 2 == 0:
#     print("Its even number")
# else: print("Its odd number")

