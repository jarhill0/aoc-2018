import unittest

from aoc_input import AOCInput
import day15

EXAMPLE = AOCInput.test_input(
    """#######   
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""
)
EXAMPLE2 = AOCInput.test_input(
    """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""
)

INPUT = AOCInput(15)


class TestDay15(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(27730, day15.part_a(EXAMPLE))
        self.assertEqual(36334, day15.part_a(EXAMPLE2))
        real_answer = day15.part_a(INPUT)
        self.assertLess(200859, real_answer)
        self.assertEqual(221754, day15.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(None, day15.part_b(EXAMPLE))
        # self.assertEqual(None, day15.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
