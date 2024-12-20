from aoc_input import AOCInput


def part_a(inp):
    return next(program())


def part_b(inp):
    prev = None
    seen = set()
    for val_attained in program():
        if val_attained in seen:
            return prev

        seen.add(val_attained)
        prev = val_attained


# Run the program and then return values that reg[3] attains at the equality check
def program():  # my input
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

            four = four // 256

            # goto 8

        yield three
        # if three == zero:  # "do-while"
        #     return
        # goto 6


if __name__ == "__main__":
    INP = AOCInput(21)
    print(part_a(INP))
    print(part_b(INP))
