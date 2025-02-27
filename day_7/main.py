import random
from hangman_art import stages,logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(placeholder)

displaylist = []

display = ""


while display != chosen_word and lives != 0:
    guess = input("\nguess a letter: ").lower()
    display = ""

    if guess in displaylist:
        print("You've already guessed that letter")

    for letter in chosen_word:
        if guess == letter:
            display += letter
            displaylist.append(letter)
        elif letter in displaylist:
            display += letter
        else:
            display += "_"



    if guess not in chosen_word:
        print("Sorry, that letter doesn't exist: "+guess)
        lives -= 1

    print("***************"+str(lives) + "/6 lives left***************")
    print(stages[lives])
    print(display)


if display == chosen_word:
    print("you've won")
if lives == 0:
    print(f"you lose: {chosen_word} was the word")