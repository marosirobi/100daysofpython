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



while placeholder != chosen_word and lives != 0:
    guess = input("\nguess a letter: ").lower()

    if guess in displaylist:
        print("You've already guessed that letter")

    letter_index = []
    count = 0
    i = 0
    for letter in chosen_word:
        if letter == guess and i == 0:
            print(chosen_word.index(letter))
            letter_index.append(chosen_word.index(letter))
            i = letter_index[len(letter_index) - 1]
        elif guess == letter and i > 0:
            print(chosen_word.index(letter,i+1))
            letter_index.append(chosen_word.index(letter,i+1))
            i = letter_index[len(letter_index)-1]

    for index in letter_index:
        if guess in chosen_word and guess not in displaylist:
            placeholder = placeholder[:index] + placeholder[index:].replace('_', guess,1)
            count += 1
        elif count != 0 and count == len(letter_index):
            displaylist.append(guess)




    if guess not in chosen_word:
        print("Sorry, that letter doesn't exist: "+guess)
        lives -= 1

    print("***************"+str(lives) + "/6 lives left***************")
    print(stages[lives])
    print(placeholder)


if placeholder == chosen_word:
    print("you've won")
if lives == 0:
    print(f"you lose: {chosen_word} was the word")