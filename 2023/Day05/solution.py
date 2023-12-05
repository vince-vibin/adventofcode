""" https://adventofcode.com/2023/day/5 """

def parse_maps(map):
    map = map.split(":")[1]
    map = map.split("\n")
    map.pop(0)
    return map

def get_matches(line):
    line = line.split(" ")
    dest = line[0]
    start = line[1]
    range = line[2]

    


solution = 0

input_file = open("./input.txt").read().strip()
maps = input_file.split("\n\n")

initial_seeds = maps[0]
initial_seeds = initial_seeds.split(": ")[1].split(" ")

maps.pop(0)

for map in maps:
    print(parse_maps(map))
#print(maps)
print(f"The Solution is: {solution}")
