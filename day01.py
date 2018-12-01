from aoc_input import AOCInput

INP = AOCInput(1)


def part_a():
    return sum(int(x) for x in INP.value.split())


def part_b():
    freqs = set()
    total = 0
    while True:
        for x in INP.value.split():
            x = int(x)
            total += x
            if total in freqs:
                return total
            freqs.add(total)


if __name__ == '__main__':
    print(part_a())
    print(part_b())
