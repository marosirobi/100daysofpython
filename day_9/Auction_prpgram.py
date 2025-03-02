from os import system
from art import logo
print(logo)
print("Welcome to the secret auction program.")

bid_data = {}

def bid():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_data[name] = bid

def max(dict):
    print("Thank you for bidding.")
    max = 0
    index = ""
    for key in dict:
        if dict[key] > max:
            max = dict[key]
            index = key
    print(f"The winner is: {index} with ${max} bid.")

more_bidders = "yes"

while more_bidders == "yes":
    bid()
    more_bidders = input("Are there any other bidders? yes/no: ").lower()
    system('cls')

if more_bidders == "no":
    max(bid_data)

