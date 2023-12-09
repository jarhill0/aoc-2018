from collections import defaultdict

from aoc_input import AOCInput


def parse(inp):
    lines = inp.value.splitlines()
    _, _, initial = lines[0].partition(": ")
    init = defaultdict(bool)
    for i, state in enumerate(initial):
        if state == "#":
            init[i] = True

    rules = {}
    for r in lines[2:]:
        start, _, result = r.partition(" => ")
        st = tuple(c == "#" for c in start)
        rules[st] = result == "#"

    return init, PlantRules(rules)


class PlantRules:
    def __init__(self, rules):
        self.rules = rules

    def next_generation(self, in_plants):
        next_plants = defaultdict(bool)
        for p in range(min(in_plants) - 2, max(in_plants) + 3):
            next_plants[p] = self.plant_at(p, in_plants)
        return next_plants

    def plant_at(self, p, plants):
        key = tuple(plants[i] for i in range(p - 2, p + 3))
        return self.rules.get(key, False)


def part_a(inp):
    plants, rules = parse(inp)
    for _ in range(20):
        plants = rules.next_generation(plants)
    return plant_score(plants)


def plant_score(plants):
    return sum(num for num, p in plants.items() if p)


def part_b(inp):
    pass


if __name__ == "__main__":
    INP = AOCInput(12)
    print(part_a(INP))
    print(part_b(INP))
