from aoc_input import AOCInput
from linked_list import LinkedList

INP = AOCInput(12)

INIT = [c == '#' for c in INP.value.split('\n')[0].partition(': ')[2]]
STATES = dict()

for line in INP.value.split('\n'):
    if ' => ' in line:
        start, _, end = line.partition(' => ')
        assert len(start) == 5
        assert len(end) == 1

        start = tuple(c == '#' for c in start)
        end = end == '#'
        STATES[start] = end

assert len(STATES) == 2 ** 5
# note: this code assumes ..... => . is always true. Otherwise the problem is way harder.
assert not STATES[(False, False, False, False, False)]


def step(row, zero_index):
    if len(row) < 5:
        return row, zero_index

    while any(row[:5]):  # those should all be false
        row.insert(0, False)
        zero_index += 1  # what we think of as "zero" has shifted
    while any(row[-5:]):  # those should also all be false
        row.append(False)

    out = []
    for i in range(len(row)):
        if i < 2 or i >= len(row) - 2:  # boundary conditions
            out.append(row[i])
        else:
            out.append(STATES[tuple(row[i - 2: i + 3])])

    return out, zero_index


def part_a():
    pots = list(INIT)
    zero = 0
    for _ in range(20):
        pots, zero = step(pots, zero)
    return sum((i - zero) * plant for i, plant in enumerate(pots))  # True = 1; False = 0


def part_b():
    plants = {i for i, pot in enumerate(INIT) if pot}
    worklist = LinkedList()

    for _ in range(50000000000):
        new_plants = set()
        worklist.clear()
        for i in range(min(plants) - 5, max(plants) + 8):
            worklist.append(i in plants)
            if len(worklist) < 5:
                continue
            while len(worklist) > 5:
                del worklist[0]

            if STATES[tuple(worklist)]:
                new_plants.add(i - 2)
        plants = new_plants
    return sum(plants)


if __name__ == '__main__':
    print(part_a())
    print(part_b())
