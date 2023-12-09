""" https://adventofcode.com/2023/day/4 """


def parse_numbers(numbers):
    numbers_parsed = []
    for number in numbers:
        if number.rstrip().isdigit():
            numbers_parsed.append(int(number))
    return numbers_parsed


def find_winning(numbers_winning, numbers_got):
    numbers_found = []
    for number in numbers_winning:
        if number in numbers_got:
            numbers_found.append(number)
    return numbers_found


def calc_score(numbers):
    score = 0
    if len(numbers) >= 1:
        score += pow(2, len(numbers) - 1)
    return score


with open("./input.txt", encoding="utf-8") as input_file:
    solution = 0
    for line in input_file:
        numbers = line.split(":")[1]
        numbers_winning = parse_numbers(numbers.split(" | ")[0].split(" "))
        numbers_got = parse_numbers(numbers.split(" | ")[1].split(" "))

        actually_winning = find_winning(numbers_winning, numbers_got)
        if len(actually_winning) != 0:
            solution += calc_score(actually_winning)

print(f"The Solution is: {solution}")
