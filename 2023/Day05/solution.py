""" https://adventofcode.com/2023/day/5 """

# unfinished still need to fix this...


def parse_maps(map):
    map = map.split(":")[1]
    map = map.split("\n")
    map.pop(0)
    return map


def get_matches(line):
    line = line.split(" ")


solution = 0

input_file = open("./input.txt", encoding="utf-8").read().strip()
maps = input_file.split("\n\n")

initial_seeds = maps[0]
initial_seeds = initial_seeds.split(": ")[1].split(" ")

maps.pop(0)

for map in maps:
    print(parse_maps(map))

print(f"The Solution is: {solution}")
