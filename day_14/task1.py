import random,art
from game_data import*

def two_choice(num1):
    if num1 == -1:
        num1 = random.randint(0, len(data) - 1)
    num2 = num1
    while num1 == num2:
        num2 = random.randint(0, len(data) - 1)
    return num1, num2

def desc(num1,num2,score):
    if score > 0:
        print("You are right! Current score: " + str(score))
    else:
        print("Your current score is " + str(score))
    print(f"Compare A: {data[num1]["name"]}, {data[num1]["description"]}, from {data[num1]['country']}")
    print(art.vs)
    print(f"Against B: {data[num2]["name"]}, {data[num2]["description"]}, from {data[num2]['country']}")

def compare(n1,n2):
    if data[n1]["follower_count"] > data[n2]["follower_count"]:
        return "a"
    else:
        return "b"

def is_it_over(guess,answer):
    if guess == answer:
        return True
    else:
        return False

def main():
    score = 0
    num1 = two_choice(-1)[0]
    num2 = two_choice(num1)[1]
    run = True
    while run:
        print(art.logo)
        desc(num1,num2,score)
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        answer = compare(num1, num2)
        run = is_it_over(guess, answer)
        score += 1
        num1 = num2
        num2 = two_choice(num1)[1]
        print("\n"*20)

main()
