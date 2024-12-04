from aoc_input import AOCInput


def parse(inp):
    d, t = inp.value.splitlines()
    d = int(d.split()[-1])
    t = t.split()[-1]
    t = tuple(int(x) for x in t.split(","))
    return d, t


MODULO = 20183


def erosion_levels(depth, target):
    el = {(0, 0): depth % MODULO}

    def el_inner(at):
        if at not in el:
            x, y = at
            if y == 0:
                geologic_index = 16807 * x
            elif x == 0:
                geologic_index = 48271 * y
            else:
                geologic_index = el_inner((x - 1, y)) * el_inner((x, y - 1))
            el[at] = (geologic_index + depth) % MODULO

        return el[at]

    el_inner(target)  # memoize it up

    el[target] = depth % MODULO

    return el


def part_a(inp):
    grid = erosion_levels(*parse(inp))
    return sum(v % 3 for v in grid.values())


def part_b(inp):
    pass


if __name__ == "__main__":
    INP = AOCInput(22)
    print(part_a(INP))
    print(part_b(INP))
