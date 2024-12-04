import unittest

from aoc_input import AOCInput
import day19


INPUT = AOCInput(19)
EXAMPLE = AOCInput.test_input(
    """#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
"""
)


class TestDay19(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(2223, day19.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(24117312, day19.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
