try:
    age = int(input("Age: "))
except ValueError:
    print("You have typed in an invalid number. Please try again with a numerical response such as 12")
    age = int(input("Age: "))

if age > 18:
    print(f"You can drive at age {age}")

