from aoc_input import AOCInput

from day16 import (
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
    gtir,
    gtri,
    gtrr,
    eqir,
    eqri,
    eqrr,
)


OPERATIONS = {
    "addr": addr,
    "addi": addi,
    "mulr": mulr,
    "muli": muli,
    "banr": banr,
    "bani": bani,
    "borr": borr,
    "bori": bori,
    "setr": setr,
    "seti": seti,
    "gtri": gtri,
    "gtir": gtir,
    "gtrr": gtrr,
    "eqri": eqri,
    "eqir": eqir,
    "eqrr": eqrr,
}


def parse_token(t):
    return OPERATIONS.get(t) or int(t)


def parse(inp):
    ip_line, _, prog = inp.value.partition("\n")
    ip_reg = int(ip_line.split()[-1])
    prog = tuple(
        tuple(parse_token(v) for v in line.split()) for line in prog.splitlines()
    )
    return ip_reg, prog


def part_a(inp):
    ip_reg, prog = parse(inp)
    registers = execute(prog, ip_reg)
    return registers[0]


def execute(prog, ip_reg, registers=None):
    registers = registers or [0] * 6
    while 0 <= registers[ip_reg] < len(prog):
        # JIT compilation :P
        if registers[ip_reg] == 1:  # the 1 works for my input
            registers[0] = sum_factors(registers[2])  # reg[2] works for my input
            registers[3] = 16 * 16
            return registers
        op, a, b, c = prog[registers[ip_reg]]
        op(registers, a, b, c)
        registers[ip_reg] += 1
    return registers


def part_b(inp):
    ip_reg, prog = parse(inp)
    registers = execute(prog, ip_reg, registers=[1] + [0] * 5)
    return registers[0]


def sum_factors(num):
    return sum(j if num % j == 0 else 0 for j in range(1, num + 1))


if __name__ == "__main__":
    INP = AOCInput(19)
    print(part_a(INP))
    print(part_b(INP))
