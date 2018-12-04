import re
from collections import defaultdict

from aoc_input import AOCInput

INP = AOCInput(4)

TEXT = INP.value.split('\n')
TEXT.sort()

ROWS = [[*map(int, re.findall(r'\d+', l))] for l in TEXT if l]


def part_a():
    sleeps = dict()
    guard = 0
    time_fell = -1
    for i, line in enumerate(ROWS):
        name = None
        if len(line) == 5:
            year, month, day, hour, minute = line
        else:
            year, month, day, hour, minute, name = line

        if name is not None:
            guard = name

        if 'falls' in TEXT[i]:
            time_fell = minute

        if 'wakes' in TEXT[i]:
            time_sleep = sleeps.get(guard, 0)
            sleeps[guard] = time_sleep + (minute - time_fell)

    best = 0
    guardbest = ''
    for guard in sleeps:
        if sleeps[guard] > best:
            best = sleeps[guard]
            guardbest = guard

    asleep = dict()
    for i, line in enumerate(ROWS):
        name = None
        if len(line) == 5:
            year, month, day, hour, minute = line
        else:
            year, month, day, hour, minute, name = line

        if name is not None:
            guard = name

        if guard == guardbest:
            if 'falls' in TEXT[i]:
                time_fell = minute

            if 'wakes' in TEXT[i]:
                for t in range(time_fell, minute):
                    v = asleep.get(t, 0)
                    asleep[t] = v + 1

    return max(asleep, key=lambda m: asleep[m]) * guardbest


def part_b():
    guards = defaultdict(dict)
    guard = 0
    time_fell = -1
    for i, line in enumerate(ROWS):
        name = None
        if len(line) == 5:
            year, month, day, hour, minute = line
        else:
            year, month, day, hour, minute, name = line

        if name is not None:
            guard = name

        if 'falls' in TEXT[i]:
            time_fell = minute

        if 'wakes' in TEXT[i]:
            for t in range(time_fell, minute):
                gdict = guards[guard]
                gdict[t] = gdict.get(t, 0) + 1

    bestguard = ''
    most_asleep = 0
    bmin = None
    for guard in guards:
        gdict = guards[guard]
        for min in gdict:
            asleep = gdict[min]
            if asleep > most_asleep:
                most_asleep = asleep
                bmin = min
                bestguard = guard

    return bestguard * bmin


if __name__ == '__main__':
    print(part_a())
    print(part_b())
