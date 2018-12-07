import re
from collections import Counter, defaultdict

from aoc_input import AOCInput

INP = AOCInput(6)
POINTS = [tuple(int(x) for x in re.findall(r'\d+', l)) for l in INP.value.split('\n')]


def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def part_a():
    maxx = max(p[0] for p in POINTS)
    minx = min(p[0] for p in POINTS)
    maxy = max(p[1] for p in POINTS)
    miny = min(p[1] for p in POINTS)

    claimed = defaultdict(int)
    infinite = defaultdict(bool)

    for x in range(minx, maxx + 1):
        for y in range(miny, maxy + 1):
            distances = {point: manhattan_dist(point, (x, y)) for point in POINTS}
            to_point = min(distances.keys(), key=distances.get)

            if Counter(distances.values())[distances[to_point]] == 1:  # if the minimum is UNIQUE
                claimed[to_point] += 1
            if x in (minx, maxx) or y in (miny, maxy):  # anything that has points on the edge has infinite points
                infinite[to_point] = True

    return max(claimed[p] for p in POINTS if not infinite[p])


def part_b():
    maxx = max(p[0] for p in POINTS)
    minx = min(p[0] for p in POINTS)
    maxy = max(p[1] for p in POINTS)
    miny = min(p[1] for p in POINTS)

    return sum(1
               for x in range(minx, maxx + 1)
               for y in range(miny, maxy + 1)
               if sum(manhattan_dist(point, (x, y)) for point in POINTS) < 10000)


if __name__ == '__main__':
    print(part_a())
    print(part_b())
