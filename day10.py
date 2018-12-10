import re
from time import sleep

from aoc_input import AOCInput

INP = AOCInput(10)


class Point:
    def __init__(self, x, y, velx, vely):
        self.x = x
        self.y = y
        self.velx = velx
        self.vely = vely

    def step(self, n=1):
        self.x += self.velx * n
        self.y += self.vely * n

    def __repr__(self):
        return str([self.x, self.y, self.velx, self.vely])


def part_a():
    points = set()
    for line in INP.value.split('\n'):
        x, y, velx, vely = (int(x) for x in re.findall(r'-?\d+', line))
        points.add(Point(x, y, velx, vely))

    # pick two random points, say we want them within a certain threshold of each other
    left = min(points, key=lambda p: p.x)
    right = max(points, key=lambda p: p.x)

    # diff = (m_1 * x + b_1) - (m_2 * x + b_2)
    #      = x * (m_1 - m_2) + b_1 - b_2
    # diff + b_2 - b_1 = x * (m_1 - m_2)
    # (diff + b_2 - b_1) / (m_1 - m_2) = x
    big_step = (500 + left.x - right.x) // (right.velx - left.velx)

    for p in points:
        p.step(big_step)
    while True:
        maxx = max(p.x for p in points)
        minx = min(p.x for p in points)
        maxy = max(p.y for p in points)
        miny = min(p.y for p in points)

        if (maxx - minx) < 160:  # guess
            coords = {(p.x, p.y) for p in points}

            for y in range(miny, maxy + 1):
                for x in range(minx, maxx + 1):
                    print('#' if (x, y) in coords else '.', end='')
                print()  # newline

            sleep(1)

        for p in points:
            p.step()


def part_b():
    pass


if __name__ == '__main__':
    print(part_a())
    print(part_b())
