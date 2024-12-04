from collections import defaultdict

from aoc_input import AOCInput

OPEN = int()  # zero
TREES = 1
LUMBERYARD = 2


def parse(inp):
    board = defaultdict(int)
    for r, row in enumerate(inp.splitlines()):
        for c, char in enumerate(row):
            if char == "|":
                board[(r, c)] = TREES
            elif char == "#":
                board[(r, c)] = LUMBERYARD
    return board


def neighbors_matching(board, pt, kind):
    return sum(
        (r, c) != pt and board[(r, c)] == kind
        for r in range(pt[0] - 1, pt[0] + 2)
        for c in range(pt[1] - 1, pt[1] + 2)
    )


def resource_value(board):
    wooded = sum(v == TREES for v in board.values())
    yards = sum(v == LUMBERYARD for v in board.values())
    return wooded * yards


def generation(old_board, rows, cols):
    new_board = parse("")
    for r in range(rows):
        for c in range(cols):
            pt = (r, c)
            if old_board[pt] == OPEN and neighbors_matching(old_board, pt, TREES) >= 3:
                new_board[pt] = TREES
            elif old_board[pt] == TREES:
                if neighbors_matching(old_board, pt, LUMBERYARD) >= 3:
                    new_board[pt] = LUMBERYARD
                else:
                    new_board[pt] = TREES
            elif (
                old_board[pt] == LUMBERYARD
                and neighbors_matching(old_board, pt, LUMBERYARD) >= 1
                and neighbors_matching(old_board, pt, TREES) >= 1
            ):
                new_board[pt] = LUMBERYARD

    return new_board


def part_a(inp):
    rows = len(inp.value.splitlines())
    cols = len(inp.value.splitlines()[0])

    board = parse(inp.value)
    for _ in range(10):
        board = generation(board, rows, cols)
    return resource_value(board)


def freeze(board, rows, cols):
    out = ""
    for r in range(rows):
        for c in range(cols):
            out += {OPEN: ".", TREES: "|", LUMBERYARD: "#"}[board[(r, c)]]
        out += "\n"
    return out


def part_b(inp):
    rows = len(inp.value.splitlines())
    cols = len(inp.value.splitlines()[0])

    board = parse(inp.value)
    seen = dict()
    remaining = 0
    for i in range(1000000000):
        board = generation(board, rows, cols)
        if freeze(board, rows, cols) in seen:
            cycle_length = i - seen[freeze(board, rows, cols)]
            remaining = (1000000000 - i - 1) % cycle_length
            break
        seen[freeze(board, rows, cols)] = i
    for i in range(remaining):
        board = generation(board, rows, cols)
    return resource_value(board)


if __name__ == "__main__":
    INP = AOCInput(18)
    print(part_a(INP))
    print(part_b(INP))
