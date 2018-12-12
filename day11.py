from aoc_input import AOCInput

GRID_SERIAL = int(AOCInput(11).value)


def part_a():
    ans = max(((x, y) for x in range(1, 298) for y in range(1, 298)), key=square_score)
    return '{},{}'.format(*ans)


def power_level(x, y):
    rack_id = x + 10
    return (((rack_id * y + GRID_SERIAL) * rack_id) // 100 % 10) - 5


def square_score(top_left, n=3):
    x, y = top_left
    return sum(power_level(x + xi, y + yi) for xi in range(n) for yi in range(n))


def part_b():
    best = 0  # manual "max" here...
    best_val = None, None, None

    for n in range(1, 301):
        for x in range(1, 301):
            for y in range(1, 301):
                if max(x, y) + n > 300:  # invalid square
                    break

                score = square_score((x, y), n)

                if score > best:
                    best = score
                    best_val = x, y, n
                    print(best)
                    print(best_val)

    return '{},{},{}'.format(*best_val)


if __name__ == '__main__':
    print(part_a())
    part_b()
