""" https://adventofcode.com/2023/day/21 """

solution = []

with open("./input.txt", encoding="utf-8") as input_file:
    lines = input_file.readlines()
    lines = [line.rstrip() for line in lines]

solution = sum(solution)
print(f"The Solution is: {solution}")
