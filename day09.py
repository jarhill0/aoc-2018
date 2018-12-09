from collections import defaultdict

from aoc_input import AOCInput

INP = AOCInput(9)
MARBLES = int(INP.value.split()[6])
PLAYERS = int(INP.value.split()[0])


def part_a():
    return solve(MARBLES)


# The Marble class is really a circular linked list. It gives us O(1) inserts
# and O(1) removes, which is something that Python's list, which is implemented
# using arrays, doesn't give us (instead, inserts and removes are both O(n)).
# This problem is minor for part A but huge for part B.
class Marble:
    def __init__(self, num, left=None, right=None):
        self.num = num
        self.left = left
        self.right = right

        if self.left is not None:
            self.left.right = self
        if self.right is not None:
            self.right.left = self

    def remove(self):
        assert self.right is not None
        assert self.left is not None
        self.right.left = self.left
        self.left.right = self.right


# Note: this algorithm isn't as fast as I'd like (part B takes several seconds). I feel like there
# must be some underlying pattern which I haven't noticed which eliminates the need for a list of any kind.
def solve(max_marble):
    current = Marble(0)
    current.left = current  # make it
    current.right = current  # a loop!

    player = 0
    score = defaultdict(int)
    for marble in range(1, max_marble + 1):
        if marble % 23 == 0:
            score[player] += marble
            for _ in range(7):
                current = current.left
            score[player] += current.num
            current = current.right
            current.left.remove()
        else:
            current = current.right
            current = Marble(marble, left=current, right=current.right)

        player = (player + 1) % PLAYERS

    return max(score.values())


def part_b():
    return solve(100 * MARBLES)


if __name__ == '__main__':
    print(part_a())
    print(part_b())
