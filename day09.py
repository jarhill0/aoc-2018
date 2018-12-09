from collections import defaultdict

from aoc_input import AOCInput

INP = AOCInput(9)
MARBLES = 71144
PLAYERS = 424

# MARBLES = 1618
# PLAYERS = 10




def part_a():
    circle = [0]
    current = 0
    player = 0
    score = defaultdict(int)
    for marble in range(1, MARBLES + 1):
        # print(circle)
        if marble % 23 == 0:
            score[player] += marble
            other_ind = (circle.index(current) - 7) % len(circle)
            score[player] += circle[other_ind]
            del circle[other_ind]
            current = circle[other_ind % len(circle)]
        else:
            if len(circle) == 1:
                two_right = 1
            else:
                two_right = (circle.index(current) + 2) % len(circle)
                if two_right == 0:
                    two_right = len(circle)
            circle.insert(two_right, marble)
            current = marble

        player = (player + 1) % PLAYERS

    return max(score.values())


class Marble:  # linked list thing... Cheap inserts, deletes
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


def part_b():
    current = Marble(0)
    current.left = current
    current.right = current

    player = 0
    score = defaultdict(int)
    for marble in range(1, 100 * MARBLES + 1):
        # print(circle)
        if marble % 23 == 0:
            # if marble % 1000 == 0:
            #     print('{}/{}'.format(marble, MARBLES))

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


if __name__ == '__main__':
    print(part_a())
    print(part_b())
