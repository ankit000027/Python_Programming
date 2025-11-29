import random

# shoe of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def ace_or_11(hand):
    while sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1


def black_jack_player_cards():
    ace_or_11(player_cards)
    print("Your cards:", player_cards, "|| Total score:", sum(player_cards), f" || Dealer 1st card: {dealer[0]}")

    while True:
        ace_or_11(player_cards)

        total = sum(player_cards)

        if total > 21:
            return f"You were busted.. your deck = {player_cards} || Dealer cards: {dealer[0]} || Total Score {total} went over 21"

        if total == 21:
            return f"You won the match! Final hand: {player_cards} || Total score: {total}"

        stand_hit = input("stand or hit? ").lower()

        if stand_hit == "hit":

            new_card = random.choice(cards)
            player_cards.append(new_card)

            # adjust ace
            ace_or_11(player_cards)

            print(f"You drew: {new_card} || Total score: {sum(player_cards)} || Dealer cards: {dealer[0]}")

        elif stand_hit == "stand":
            print(f"You stopped at {sum(player_cards)} with hand {player_cards} || Dealers Turn")
            return total

        else:
            print("Invalid input! Type 'hit' or 'stand'.")


# Black jack dealer
def black_jack_dealer_card():
    ace_or_11(dealer)

    print(f"Dealer starts with: {dealer} || Score: {sum(dealer)}")

    while sum(dealer) < 17:
        new_card = random.choice(cards)
        dealer.append(new_card)
        ace_or_11(dealer)
        print(f"Dealer draws {new_card}. Dealer now has {dealer} || Score: {sum(dealer)}")

        if sum(dealer) > 21:
            return f"Dealer busted! || Cards: {dealer} || Score: {sum(dealer)}"

    dealer_score = sum(dealer)
    player_score = sum(player_cards)

    print(f"Dealer Finishes with {dealer} || Score: {dealer_score}")

    if dealer_score > player_score:
        return f"Dealer wins! Dealer: {dealer_score} > Player: {player_score}"
    elif dealer_score < player_score:
        return f"Player wins! Player: {player_score} > Dealer: {dealer_score}"
    else:
        return f"It's a draw! Player: {player_score} = Dealer: {dealer_score}"


# player_cards and dealer initial deck
player_cards = [random.choice(cards), random.choice(cards)]
dealer = [random.choice(cards), random.choice(cards)]

player_cards_outcome = black_jack_player_cards()
print(player_cards_outcome)

dealer_cards_outcome = black_jack_dealer_card()
print(dealer_cards_outcome)

