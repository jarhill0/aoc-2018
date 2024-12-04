import unittest

from aoc_input import AOCInput
import day17


INPUT = AOCInput(17)
EXAMPLE = AOCInput.test_input(
    """x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504"""
)


class TestDay17(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(57, day17.part_a(EXAMPLE))
        actual_answer = day17.part_a(INPUT)
        self.assertEqual(50838, actual_answer)

    def test_part_b(self):
        self.assertEqual(29, day17.part_b(EXAMPLE))
        self.assertEqual(43039, day17.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
