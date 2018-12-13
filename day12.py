from aoc_input import AOCInput

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
            plant = STATES.get(tuple(row[i - 2: i + 3]), False)
            out.append(plant)

    return out, zero_index


def part_a():
    pots = INIT
    zero = 0
    for _ in range(20):
        pots, zero = step(pots, zero)
    return sum((i - zero) * plant for i, plant in enumerate(pots))  # True = 1; False = 0


if __name__ == '__main__':
    print(part_a())
