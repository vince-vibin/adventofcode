""" https://adventofcode.com/2023/day/12 """

solution = []

# still need to check the rows next to it to find a mirror
def get_mirrorline(segment):
    # check for vertical mirror
    columns = []
    i = 0
    while len(segment[0]) > i:
        column = []
        for row in segment:
            column.append(row[i])
        i += 1
        columns.append(column)

    for i, column in enumerate(columns):
        if len(columns) > i + 1 and column == columns[i + 1]:
            return(columns.index(column))

    # check for horizontal mirror
    for i, row in enumerate(segment):
        if len(segment) > i + 1 and row == segment[i + 1]:
            return(segment.index(row))


with open("./input.txt", encoding="utf-8") as input_file:
    lines = input_file.read()
    segments = lines.split('\n\n')

for segment in segments:
    print(get_mirrorline(segment.split("\n")))

solution = sum(solution)
print(f"The Solution is: {solution}")
