import random

print("Welocme to the PyPassword Generator!")
letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like?\n"))
number_count = int(input("How many numbers would you like?\n"))

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','#','$','%','&','*','(',')','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

all_count = letter_count + symbol_count + number_count

password_list = []
hard_password = ""
easy_password = ""

for i in range(0,letter_count):
    char = random.choice(letters)
    password_list.append(char)
    easy_password += char

for i in range(0,symbol_count):
    char = random.choice(symbols)
    password_list.append(char)
    easy_password += char

for i in range(0,number_count):
    char = random.choice(numbers)
    password_list.append(char)
    easy_password += char

# print(password_list)

# random.shuffle(password_list)
# print(password_list)

for i in range(0,password_list.__len__()):
    random_num = int(random.randint(0,password_list.__len__()-1))
    hard_password += password_list[random_num]
    password_list.remove(password_list[random_num])

print("easy pw: "+easy_password)
print("hard pw: "+hard_password)
