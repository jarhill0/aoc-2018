import unittest

from aoc_input import AOCInput
import day24


INPUT = AOCInput(24)
EXAMPLE = AOCInput.test_input(
    """Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4
"""
)


class TestDay24(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(5216, day24.part_a(EXAMPLE))
        self.assertEqual(26937, day24.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(None, day24.part_b(EXAMPLE))
        # self.assertEqual(None, day24.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
