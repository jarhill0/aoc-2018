import re
from collections import defaultdict

from aoc_input import AOCInput

TEXT = AOCInput(4).value.split('\n')
TEXT.sort()  # since each line is in YYYY-MM-DD HH:MM, it is easy to sort by string ordering

# parse out the relevant ints
# this splits each line on the time colon since we only care about the minute and the guard ID.
ROWS = [['falls' in l, 'wakes' in l, *map(int, re.findall(r'\d+', l.partition(':')[2]))] for l in TEXT if l]


def part_a():
    guards = defaultdict(lambda: defaultdict(int))

    for line in ROWS:
        fell_asleep, woke_up, minute = line[:3]
        name = line[3] if len(line) == 4 else None  # len 4 when ID in the line

        if name is not None:
            current_guard = name

        if fell_asleep:
            time_fell = minute

        if woke_up:
            for minute in range(time_fell, minute):
                guards[current_guard][minute] += 1

    sleepiest_guard = max(guards.keys(), key=lambda g: sum(guards[g].values()))
    sleepiest_minute = max(guards[sleepiest_guard].keys(), key=lambda min: guards[sleepiest_guard][min])
    return sleepiest_guard * sleepiest_minute


def part_b():
    guards = defaultdict(lambda: defaultdict(int))

    for line in ROWS:
        fell_asleep, woke_up, minute = line[:3]
        name = line[3] if len(line) == 4 else None  # len 4 when ID in the line

        if name is not None:
            current_guard = name

        if fell_asleep:
            time_fell = minute

        if woke_up:
            for minute in range(time_fell, minute):
                guards[current_guard][minute] += 1

    sleepiest_minute = {guard: max(guards[guard].keys(), key=lambda m: guards[guard][m]) for guard in guards.keys()}
    sleepiest_guard = max(guards.keys(), key=lambda g: guards[g][sleepiest_minute[g]])
    return sleepiest_guard * sleepiest_minute[sleepiest_guard]


if __name__ == '__main__':
    print(part_a())
    print(part_b())
