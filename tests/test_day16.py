import unittest

from aoc_input import AOCInput
import day16


INPUT = AOCInput(16)
EXAMPLE = AOCInput.test_input(
    """Before: [3, 2, 1, 1]
9 2 1 2
After:  [3, 2, 2, 1]



"""
)


class TestDay16(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(1, day16.part_a(EXAMPLE))
        self.assertEqual(531, day16.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(649, day16.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
