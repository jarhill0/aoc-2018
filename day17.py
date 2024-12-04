from aoc_input import AOCInput

CLAY = 1
WATER = 2


class Ground:
    def __init__(self, grid):
        self.grid = grid
        self.water_reached = set()
        self.overflowed = False
        self.min_y = min(y for _, y in self.grid)
        self.max_y = max(y for _, y in self.grid)
        self.water_source = (500, 0)

    def simulate(self):
        try:
            self.fill(self.water_source)
        except RecursionError:
            self.visualize()

    def fill(self, pt):
        if pt[1] > self.max_y or pt in self.grid:
            return
        if pt[1] >= self.min_y:
            self.water_reached.add(pt)

        below = (pt[0], pt[1] + 1)
        if (
            below not in self.grid
            and below[1] <= self.max_y
            and below not in self.water_reached
        ):
            self.fill(below)

        if below not in self.grid:
            return

        row = [pt]
        flowed_out = False
        left = (pt[0] - 1, pt[1])
        while left not in self.grid:
            row.append(left)
            self.water_reached.add(left)
            below = (left[0], left[1] + 1)
            if below not in self.grid:
                self.fill(below)
                if below not in self.grid:
                    flowed_out = True
                    break
            left = (left[0] - 1, left[1])
        right = (pt[0] + 1, pt[1])
        while right not in self.grid:
            row.append(right)
            self.water_reached.add(right)
            below = (right[0], right[1] + 1)
            if below not in self.grid:
                self.fill(below)
                if below not in self.grid:
                    flowed_out = True
                    break
            right = (right[0] + 1, right[1])

        if not flowed_out:
            for p in row:
                self.grid[p] = WATER

    def visualize(self):
        min_x = min(min(x for x, _ in self.grid), min(x for x, _ in self.water_reached))
        max_x = max(max(x for x, _ in self.grid), max(x for x, _ in self.water_reached))
        min_y = min(y for _, y in self.grid)
        max_y = max(y for _, y in self.grid)
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                square = self.grid.get((x, y))
                char = {None: " ", CLAY: "#", WATER: "~"}[square]
                if (x, y) in self.water_reached:
                    if square == CLAY:
                        char = "🙅"
                    elif square is None:
                        char = "|"
                print(char, end="")
            print("")


def parse(inp):
    grid = {}
    for line in inp.value.splitlines():
        single, _, rnge = line.partition(", ")
        mx = {"x": 0, "y": 1}
        pt = [0, 0]

        n, _, v = single.partition("=")
        pt[mx[n]] = int(v)

        n, _, r = rnge.partition("=")
        a, _, b = r.partition("..")
        for v in range(int(a), int(b) + 1):
            pt[mx[n]] = v
            grid[tuple(pt)] = CLAY
    return Ground(grid)


def part_a(inp):
    g = parse(inp)
    g.simulate()
    return len(g.water_reached)


def part_b(inp):
    g = parse(inp)
    g.simulate()
    return sum(s == WATER for s in g.grid.values())


if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(2000)

    INP = AOCInput(17)
    print(part_a(INP))
    print(part_b(INP))
