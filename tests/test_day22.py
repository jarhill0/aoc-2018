import unittest

from aoc_input import AOCInput
import day22


INPUT = AOCInput(22)
EXAMPLE = AOCInput.test_input("""depth: 510\ntarget: 10,10\n""")


class TestDay22(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(114, day22.part_a(EXAMPLE))
        self.assertEqual(6318, day22.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(45, day22.part_b(EXAMPLE))
        actual = day22.part_b(INPUT)
        self.assertLess(actual, 1099)
        # self.assertEqual(None, day22.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
