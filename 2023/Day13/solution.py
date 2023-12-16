""" https://adventofcode.com/2023/day/13 """

solution = []


def check_mirroring(segment, mirrorline_index, vertical):
    # mirror line is on the first index
    part1 = list(reversed(segment[:mirrorline_index + 1]))
    part2 = segment[mirrorline_index + 1:]
    points = len(part1)

    print(part1)
    print(part2)

    if len(part1) > len(part2):
        part1 = part1[:len(part2)]
    else:
        part2 = part2[:len(part1)]

    if part1 == part2:
        if vertical:
            return points
        else:
            return points * 100
    else:
        return False


def get_mirrorline(segment):
    print(segment)
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
            # already the same column and column + 1
            if check_mirroring(columns, columns.index(column), True) is not False:
                return check_mirroring(columns, columns.index(column), True)
            else:
                print("noting vertical found")
                print(check_mirroring(columns, columns.index(column), True))

    # check for horizontal mirror
    for i, row in enumerate(segment):
        if len(segment) > i + 1 and row == segment[i + 1]:
            if check_mirroring(segment, segment.index(row), False) is not False:
                return check_mirroring(segment, segment.index(row), False)
            else:
                print("noting horizontal found")
                print(check_mirroring(segment, segment.index(row), False))


with open("./input.txt", encoding="utf-8") as input_file:
    lines = input_file.read()
    segments = lines.split('\n\n')

for segment in segments:
    print(segment)
    solution.append(get_mirrorline(segment.split("\n")))

print(solution)
solution = sum(solution)
print(f"The Solution is: {solution}")
