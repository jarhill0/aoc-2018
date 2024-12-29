import re
from collections import namedtuple

from aoc_input import AOCInput

Unit = namedtuple(
    "Unit", ["count", "hp", "weakness", "immunity", "atk", "atk_type", "init"]
)


def parse(inp):
    immune, infection = inp.value.split("\n\n")

    def parse_unit(unit):
        count, hp, atk, atk_type, init = re.match(
            r"(\d+) units each with (\d+) hit points (?:\(.*\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)",
            unit,
        ).groups()
        weakness = re.findall(r"weak to ([^;)]+)", unit)
        if weakness:
            weakness = weakness[0].split(", ")
        immunity = re.findall(r"immune to ([^;)]+)", unit)
        if immunity:
            immunity = immunity[0].split(", ")
        count = int(count)
        hp = int(hp)
        atk = int(atk)
        init = int(init)
        return Unit(count, hp, weakness, immunity, atk, atk_type, init)

    immune = list(map(parse_unit, immune.splitlines()[1:]))
    infection = list(map(parse_unit, infection.splitlines()[1:]))
    return immune, infection


def part_a(inp):
    immune, infection = parse(inp)
    fight(immune, infection)
    return sum(u.count for u in (immune + infection))


def effective_power(unit):
    return unit.count * unit.atk


IMMUNE = 0
INFECTION = 1


def fight(immune, infection):
    def get(k):
        kind, ind = k
        a = immune if kind == IMMUNE else infection
        return a[ind]

    def sett(k, v):
        kind, ind = k
        a = immune if kind == IMMUNE else infection
        a[ind] = v

    def delete(k):
        kind, ind = k
        a = immune if kind == IMMUNE else infection
        del a[ind]

    while immune and infection:
        keys = [(IMMUNE, i) for i, x in enumerate(immune) if x is not None] + [
            (INFECTION, i) for i, x in enumerate(infection) if x is not None
        ]

        # ----------------
        # target selection
        # ----------------
        targets = dict()
        targeted = set()

        def target_selection_key(k):
            unit = get(k)
            return (effective_power(unit) + unit.init / 100,)

        for atk_key in sorted(keys, key=target_selection_key, reverse=True):
            atk_knd, atk_i = atk_key
            most_damage = 0
            target = None
            opponents = immune if atk_knd == INFECTION else infection
            for opp_i, opp in enumerate(opponents):
                opp_key = ((atk_knd + 1) % 2, opp_i)
                if opp_key in targeted:
                    continue

                units_killed = damage_to(get(atk_key), opp)
                if units_killed == 0:
                    continue
                if units_killed > most_damage:
                    target = opp_key
                    most_damage = units_killed
                elif units_killed == most_damage and effective_power(
                    opp
                ) > effective_power(get(target)):
                    target = opp_key
                elif (
                    units_killed == most_damage
                    and effective_power(opp) == effective_power(get(target))
                    and opp.init > get(target).init
                ):
                    target = opp_key
            if target is not None:
                targets[atk_key] = target
                targeted.add(target)

        # ------
        # attack
        # ------
        for atk_key in sorted(keys, key=lambda k: get(k).init, reverse=True):
            if get(atk_key) is None:
                continue
            # TODO: atk_key may no longer be present
            if atk_key not in targets:
                continue
            tgt_key = targets[atk_key]
            target = get(tgt_key)
            units_killed = damage_to(get(atk_key), target) // target.hp
            if units_killed >= target.count:
                sett(tgt_key, None)
            else:
                sett(tgt_key, target._replace(count=target.count - units_killed))

        # -------
        # cleanup
        # -------
        while None in immune:
            immune.remove(None)
        while None in infection:
            infection.remove(None)


def damage_to(attacker, target):
    if attacker.atk_type in target.immunity:
        return 0
    if attacker.atk_type in target.weakness:
        return 2 * effective_power(attacker)
    return effective_power(attacker)


#  Defending groups can only be chosen as a target by one attacking group.


def part_b(inp):
    pass


if __name__ == "__main__":
    INP = AOCInput(24)
    print(part_a(INP))
    print(part_b(INP))
