import re
from collections import defaultdict

from aoc_input import AOCInput

INP = AOCInput(6)
POINTS = [tuple(int(x) for x in re.findall(r'\d+', l)) for l in INP.value.split('\n')]


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def part_a():
    dists = defaultdict(dict)
    claimed = defaultdict(list)

    for point in POINTS:
        dist = dists[point]
        dist[point] = 0
        stack = [point]
        infinite = False

        while len(stack) > 0:
            x, y = stack.pop()
            if any(manhattan_dist(p_other, (x, y)) <= dist[x, y] if p_other != point else False for p_other in POINTS):
                continue
            claimed[point].append((x, y))
            if dist[x, y] > 300:  # infinite
                infinite = True
                break
            for adj in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                if adj not in dist:
                    dist[adj] = dist[x, y] + 1
                    stack.append(adj)

        if infinite:
            claimed[point] = []

    return max(len(claimed[p]) for p in POINTS)


def part_b():
    pass


if __name__ == '__main__':
    print(part_a())
    print(part_b())
