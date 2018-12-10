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


def solve():
    points = set()
    for line in INP.value.split('\n'):
        x, y, velx, vely = (int(x) for x in re.findall(r'-?\d+', line))
        points.add(Point(x, y, velx, vely))

    best = 10 ** 999
    i = 0
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
            print(i)

        if maxx - minx < best:
            best = maxx - minx
        else:
            break
        for p in points:
            p.step()
        i += 1


if __name__ == '__main__':
    solve()
