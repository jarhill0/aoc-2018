from aoc_input import AOCInput


def parse(inp):
    return {tuple(map(int, line.split(","))) for line in inp.value.splitlines()}


def mdist(p1, p2):
    return sum(map(lambda x: abs(x[0] - x[1]), zip(p1, p2)))


def part_a(inp):
    return len(constellations(parse(inp)))


def constellations(points):
    cs = []
    while points:
        pt = points.pop()
        joins = []
        for i, c in enumerate(cs):
            if any(mdist(pt, cpt) <= 3 for cpt in c):
                joins.append(i)
        if joins:
            c = cs[joins.pop(0)]
            c.add(pt)
            while joins:
                collapse_i = joins.pop()
                c2 = cs[collapse_i]
                c.update(c2)
                del cs[collapse_i]
            continue
        else:
            cs.append({pt})
    return cs


if __name__ == "__main__":
    INP = AOCInput(25)
    print(part_a(INP))
