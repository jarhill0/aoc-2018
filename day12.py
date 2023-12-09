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
            if self.plant_at(p, in_plants):
                next_plants[p] = True
        return next_plants

    def plant_at(self, p, plants):
        key = tuple(plants[i] for i in range(p - 2, p + 3))
        return self.rules.get(key, False)


def part_a(inp):
    plants, rules = parse(inp)
    for _ in range(20):
        plants = rules.next_generation(plants)
    return plant_score(plants)


def plant_score(plants, offset=0):
    return sum(num + offset for num, p in plants.items() if p)


def part_b(inp):
    seen = SeenStates()
    plants, rules = parse(inp)
    i = 0

    while plants not in seen:
        seen.add(plants)
        plants = rules.next_generation(plants)
        i += 1

    # at this point, my plants settle into a steady state (subject to offset),
    # much like a spaceship/glider in a cellular automaton:
    # <https://en.wikipedia.org/wiki/Spaceship_(cellular_automaton)>
    # <https://en.wikipedia.org/wiki/Glider_(Conway%27s_Game_of_Life)>

    # On my input, the plants drift right by one place each iteration,
    # with a loop period of 1. A more general solution for inputs of this
    # type could actually figure out what the drift and period are, but I
    # assume all the inputs actually have this feature as well.

    remaining_steps = 50_000_000_000 - i

    return plant_score(plants, remaining_steps)


class SeenStates(set):
    def add(self, state):
        super().add(self.key(state))

    def __contains__(self, item):
        return super().__contains__(self.key(item))

    def key(self, state):
        return tuple(sorted(self.normalize(state)))

    @staticmethod
    def normalize(plants):
        new = set()
        smallest = min(i for i, p in plants.items() if p)
        for i, p in plants.items():
            if p:
                new.add(i - smallest)
        return new


if __name__ == "__main__":
    INP = AOCInput(12)
    print(part_a(INP))
    print(part_b(INP))
