from aoc_input import AOCInput

GRID_SERIAL = int(AOCInput(11).value)


def part_a():
    ans = max(((x, y) for x in range(1, 298) for y in range(1, 298)), key=square_score)
    return '{},{}'.format(*ans)


def power_level(x, y):
    rack_id = x + 10
    return (((rack_id * y + GRID_SERIAL) * rack_id) // 100 % 10) - 5


def square_score(top_left):
    x, y = top_left
    return sum(power_level(x + xi, y + yi) for xi in range(3) for yi in range(3))


def part_b():
    best = 0  # manual "max" here...
    best_val = None, None, None

    for x in range(1, 301):
        print(x)
        for y in range(1, 301):
            score = 0
            for n in range(1, 301):
                if max(x, y) + n > 300:  # invalid square
                    break

                score += sum(power_level(x + i, y + n) for i in range(n))  # the "extra" part on the bottom
                score += sum(power_level(x + n, y + i) for i in range(n - 1))  # extra on the right

                if score > best:
                    best = score
                    best_val = x, y, n

    return '{},{},{}'.format(*best_val)


def part_b_alt():
    scores = [[power_level(x, y) for x in range(1, 301)] for y in range(1, 301)]

    def square_sum(items):
        x, y, n = items
        if max(x, y) + n > 300:
            return 0
        return sum(scores[y + yi][x + xi] for xi in range(n) for yi in range(n))

    ans = max(((x, y, n) for n in range(1, 301) for x in range(1, 302 - n) for y in range(1, 302 - n)),
              key=square_sum)
    return '{},{},{}'.format(*ans)


if __name__ == '__main__':
    print(part_a())
    print(part_b_alt())
