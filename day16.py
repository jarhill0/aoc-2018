import collections

from aoc_input import AOCInput


def addr(reg, a, b, c):
    reg[c] = reg[a] + reg[b]


def addi(reg, a, b, c):
    reg[c] = reg[a] + b


def mulr(reg, a, b, c):
    reg[c] = reg[a] * reg[b]


def muli(reg, a, b, c):
    reg[c] = reg[a] * b


def banr(reg, a, b, c):
    reg[c] = reg[a] & reg[b]


def bani(reg, a, b, c):
    reg[c] = reg[a] & b


def borr(reg, a, b, c):
    reg[c] = reg[a] | reg[b]


def bori(reg, a, b, c):
    reg[c] = reg[a] | b


def setr(reg, a, _, c):
    reg[c] = reg[a]


def seti(reg, a, _, c):
    reg[c] = a


def gtir(reg, a, b, c):
    reg[c] = 1 if a > reg[b] else 0


def gtri(reg, a, b, c):
    reg[c] = 1 if reg[a] > b else 0


def gtrr(reg, a, b, c):
    reg[c] = 1 if reg[a] > reg[b] else 0


def eqir(reg, a, b, c):
    reg[c] = 1 if a == reg[b] else 0


def eqri(reg, a, b, c):
    reg[c] = 1 if reg[a] == b else 0


def eqrr(reg, a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0


def wrap(f):
    """Give `f` its own copy of the registers for it to mutate."""

    def wrapped(reg, *args):
        custom_reg = list(reg)
        f(custom_reg, *args)
        return tuple(custom_reg)

    return wrapped


OPERATIONS = [
    addr,
    addi,
    mulr,
    muli,
    banr,
    bani,
    borr,
    bori,
    setr,
    seti,
    gtri,
    gtir,
    gtrr,
    eqri,
    eqir,
    eqrr,
]


def all_operations(registers, a, b, c):
    return {op: wrap(op)(registers, a, b, c) for op in OPERATIONS}


def parse(inp):
    out = []
    cases, _, prog = inp.value.partition("\n\n\n\n")
    for case in cases.split("\n\n"):
        before, inst, after = case.splitlines()
        before = tuple(eval(before.partition(": ")[2]))  # 😬😬😳😥😟
        after = tuple(eval(after.partition(": ")[2]))  # 😬😬😳😥😟
        inst = tuple(int(i) for i in inst.split(" "))
        out.append((before, inst, after))
    prog = tuple(tuple(int(v) for v in line.split()) for line in prog.splitlines())
    return out, prog


def part_a(inp):
    count = 0
    for before, inst, after in parse(inp)[0]:
        _, a, b, c = inst
        if list(all_operations(before, a, b, c).values()).count(after) >= 3:
            count += 1
    return count


def part_b(inp):
    tests, prog = parse(inp)
    candidates = {opcode: set(OPERATIONS) for opcode in range(16)}
    for before, inst, after in tests:
        op, a, b, c = inst
        for operation, result in all_operations(before, a, b, c).items():
            if result != after:
                candidates[op].discard(operation)

    opcodes = solve(candidates)

    reg = execute(prog, opcodes)
    return reg[0]


def execute(prog, opcodes):
    registers = [0] * 4
    for oc, a, b, c in prog:
        opcodes[oc](registers, a, b, c)
    return registers


def solve(candidates):
    opcodes = {}
    while len(opcodes) < 16:
        for opcode, ops in candidates.items():
            if len(ops) != 1:
                continue
            sol = next(iter(ops))
            assert opcode not in opcodes
            opcodes[opcode] = sol
            candidates[opcode].clear()
            for ops2 in candidates.values():
                ops2.discard(sol)
            break

        seen_count = collections.Counter()
        for ops in candidates.values():
            for o in ops:
                seen_count[o] += 1

        for o, ct in seen_count.items():
            if ct != 1:
                continue
            opcode = next(code for code, ops in candidates.items() if o in ops)
            assert opcode not in opcodes
            opcodes[opcode] = o
            candidates[opcode].clear()
            for ops2 in candidates.values():
                ops2.discard(o)
            break

    return opcodes


if __name__ == "__main__":
    INP = AOCInput(16)
    print(part_a(INP))
    print(part_b(INP))
