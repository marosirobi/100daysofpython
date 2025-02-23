size = input("what size of pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else: print("Please enter a valid size.")

if pepperoni == "Y":
    if size == "M" or size == "L":
        bill += 3
    else:
        bill += 2

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")