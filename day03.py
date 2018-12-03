from collections import namedtuple

from aoc_input import AOCInput

INP = AOCInput(3)

Rectangle = namedtuple('Rectangle', 'name x y width height')

RECTANGLES = []


def parse_rects():
    for line in INP.value.split('\n'):
        # "#1 @ 257,829: 10x23"
        words = line.split()
        name = words[0].lstrip("#")
        x, y = (int(n) for n in words[2].rstrip(':').split(','))
        w, h = (int(n) for n in words[3].split('x'))
        RECTANGLES.append(Rectangle(name, x, y, w, h))


def rect_iter(rect):
    for x in range(rect.x, rect.x + rect.width):
        for y in range(rect.y, rect.y + rect.height):
            yield (x, y)


def part_a():  # O(nwh), where n is the number of rectangles and w/h are the average width and height
    claimed = set()
    double_claimed = set()
    for rect in RECTANGLES:
        for inch in rect_iter(rect):
            if inch in claimed:
                double_claimed.add(inch)
            else:
                claimed.add(inch)
    return len(double_claimed)


def part_b():  # O(nwh), where n is the number of rectangles and w/h are the average width and height
    claimed = dict()
    for rect in RECTANGLES:
        for inch in rect_iter(rect):
            if inch in claimed:
                claimed[inch] = 'BAD'  # it's disputed... no ID may own it.
            else:
                claimed[inch] = rect.name  # staking a claim

    for rect in RECTANGLES:
        perfect = True
        for inch in rect_iter(rect):
            if claimed[inch] != rect.name:  # every inch needs to be named for this section
                perfect = False
                break

        if perfect:  # exactly one...
            return rect.name


if __name__ == '__main__':
    parse_rects()
    print(part_a())
    print(part_b())
