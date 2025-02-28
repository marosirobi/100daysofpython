def calculate_love_score(name1, name2):
    # your code here

    counter1 = 0
    counter2 = 0
    for letter in name1.lower():
        if letter in "true":
            counter1 += 1

        if letter in "love":
            counter2 += 1

    for letter in name2.lower():
        if letter in "true":
            counter1 += 1

        if letter in "love":
            counter2 += 1

    print(f"{counter1}{counter2}")


# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")
