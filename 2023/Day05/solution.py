""" https://adventofcode.com/2023/day/5 """

import re


def main(lines):
    segments = lines.split('\n\n')
    seeds = re.findall(r'\d+', segments[0])

    min_location = float('inf')
    for x in map(int, seeds):
        for seg in segments[1:]:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)', seg):
                destination, start, delta = map(int, conversion)
                if x in range(start, start + delta):
                    x += destination - start
                    break

        min_location = min(x, min_location)

    return min_location


with open("./input.txt", encoding="utf-8") as input_file:
    solution = main(input_file.read())

print(solution)
