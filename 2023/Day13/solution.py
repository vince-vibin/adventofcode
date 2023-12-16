""" https://adventofcode.com/2023/day/13 """

solution = []


def check_mirroring(segment, mirrorline_index, vertical):
    # mirror line is on the first index
    part1 = list(reversed(segment[:mirrorline_index + 1]))
    part2 = segment[mirrorline_index + 1:]
    points = len(part1)

    smallest = min(len(part1), len(part2))
    part1 = part1[:smallest]
    part2 = part2[:smallest]

    if part1 == part2:
        if vertical:
            return points
        return points * 100
    return False


def get_mirrorline(segment):
    # check for vertical mirror
    columns = []
    for i, _ in enumerate(segment[0]):
        column = []
        for row in segment:
            column.append(row[i])
        columns.append(column)

    for i, column in enumerate(columns):
        length = len(columns) - 1
        if length > i:
            if column == columns[i + 1] and check_mirroring(columns, i, True):
                return check_mirroring(columns, i, True)

    # check for horizontal mirror
    for i, row in enumerate(segment):
        length = len(segment) - 1
        if length > i:
            if row == segment[i + 1] and check_mirroring(segment, i, False):
                return check_mirroring(segment, i, False)


with open("./input.txt", encoding="utf-8") as input_file:
    lines = input_file.read()
    segments = lines.split('\n\n')

for segment in segments:
    solution.append(get_mirrorline(segment.split("\n")))

solution = sum(solution)
print(f"The Solution is: {solution}")
