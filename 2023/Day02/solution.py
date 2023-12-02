""" https://adventofcode.com/2023/day/2 """

import re

CUBES_LOADED = {"red": 12, "green": 13, "blue": 14}


def check_sets(sets):
    for set in sets:
        cubes = set.split(",")
        if check_cubes(cubes) is False:
            return False
    return True


def check_cubes(cubes):
    for cube in cubes:
        number = int(cube[1:].split(" ")[0])
        color = cube[1:].split(" ")[1].rstrip()
        if number > CUBES_LOADED[color]:
            return False
    return True


with open("./input.txt", encoding="utf-8") as input_file:
    solution = 0
    for line in input_file:
        game_id = int(re.findall(r'\d+', line.split(":")[0])[0])
        sets = line.split(":")[1].split(";")
        if check_sets(sets):
            solution = solution + game_id

print(f"The Solution is: {solution}")
