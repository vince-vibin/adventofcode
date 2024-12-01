""" https://adventofcode.com/2023/day/12 """

solution = []
rows = []
sizes = []

with open("./input.txt", encoding="utf-8") as input_file:
    lines = input_file.readlines()
    lines = [line.rstrip() for line in lines]
    for line in lines:
        row, size = line.split(" ")
        rows.append(row)
        sizes.append(size)


solution = sum(solution)
print(f"The Solution is: {solution}")
