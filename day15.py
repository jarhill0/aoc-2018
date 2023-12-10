from aoc_input import AOCInput


WALL = 1
GOBLIN = 2
ELF = 4


def map_str(thing):
    if thing is None:
        return "."
    kind = thing[0]
    if kind == WALL:
        return "#"
    if kind == GOBLIN:
        return "G"
    if kind == ELF:
        return "E"
    raise "unknown"


class Combat:
    def __init__(self, board):
        self.board = board
        self.rounds_completed = 0
        self.game_over = False

    def __str__(self):
        max_r = max(r for r, c in self.board)
        max_c = max(c for r, c in self.board)
        return (
            f"After {self.rounds_completed} rounds:\n"
            + "\n".join(
                "".join((map_str(self.board.get((r, c))) for c in range(max_c + 1)))
                + "   "
                + self.healths(r, max_c + 1)
                for r in range(max_r + 1)
            )
            + "\n"
        )

    def healths(self, r, max_c):
        out = []
        for c in range(max_c):
            if (r, c) in self.board:
                kind, _, health = self.board[(r, c)]
                if kind == WALL:
                    continue
                out.append(f'{"G" if kind == GOBLIN else "E"}({health})')
        return ", ".join(out)

    def round(self):
        for unit_coord in sorted(self.board):
            self.unit_turn(unit_coord)
            if self.game_over:
                return
        self.rounds_completed += 1

    def unit_turn(self, unit_coord):
        unit = self.board.get(unit_coord)
        if not unit or unit[0] == WALL:
            return

        unit_type, _, _ = unit
        targets = self.targets_for(unit_type)
        if not targets:
            self.game_over = True
            return

        squares_in_range = self.in_range(unit_coord, targets)
        if unit_coord not in squares_in_range:
            unit_coord = self.unit_move(unit_coord, squares_in_range)

        self.attack(unit_coord, targets)

    def targets_for(self, unit_type):
        target_type = GOBLIN if unit_type == ELF else ELF
        return {coord for coord, unit in self.board.items() if unit[0] == target_type}

    def in_range(self, unit_coord, targets):
        found = set()
        for target_coord in targets:
            tr, tc = target_coord
            for square in [(tr - 1, tc), (tr, tc - 1), (tr, tc + 1), (tr + 1, tc)]:
                if square == unit_coord or square not in self.board:
                    found.add(square)
        return found

    def unit_move(self, unit_coord, dest_coords):
        chosen_dest = None
        shortest_dist = float("inf")
        for dest_coord in sorted(dest_coords):
            dist = self.dist(unit_coord, dest_coord)
            if dist < shortest_dist:
                shortest_dist = dist
                chosen_dest = dest_coord

        if chosen_dest is None:
            return unit_coord

        return self.unit_step(unit_coord, chosen_dest)

    def unit_step(self, unit_coord, dest_coord):
        r, c = unit_coord
        chosen_step = None
        shortest_dist = float("inf")
        for step in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
            if step in self.board:
                continue
            dist = self.dist(step, dest_coord)
            if dist < shortest_dist:
                shortest_dist = dist
                chosen_step = step

        assert chosen_step is not None

        unit = self.board.pop(unit_coord)
        self.board[chosen_step] = unit
        return chosen_step

    def dist(self, start, end):
        # BFS
        visited = {start}
        batch = [start]
        d = 0

        while batch and end not in batch:
            d += 1
            next_batch = []
            for st in batch:
                r, c = st
                for sq in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
                    if sq not in self.board and sq not in visited:
                        visited.add(sq)
                        next_batch.append(sq)
            batch = next_batch

        if not batch:
            return float("inf")
        return d

    def attack(self, unit_coord, targets):
        _, my_attack_power, _ = self.board[unit_coord]
        r, c = unit_coord
        chosen_target = None
        least_hitpoints = float("inf")
        for target in [(r - 1, c), (r, c - 1), (r, c + 1), (r + 1, c)]:
            if target in targets and self.board[target][2] < least_hitpoints:
                least_hitpoints = self.board[target][2]
                chosen_target = target

        if chosen_target is None:
            return

        target_kind, target_attack_power, target_health = self.board[chosen_target]
        new_health = target_health - my_attack_power
        if new_health <= 0:
            del self.board[chosen_target]
        else:
            self.board[chosen_target] = (target_kind, target_attack_power, new_health)

    def outcome(self):
        return self.rounds_completed * self.total_hit_points()

    def total_hit_points(self):
        return sum(hit_points for _, _, hit_points in self.board.values())


def parse(inp):
    board = {}
    for r, row in enumerate(inp.value.splitlines()):
        for c, char in enumerate(row):
            if char == "#":
                board[(r, c)] = (WALL, 0, 0)
            elif char == "G":
                board[(r, c)] = (GOBLIN, 3, 200)
            elif char == "E":
                board[(r, c)] = (ELF, 3, 200)
    return Combat(board)


def part_a(inp):
    combat = parse(inp)
    while not combat.game_over:
        combat.round()
    return combat.outcome()


def part_b(inp):
    return None


if __name__ == "__main__":
    INP = AOCInput(15)
    print(part_a(INP))
    print(part_b(INP))
