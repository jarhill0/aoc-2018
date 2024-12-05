from aoc_input import AOCInput


def parse(inp):
    d, t = inp.value.splitlines()
    d = int(d.split()[-1])
    t = t.split()[-1]
    t = tuple(int(x) for x in t.split(","))
    return d, t


ROCKY = 0
WET = 1
NARROW = 2

MODULO = 20183


class Map:
    def __init__(self, depth, target):
        self.depth = depth
        self.target = target
        self.el = {(0, 0): depth % MODULO}
        self.region_kind(target)  # init for part 1
        self.el[target] = depth % MODULO

    def region_kind(self, at):
        return self.erosion_level(at) % 3

    def erosion_level(self, at):
        if at not in self.el:
            x, y = at
            if y == 0:
                geologic_index = 16807 * x
            elif x == 0:
                geologic_index = 48271 * y
            else:
                geologic_index = self.erosion_level((x - 1, y)) * self.erosion_level(
                    (x, y - 1)
                )
            self.el[at] = (geologic_index + self.depth) % MODULO

        return self.el[at]


def part_a(inp):
    grid = Map(*parse(inp))
    return sum(v % 3 for v in grid.el.values())


def part_b(inp):
    depth, target = parse(inp)
    maze = Map(depth, target)
    return fastest_route(maze, target)


TORCH = 101
GEAR = 102
NEITHER = 100

ALLOWED = {ROCKY: {TORCH, GEAR}, WET: {GEAR, NEITHER}, NARROW: {TORCH, NEITHER}}


def fastest_route(maze, target):
    gen = {((0, 0), TORCH): 0}
    been = {((0, 0), TORCH)}
    length = 0
    while True:
        next_gen = dict()
        for (pt, tool), wait_remaining in gen.items():
            if wait_remaining > 0:
                next_gen[(pt, tool)] = wait_remaining - 1
                continue

            if pt == target:
                if tool == TORCH:
                    return length
                return length + 7

            pt_kind = maze.region_kind(pt)
            other_tool = next(iter(ALLOWED[pt_kind].difference({tool})))
            if (pt, other_tool) not in been:
                next_gen[(pt, other_tool)] = (
                    6  # this iteration counts as our first minute of wait
                )
                been.add((pt, other_tool))

            for neighbor in neighbors(pt):
                neighbor_kind = maze.region_kind(neighbor)
                neighbor_tools = ALLOWED[neighbor_kind]
                if tool in neighbor_tools:
                    if (neighbor, tool) not in been:
                        next_gen[(neighbor, tool)] = 0
                        been.add((neighbor, tool))

        length += 1
        gen = next_gen


def neighbors(pt):
    x, y = pt
    n = {(x + 1, y), (x, y + 1)}
    if x > 0:
        n.add((x - 1, y))
    if y > 0:
        n.add((x, y - 1))
    return n


if __name__ == "__main__":
    INP = AOCInput(22)
    print(part_a(INP))
    print(part_b(INP))