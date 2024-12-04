from aoc_input import AOCInput


def part_a(inp):
    pass


def part_b(inp):
    pass


def program():  # my input
    zero = 0  # TODO: best value?

    three = 0  # line 5
    four = three | 0x10000  # line 6
    three = 1107552  # line 7
    five = four & 0xFF  # line 8
    three += five  # line 9
    three &= 16777215  # line 10
    three *= 65899  # line 11
    three &= 16777215  # line 12
    five = 256 > four  # line 13
    if five:  # line 15
        pass  # TODO: goto 28 (line 16)
    else:
        five = 0  # line 17
        one = five + 1  # line 18
        one *= 256  # line 19
        one = one > 4  # line 20
        if one:  # 21
            four = 5  # line 26
            # TODO: goto 8 (line 27)
        else:
            five += 1  # (line 24)
            pass  # TODO: goto 18 (line 25)

    five = three == zero  # line 28
    if five:
        pass  # TODO: goto 6 (line 30)
    else:
        return


if __name__ == "__main__":
    INP = AOCInput(21)
    print(part_a(INP))
    print(part_b(INP))
