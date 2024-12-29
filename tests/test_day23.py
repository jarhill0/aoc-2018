import unittest

from aoc_input import AOCInput
import day23


INPUT = AOCInput(23)
EXAMPLE = AOCInput.test_input(
    """pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1"""
)


class TestDay23(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(7, day23.part_a(EXAMPLE))
        self.assertEqual(232, day23.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(None, day23.part_b(EXAMPLE))
        # self.assertEqual(None, day23.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
