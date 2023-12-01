""" https://adventofcode.com/2023/day/1 """

import re

with open("./input.txt", encoding="utf-8") as input_file:
    solution: int
    for line in input_file:
        nums = re.findall(r'\d', line)
        first_num = nums[0]
        last_num = nums[-1]

        solution = solution + int(first_num + last_num)

print(f"The Solution is: {solution}")
