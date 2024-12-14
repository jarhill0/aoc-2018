import re

from aoc_input import AOCInput


def parse(inp):
    bots = []
    for line in inp.value.splitlines():
        nums = list(map(int, re.findall(r"-?\d+", line)))
        bots.append(
            (
                tuple(
                    nums[:3],
                ),
                nums[3],
            )
        )
    return bots


def mdist(p1, p2):
    return sum(map(lambda x: abs(x[0] - x[1]), zip(p1, p2)))


def in_range(bot, other):
    return mdist(bot[0], other[0]) <= bot[1]


def part_a(inp):
    bots = parse(inp)
    strongest = max(bots, key=lambda b: b[1])
    return sum(in_range(strongest, b) for b in bots)


def part_b(inp):
    pass


if __name__ == "__main__":
    INP = AOCInput(23)
    print(part_a(INP))
    print(part_b(INP))
