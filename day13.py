from aoc_input import AOCInput


def parse(inp):
    return Track(inp.value)


RIGHT = 0
DOWN = 1
LEFT = 2
UP = 3

DIRECTIONS = {">": RIGHT, "v": DOWN, "<": LEFT, "^": UP}
MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]

SLASH_TURNS = {RIGHT: UP, UP: RIGHT, LEFT: DOWN, DOWN: LEFT}
BACKSLASH_TURN = {RIGHT: DOWN, DOWN: RIGHT, LEFT: UP, UP: LEFT}


class Track:
    def __init__(self, inp):
        self.carts = {}
        for r, row in enumerate(inp.splitlines()):
            for c, char in enumerate(row):
                if char in DIRECTIONS:
                    self.carts[(r, c)] = (DIRECTIONS[char], -1)

        self.map = (
            inp.replace(">", "-")
            .replace("<", "-")
            .replace("v", "|")
            .replace("^", "|")
            .splitlines()
        )
        self.crash = None

    def at(self, r, c):
        return self.map[r][c]

    def tick(self):
        new_carts = {}
        for cart in sorted(self.carts):
            if cart not in self.carts:
                # something else crashed into us
                continue
            facing, turn = self.carts.pop(cart)
            r, c = cart

            dr, dc = MOVES[facing]
            r += dr
            c += dc

            if (r, c) in self.carts:
                del self.carts[(r, c)]
                self.crash = (r, c)
                continue
            elif (r, c) in new_carts:
                del new_carts[(r, c)]
                self.crash = (r, c)
                continue

            if self.at(r, c) == "+":
                new_carts[(r, c)] = ((facing + turn) % len(DIRECTIONS), next_turn(turn))
            elif self.at(r, c) == "/":
                new_carts[(r, c)] = (SLASH_TURNS[facing], turn)
            elif self.at(r, c) == "\\":
                new_carts[(r, c)] = (BACKSLASH_TURN[facing], turn)
            else:
                new_carts[(r, c)] = (facing, turn)

        self.carts = new_carts


def next_turn(turn):
    return (turn + 2) % 3 - 1


def part_a(inp):
    track = parse(inp)
    while not track.crash:
        track.tick()
    return f"{track.crash[1]},{track.crash[0]}"


def part_b(inp):
    track = parse(inp)
    while len(track.carts) > 1:
        track.tick()
    cart = next(iter(track.carts))
    return f"{cart[1]},{cart[0]}"


if __name__ == "__main__":
    INP = AOCInput(13)
    print(part_a(INP))
    print(part_b(INP))
