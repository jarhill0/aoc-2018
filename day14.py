from aoc_input import AOCInput


def parse(inp):
    return int(inp.value)


class HotChocolateElves:
    def __init__(self):
        self.recipes = [3, 7]
        self.elf1 = 0
        self.elf2 = 1

    def step(self):
        self.create_new()
        self.move_elves()

    def create_new(self):
        new = self.recipes[self.elf1] + self.recipes[self.elf2]
        if new >= 10:
            self.recipes.append(1)
            new -= 10
        self.recipes.append(new)

    def move_elves(self):
        self.elf1 = (self.elf1 + 1 + self.recipes[self.elf1]) % len(self.recipes)
        self.elf2 = (self.elf2 + 1 + self.recipes[self.elf2]) % len(self.recipes)

    def ends_with(self, subseq):
        return (
            subseq == self.recipes[-len(subseq) :]
            or subseq == self.recipes[-len(subseq) - 1 : -1]
        )

    def index_of(self, subseq):
        if subseq == self.recipes[-len(subseq) :]:
            return len(self.recipes) - len(subseq)
        elif subseq == self.recipes[-len(subseq) - 1 : -1]:
            return len(self.recipes) - len(subseq) - 1


def part_a(inp):
    recipes_after = parse(inp)
    elves = HotChocolateElves()
    while len(elves.recipes) < recipes_after + 10:
        elves.step()
    return "".join(str(r) for r in elves.recipes[recipes_after : recipes_after + 10])


def parse2(inp):
    return [int(c) for c in inp.value]


def part_b(inp):
    subseq = parse2(inp)
    elves = HotChocolateElves()
    while not elves.ends_with(subseq):
        elves.step()
    return elves.index_of(subseq)


if __name__ == "__main__":
    INP = AOCInput(14)
    print(part_a(INP))
    print(part_b(INP))
