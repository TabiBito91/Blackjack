import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play_game():
    choice_continue = "y"
    your_hand = []
    dealers_hand = []

    def calculate_score(hand):
        score = sum(hand)
        if 11 in hand and score > 21:
            hand[hand.index(11)] = 1
            score = sum(hand)
        return score

    your_score = calculate_score(your_hand)
    dealers_score = calculate_score(dealers_hand)

    def deal_cards():
        return random.choice(cards)

    def compare_cards(y_score, d_score):
        # Player busts
        if y_score > 21:
            print(f"Your final hand: {your_hand}, final score: {y_score}")
            print(f"Computer's final hand: {dealers_hand}, final score: {d_score}")
            print("You went over! Bust!")

        elif d_score > 21:
            print(f"Your final hand: {your_hand}, final score: {y_score}")
            print(f"Computer's final hand: {dealers_hand}, final score: {d_score}")
            print("The Computer went over! Bust!")

        elif y_score == d_score:
            if d_score == 21:
                print(f"Your final hand: {your_hand}, final score: {y_score}")
                print(f"Computer's final hand: {dealers_hand}, final score: {d_score}")
                print("You lose!")

            else:
                print(f"Your final hand: {your_hand}, final score: {y_score}")
                print(f"Computer's final hand: {dealers_hand}, final score: {d_score}")
                print("Draw")

        elif y_score > d_score:
            print(f"Your final hand: {your_hand}, final score: {y_score}")
            print(f"Computer's final hand: {dealers_hand}, final score: {d_score}")
            print("You win! Good job!")

        else:
            print(f"Your final hand: {your_hand}, final score: {y_score}")
            print(f"Computer's final hand: {dealers_hand}, final score: {d_score}")
            print("You lose!")


    continue_game = True
    first_round = True

    while continue_game:
        if choice_continue == "y":
            if first_round:
                print(art.logo)
                your_hand += random.sample(cards,2)
                dealers_hand += random.sample(cards,1)
                first_round = False
            else:
                your_hand.append(deal_cards())

            your_score = calculate_score(your_hand)
            dealers_score = calculate_score(dealers_hand)

            if your_score > 21:
                compare_cards(your_score, dealers_score)
                continue_game = False
            else:
                print(f"Your hand: {your_hand}, current score: {your_score}")
                print(f"Computer's hand: {dealers_hand}, current score: {dealers_score}")
                choice_continue = input("Type 'y' to get another card, type 'n' to pass")

        elif choice_continue == "n":
            dealers_hand.append(deal_cards())
            your_score = calculate_score(your_hand)
            dealers_score = calculate_score(dealers_hand)
            compare_cards(your_score,dealers_score)
            continue_game = False

        else:
            choice_continue = input("Type 'y' to get another card, type 'n' to pass")



while input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower() == "y":
    play_game()