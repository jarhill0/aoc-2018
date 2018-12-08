from collections import deque

from aoc_input import AOCInput

INP = AOCInput(8)


def part_a():
    vals = deque([int(n) for n in INP.value.split()])
    return sum_metadata(vals)


def sum_metadata(vals):
    n_children = vals.popleft()
    n_metadata = vals.popleft()

    metadata_sum = sum(sum_metadata(vals) for _ in range(n_children))
    metadata_sum += sum(vals.popleft() for _ in range(n_metadata))

    return metadata_sum


if __name__ == '__main__':
    print(part_a())
