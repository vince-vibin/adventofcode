""" https://adventofcode.com/2023/day/14 """

solution = []


def tilt_plattform(plattform):
    columns = []
    for i, char in enumerate(plattform[0]):
        column = []
        for row in plattform:
            column.append(row[i])
        columns.append(column)
    return columns


def calc_roling_rocks(column):
    falling_field = 0
    for i, field in enumerate(column):
        if field == "#":
            falling_field = i
        if len(column) - 1 < falling_field + 1:
            break
        if field == "O":
            if falling_field != 0:
                column[falling_field + 1] = "O"
                column[i] = "."
                falling_field += 2
            else:
                column[falling_field] = "O"
                column[i] = "."
                falling_field += 1
    return column

with open("./input.txt", encoding="utf-8") as input_file:
    lines = input_file.readlines()
    lines = [line.rstrip() for line in lines]


plattform_tilted = tilt_plattform(lines)
for column in plattform_tilted:
    print(calc_roling_rocks(column))
solution = sum(solution)
print(f"The Solution is: {solution}")
