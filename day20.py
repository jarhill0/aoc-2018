from aoc_input import AOCInput


class Map:
    def __init__(self, regex):
        self.rooms = dict()
        self.origin = self.room(0, 0)
        self.regex = regex

    def room(self, x, y):
        if (x, y) not in self.rooms:
            self.rooms[(x, y)] = Room(x, y, self.room)
        return self.rooms[(x, y)]

    def explore(self, ri=0, start=None, in_or=False):
        if start is None:
            start = MultiRoom([self.origin])

        current = start

        while ri < len(self.regex):
            c = self.regex[ri]
            ri += 1
            if c == "N":
                current = current.north()
            elif c == "E":
                current = current.east()
            elif c == "S":
                current = current.south()
            elif c == "W":
                current = current.west()
            elif c == "(":
                ri, current = self.explore(ri, start=current)
            elif c == ")":
                if in_or:
                    ri -= 1  # parenthetical group needs a chance to return on its own
                break  # and return
            elif c == "|":
                ri, br_current = self.explore(ri, start=start, in_or=True)
                current = current + br_current

        return ri, current

    def furthest_room(self):
        reached = set()
        steps = 0
        curr = {self.origin}

        while curr:
            next_rooms = set()
            for room in curr:
                reached.add(room.loc)

                for nr in room.neighbors():
                    if nr.loc not in reached:
                        next_rooms.add(nr)

            curr = next_rooms
            steps += 1

        return steps - 1

    def visualize(self):
        out = ""
        min_x, min_y = max_x, max_y = self.origin.loc
        for x, y in self.rooms:
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)
        for y in range(max_y, min_y - 1, -1):
            for x in range(min_x, max_x + 1):
                if (x, y) == (0, 0):
                    out += "X"
                elif (x, y) in self.rooms:
                    out += "."
                else:
                    out += " "
            out += "\n"

        out += f"({len(self.rooms)} rooms)"
        return out


class Room:
    def __init__(self, x, y, room_at):
        self.loc = (x, y)
        self.x = x
        self.y = y
        self.room_at = room_at
        self.n = self.e = self.s = self.w = None

    def __repr__(self):
        return f"Room({self.x}, {self.y})"

    def neighbors(self):
        bors = {self.n, self.e, self.s, self.w}
        bors.discard(None)
        return bors

    def north(self):
        if self.n is None:
            self.n = self.room_at(self.x, self.y + 1)
            self.n.s = self
        return self.n

    def south(self):
        if self.s is None:
            self.s = self.room_at(self.x, self.y - 1)
            self.s.n = self
        return self.s

    def east(self):
        if self.e is None:
            self.e = self.room_at(self.x + 1, self.y)
            self.e.w = self
        return self.e

    def west(self):
        if self.w is None:
            self.w = self.room_at(self.x - 1, self.y)
            self.w.e = self
        return self.w


class MultiRoom:
    def __init__(self, rooms=None):
        self.rooms = rooms or set()

        def call_all(f):
            def m():
                return MultiRoom({f(room) for room in self.rooms})

            return m

        self.north = call_all(Room.north)
        self.east = call_all(Room.east)
        self.south = call_all(Room.south)
        self.west = call_all(Room.west)

    def __repr__(self):
        return repr(self.rooms)

    def __add__(self, other):
        if not isinstance(other, MultiRoom):
            raise TypeError(
                f"unsupported operand type(s) for +: 'MultiRoom' and '{type(other)}'"
            )
        return MultiRoom(self.rooms.union(other.rooms))


def part_a(inp):
    m = Map(inp.value[1:-1])
    m.explore()
    return m.furthest_room()


def part_b(inp):
    pass


if __name__ == "__main__":
    INP = AOCInput(20)
    print(part_a(INP))
    print(part_b(INP))
