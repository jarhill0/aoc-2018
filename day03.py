from aoc_input import AOCInput

INP = AOCInput(3)


def part_a():
    claimed = set()
    double_claimed = set()
    for line in INP.value.split('\n'):
        # "#1 @ 257,829: 10x23"
        words = line.split()
        x, y = words[2].rstrip(':').split(',')
        w, h = words[3].split('x')
        x, y, w, h = int(x), int(y), int(w), int(h)
        for xi in range(x, x + w):
            for yi in range(y, y + h):
                inch = (xi, yi)
                if inch in claimed:
                    double_claimed.add(inch)
                else:
                    claimed.add(inch)
    return len(double_claimed)


def part_b():
    claimed = dict()
    for line in INP.value.split('\n'):
        # "#1 @ 257,829: 10x23"
        words = line.split()
        name = words[0].lstrip("#")
        x, y = words[2].rstrip(':').split(',')
        w, h = words[3].split('x')
        x, y, w, h = int(x), int(y), int(w), int(h)

        for xi in range(x, x + w):
            for yi in range(y, y + h):
                inch = (xi, yi)
                if inch in claimed:
                    claimed[inch] = 'BAD'
                else:
                    claimed[inch] = name

    for line in INP.value.split('\n'):
        # "#1 @ 257,829: 10x23"
        words = line.split()
        name = words[0].lstrip("#")
        x, y = words[2].rstrip(':').split(',')
        w, h = words[3].split('x')
        x, y, w, h = int(x), int(y), int(w), int(h)

        perfect = True
        for xi in range(x, x + w):
            for yi in range(y, y + h):
                inch = (xi, yi)
                if claimed[inch] != name:
                    perfect = False

        if perfect:
            return name


if __name__ == '__main__':
    print(part_a())
    print(part_b())
