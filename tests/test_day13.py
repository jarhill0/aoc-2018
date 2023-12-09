import unittest

from aoc_input import AOCInput
import day13

EXAMPLE = AOCInput.test_input(
    "/->-\\        \n|   |  /----\\\n| /-+--+-\\  |\n| | |  | v  |\n\\-+-/  \\-+--/\n  \\------/   "
)
EXAMPLE2 = AOCInput.test_input(
    "/>-<\\  \n|   |  \n| /<+-\\\n| | | v\n\\>+</ |\n  |   ^\n  \\<->/"
)
INPUT = AOCInput(13)


class TestDay13(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual("7,3", day13.part_a(EXAMPLE))
        real_answer = day13.part_a(INPUT)
        self.assertNotEqual("91,85", real_answer)
        self.assertNotEqual("27,107", real_answer)
        self.assertEqual("28,107", real_answer)

    def test_part_b(self):
        self.assertEqual("6,4", day13.part_b(EXAMPLE2))
        self.assertEqual("36,123", day13.part_b(INPUT))

    def test_next_turn(self):
        self.assertEqual(0, day13.next_turn(-1))
        self.assertEqual(1, day13.next_turn(0))
        self.assertEqual(-1, day13.next_turn(1))


if __name__ == "__main__":
    unittest.main()
