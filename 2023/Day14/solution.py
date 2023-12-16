""" https://adventofcode.com/2023/day/14 """

solution = []


def get_columns(plattform):
    columns = []
    for i, _ in enumerate(plattform[0]):
        column = []
        for row in plattform:
            column.append(row[i])
        columns.append(column)
    return columns


def tilt_plattform(column):
    falling_field = 0
    for i, elem in enumerate(column):
        if elem == ".":
            continue
        if elem == "#":
            falling_field = i + 1
        if elem == "O":
            if column[i] != column[falling_field]:
                column[falling_field] = "O"
                column[i] = "."
                falling_field += 1
            else:
                falling_field += 1
    return column


def calc_column_score(column):
    score = 0
    for i, elem in enumerate(column):
        if elem == "O":
            score += len(column) - i
    return score


with open("./input.txt", encoding="utf-8") as input_file:
    lines = input_file.readlines()
    lines = [line.rstrip() for line in lines]

plattform = get_columns(lines)
for column in plattform:
    column = tilt_plattform(column)
    solution.append(calc_column_score(column))

solution = sum(solution)
print(f"The Solution is: {solution}")
