import unittest

from aoc_input import AOCInput
import day14

EXAMPLE = AOCInput.test_input("5")
EXAMPLE2 = AOCInput.test_input("9")
EXAMPLE3 = AOCInput.test_input("18")
EXAMPLE4 = AOCInput.test_input("2018")

INPUT = AOCInput(14)


class TestDay14(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual("0124515891", day14.part_a(EXAMPLE))
        self.assertEqual("5158916779", day14.part_a(EXAMPLE2))
        self.assertEqual("9251071085", day14.part_a(EXAMPLE3))
        self.assertEqual("5941429882", day14.part_a(EXAMPLE4))
        self.assertEqual("8610321414", day14.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(5, day14.part_b(AOCInput.test_input("01245")))
        self.assertEqual(9, day14.part_b(AOCInput.test_input("51589")))
        self.assertEqual(18, day14.part_b(AOCInput.test_input("92510")))
        self.assertEqual(2018, day14.part_b(AOCInput.test_input("59414")))
        self.assertEqual(20258123, day14.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
