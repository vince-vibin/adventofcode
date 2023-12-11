""" https://adventofcode.com/2023/day/3 """

solution = 0


def is_symbol(i, j):
    if (0 <= i < rows and 0 <= j < columns):  # if symbol is in the grid
        return bool(lines[i][j] != "." and not lines[i][j].isdigit())  # if symbol isnt a digit
    return False


with open("./input.txt", encoding="utf-8") as input_file:
    lines = input_file.readlines()
    lines = [line.rstrip() for line in lines]

rows = len(lines)
columns = len(lines[0])

for current_row, line in enumerate(lines):
    start = 0
    current_column = 0
    while columns > current_column:
        start = current_column
        num = ""
        while current_column < columns and line[current_column].isdigit():
            num += line[current_column]
            current_column += 1

        if num == "":  # no number next to it found
            current_column += 1
            continue

        num = int(num)

        if is_symbol(current_row, start - 1) or is_symbol(current_row, current_column):  # if symbol is left or right
            solution += num
            continue

        for k in range(start - 1, current_column + 1):
            if is_symbol(current_row - 1, k) or is_symbol(current_row + 1, k):
                solution += num
                break

print(f"The solution is: {solution}")
