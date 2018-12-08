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


def part_b():
    vals = deque([int(n) for n in INP.value.split()])
    return Node(vals).value()


class Node:
    def __init__(self, vals):
        n_children = vals.popleft()
        n_metadata = vals.popleft()

        self.children = [Node(vals) for _ in range(n_children)]
        self.metadata = [vals.popleft() for _ in range(n_metadata)]

    def value(self):
        if len(self.children) == 0:
            return sum(self.metadata)

        return sum(self.children[m - 1].value() for m in self.metadata if m <= len(self.children))


if __name__ == '__main__':
    print(part_a())
    print(part_b())
