import re
from collections import defaultdict

from aoc_input import AOCInput

TEXT = AOCInput(4).value.split('\n')
TEXT.sort()  # since each line is in YYYY-MM-DD HH:MM, it is easy to sort by string ordering

ROWS = [[*map(int, re.findall(r'\d+', l))] for l in TEXT if l]  # parse out all the ints


def part_a():
    guards = defaultdict(lambda: defaultdict(int))

    for text_line, number_line in zip(TEXT, ROWS):
        minute = number_line[4]
        name = number_line[5] if len(number_line) == 6 else None  # len 6 when ID in the line

        if name is not None:
            current_guard = name

        if 'falls' in text_line:
            time_fell = minute

        if 'wakes' in text_line:
            for minute in range(time_fell, minute):
                guards[current_guard][minute] += 1

    sleepiest_guard = max(guards.keys(), key=lambda g: sum(guards[g].values()))
    sleepiest_minute = max(guards[sleepiest_guard].keys(), key=lambda min: guards[sleepiest_guard][min])
    return sleepiest_guard * sleepiest_minute


def part_b():
    guards = defaultdict(lambda: defaultdict(int))

    for text_line, number_line in zip(TEXT, ROWS):
        minute = number_line[4]
        name = number_line[5] if len(number_line) == 6 else None  # len 6 when ID in the line

        if name is not None:
            current_guard = name

        if 'falls' in text_line:
            time_fell = minute

        if 'wakes' in text_line:
            for minute in range(time_fell, minute):
                guards[current_guard][minute] += 1

    sleepiest_minute = {guard: max(guards[guard].keys(), key=lambda m: guards[guard][m]) for guard in guards.keys()}
    sleepiest_guard = max(guards.keys(), key=lambda g: guards[g][sleepiest_minute[g]])
    return sleepiest_guard * sleepiest_minute[sleepiest_guard]


if __name__ == '__main__':
    print(part_a())
    print(part_b())
