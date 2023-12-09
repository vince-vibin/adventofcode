""" https://adventofcode.com/2023/day/6 """


def get_lines():
    with open("./input.txt", encoding="utf-8") as input_file:
        lines = []
        for line in input_file:
            lines.append(line)
        return lines


def parse_lists(list):
    parsed_list = []
    for elem in list:
        if elem != "":
            parsed_list.append(int(elem))
    return parsed_list


def get_won_multiplied(won):
    multiplied = 1
    for race in won:
        multiplied *= race
    return multiplied


lines = get_lines()

times = parse_lists(lines[0].split(":")[1].split(" "))
record = parse_lists(lines[1].split(":")[1].split(" "))

won = []
for time in times:
    won_per_race = 0
    for hold_ms in list(range(0, time + 1)):
        ms_remaining = time - hold_ms
        distance = ms_remaining * hold_ms

        if distance > record[times.index(time)]:
            won_per_race += 1
    won.append(won_per_race)

solution = get_won_multiplied(won)
print(f"The Solution is: {solution}")
