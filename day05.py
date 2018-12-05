from aoc_input import AOCInput

INP = AOCInput(5)


def opp_polarity(a, b):
    return a.lower() == b.lower() and a.islower() != b.islower()


def part_a():
    return len(react(INP.value))


def react(polymer):
    p = list(polymer)

    i = 0
    while i + 1 < len(p):
        if opp_polarity(p[i], p[i + 1]):
            del p[i]
            del p[i]  # p[i + 1], but shifted left now!
            if i >= 1:
                i -= 1  # we might have created a new collision, so backtrack.
        else:  # don't increment when we've just deleted.
            i += 1
    return p


def part_b():
    polymer_types = set(INP.value.lower())
    return min(len(react(INP.value.replace(p_type, '').replace(p_type.upper(), ''))) for p_type in polymer_types)


if __name__ == '__main__':
    print(part_a())
    print(part_b())
