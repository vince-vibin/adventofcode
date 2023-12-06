""" https://adventofcode.com/2023/day/6 """

solution = 0

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

lines = get_lines()

times = parse_lists(lines[0].split(":")[1].split(" "))
distance = parse_lists(lines[1].split(":")[1].split(" "))

print(f"The Solution is: {solution}")
