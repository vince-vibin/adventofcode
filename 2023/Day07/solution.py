""" https://adventofcode.com/2023/day/7 """

def check_hand(hand):
    points_per_card = []
    for card in hand:
        points_per_card.append([card, hand.count(card)])
    
    temp = []
    temp1 = set(points_per_card)
    for points in points_per_card:
        if points not in temp:
            temp.append(points)
    points_per_card = temp
    print(temp1)
    return points_per_card

def get_points(points_per_card):
    highest = 0
    for card in points_per_card:
        if card[1] > highest:
            highest = card[1]
"""             if card[1] = 3:
                # check for full house """
                
        

with open("./input.txt", encoding="utf-8") as input_file:
    for line in input_file:
        solution = 0
        hand = line.split(" ")[0]
        bet = line.split(" ")[1]

        points_per_card = check_hand(hand)
        get_points(points_per_card)


print(f"The Solution is: {solution}")
