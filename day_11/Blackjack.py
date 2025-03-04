import random

def pull_cards(hands,hand, count):
    for i in range(count):
        hands[hand].append(random.choice(cards))

def show_hands(hands,hand):
    if hand == "your_hand":
        print(f"Your cards: {hands[hand]}, your score: {sum(hands[hand])}")
    else:
        print(f"Dealer's hand: {hands[hand]}, dealers score: {sum(hands[hand])}")

def score(hands,hand):
    return sum(hands[hand])

def switch_11(hands,hand):
    if hands[hand][len(hands[hand])-1] == 11 and score(hand) > 21:
        hands[hand][len(hands[hand])-1] = 1

def is_it_over(hands):
    your_sum = score(hands,"your_hand")
    dealer_sum = score(hands,"dealer_hand")
    if 11 in hands['dealer_hand'] and 10 in hands['dealer_hand'] and len(hands['dealer_hand']) == 2:
        return "You lost!"
    if 11 in hands['your_hand'] and 10 in hands['your_hand'] and len(hands['your_hand']) == 2:
        return "Blackjack!"
    elif dealer_sum > 21:
        return "The dealer went over. You won!"
    elif your_sum > 21:
        return "You went over. You lost!"
    elif dealer_sum == your_sum:
        return "draw."
    elif dealer_sum > your_sum:
        return "You lost!"
    elif dealer_sum < your_sum:
        return "You won!"

def main():
    want_to_play = input("Do you want to play Blackjack? (y/n) ").lower()

    while want_to_play == 'y':
        hands = {"your_hand": [],
                 "dealer_hand": []}

        pull_cards(hands,"your_hand", 2)
        pull_cards(hands,"dealer_hand", 1)
        show_hands(hands,"your_hand")
        show_hands(hands,"dealer_hand")

        if score(hands,"your_hand") >= 21:
            print(is_it_over(hands))
            want_cards = 'n'
        else:
            want_cards = input("\nType \'y\' to get another card, type \'n\' to pass: ").lower()
            print("\n")
        while want_cards == 'y':

            pull_cards(hands,"your_hand", 1)
            switch_11(hands,"your_hand")
            your_sum = score(hands,"your_hand")

            if your_sum >= 21:
                show_hands(hands,"your_hand")
                show_hands(hands,"dealer_hand")
                print(is_it_over(hands))
                want_cards = 'n'
                want_to_play = input("\nDo you want to play Blackjack? (y/n) ").lower()
                print("\n" * 20)
            else:
                show_hands(hands,"your_hand")
                show_hands(hands,"dealer_hand")
                want_cards = input("\nType \'y\' to get another card, type \'n\' to pass: ").lower()
                print("\n")

        if want_cards == 'n' and score(hands,"your_hand") < 21:
            while score(hands,"dealer_hand") < score(hands,"your_hand"):
                pull_cards(hands,"dealer_hand", 1)
                switch_11(hands,"dealer_hand")
            show_hands(hands,"your_hand")
            show_hands(hands,"dealer_hand")
            print(is_it_over(hands))
            want_to_play = input("Do you want to play Blackjack? (y/n) ").lower()
            print("\n" * 20)
        elif want_cards == 'n' and score(hands,"your_hand") >= 21:
            show_hands(hands,"your_hand")
            show_hands(hands,"dealer_hand")
            print(is_it_over(hands))
            want_to_play = input("Do you want to play Blackjack? (y/n) ").lower()
            print("\n" * 20)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



main()