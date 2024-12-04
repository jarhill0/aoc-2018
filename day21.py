from aoc_input import AOCInput


def part_a(inp):
    program()


def part_b(inp):
    pass


def program():  # my input
    zero = 0  # TODO: best value?

    three = 0  # line 5
    while True:
        four = three | 0x10000  # line 6
        three = 1107552  # line 7
        while True:
            three += four & 0xFF
            three &= 0xFFFFFF  # line 10
            three *= 65899  # line 11
            three &= 0xFFFFFF  # line 12

            if 256 > four:  # line 13–14
                break

            j = 0  # line 17
            while not (256 * (j + 1) > four):
                j += 1  # (line 24)
            four = j  # line 26
            # goto 8

        if three != zero:  # "do-while"
            return
        # goto 6


if __name__ == "__main__":
    INP = AOCInput(21)
    print(part_a(INP))
    print(part_b(INP))