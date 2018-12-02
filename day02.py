from collections import Counter

from aoc_input import AOCInput

INP = AOCInput(2)


def part_a():
    return sum(1 if contains_exactly(w, 2) else 0 for w in INP.value.split()) * sum(1 if contains_exactly(w, 3)
                                                                                    else 0
                                                                                    for w in INP.value.split())


def contains_exactly(word, n):
    counter = Counter(word)
    for val in counter.values():
        if val == n:
            return True
    return False


def part_b():
    ids = INP.value.split()
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            if string_diff(ids[i], ids[j]) == 1:
                return common_letters(ids[i], ids[j])


def string_diff(s1, s2):
    return sum(1 if c1 != c2 else 0 for c1, c2 in zip(s1, s2))


def common_letters(s1, s2):
    return ''.join(c1 if c1 == c2 else '' for c1, c2 in zip(s1, s2))


if __name__ == '__main__':
    print(part_a())
    print(part_b())
