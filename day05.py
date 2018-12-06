from aoc_input import AOCInput

INP = AOCInput(5)


def opp_polarity(a, b):
    return a.lower() == b.lower() and a.islower() != b.islower()


def part_a():
    return len(react(INP.value))


def react(polymer):
    stack = []

    for c in polymer:
        if len(stack) > 0 and opp_polarity(stack[-1], c):
            stack.pop()  # remove the last element because it reacts with element c
        else:
            stack.append(c)

    return stack


def part_b():
    polymer_types = set(INP.value.lower())
    return min(len(react(INP.value.replace(p_type, '').replace(p_type.upper(), ''))) for p_type in polymer_types)


if __name__ == '__main__':
    print(part_a())
    print(part_b())
