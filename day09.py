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


def part_b():
    pass


if __name__ == '__main__':
    print(part_a())
    print(part_b())
