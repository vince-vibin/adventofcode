""" https://adventofcode.com/2023/day/8 """              

import re

def rm_newline(lines):
    lines = [line.rstrip() for line in lines]
    return lines


def find_node(search):
    for node in nodes:
        if node.startswith(search):
            return nodes[nodes.index(node)]


with open("./input.txt", encoding="utf-8") as input_file:
    lines = input_file.readlines()
    instructions = lines[0].rstrip()
    nodes = rm_newline(lines[2:])


# get start
current_node = find_node("AAA")
i = 0
steps = 0
while i <= len(instructions) - 1:
    instruction = instructions[i]
    if instruction == "L":
        current_node = find_node(current_node.split(",")[0][3:].split("(")[1])
    elif instruction == "R":
        current_node = find_node(current_node.split(", ")[1].split(")")[0])
    steps += 1
    if current_node.startswith("ZZZ"):
        print("found goal")
        break
    i += 1
    if i >= len(instructions):
        i = 0

solution = steps
print(f"The Solution is: {solution}")
