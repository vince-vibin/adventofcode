""" https://adventofcode.com/2023/day/9 """

solution = []

def get_nxt_history(history):
    nxt_history = []
    for i, number in enumerate(history[1:]):
        nxt_history.append(number - history[i])
    return nxt_history

def extrapolate(last_elements, first):
    for element in reversed(last_elements):
        first += element
    return first

with open("./input.txt", encoding="utf-8") as input_file:
    histories = input_file.readlines()
    histories = [history.rstrip() for history in histories]

for history in histories:
    numbers = [int(number) for number in history.split(" ")]
    last_elements = [numbers[-1]]
    nxt_history = get_nxt_history(numbers)

    while not all(x == nxt_history[0] for x in nxt_history):
        last_elements.append(nxt_history[-1])
        nxt_history = get_nxt_history(nxt_history)

    solution.append(extrapolate(last_elements, nxt_history[0]))

solution = sum(solution)
print(f"The Solution is: {solution}")
