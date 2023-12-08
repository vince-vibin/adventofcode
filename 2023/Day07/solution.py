""" https://adventofcode.com/2023/day/7 """

SPECIAL_CARD = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
}

def get_card_values(hand):
    card_values = []
    for card in hand:
        if card.isdigit():
            card_values.append(int(card))
        else:
            card_values.append(int(SPECIAL_CARD[card]))
    return card_values

def count_hand(hand):
    hand_counted = []
    for card in hand:
        hand_counted.append(hand.count(card))
    return sorted(hand_counted, reverse=True)

def get_total(hands):
    worth = []
    for i, (_, bid) in enumerate(hands, start=1):
        worth.append(i * bid)
    return sum(worth)

with open("./input.txt", encoding="utf-8") as input_file:
    hands = []
    for line in input_file:
        hand, bid = line.split(" ")

        hand_values = get_card_values(hand)
        hand_counts = count_hand(hand)

        hands.append([hand_counts + hand_values, int(bid)])

hands.sort()

solution = get_total(hands)
print(f"The Solution is: {solution}")