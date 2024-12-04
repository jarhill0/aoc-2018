import unittest

from aoc_input import AOCInput
import day21


INPUT = AOCInput(21)


class TestDay21(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(16134795, day21.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(14254292, day21.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
