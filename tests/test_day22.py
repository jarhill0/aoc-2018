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
        self.assertLess(actual, 1090)
        # self.assertEqual(None, day22.part_b(INPUT))

    def test_fastest_route_longcut_shortcut(self):
        # ...
        # ==.
        # T..
        #
        # (answer is 6)
        # This tests that a longer route that requires no gear change
        # beats a "shorter" route with a gear change
        class MockMaze:
            def __init__(self):
                self.target = (0, 2)

            def region_kind(self, pt):
                if pt == (0, 1) or pt == (1, 1):
                    return day22.WET
                return day22.ROCKY

        maze = MockMaze()
        self.assertEqual(6, day22.fastest_route(maze))


if __name__ == "__main__":
    unittest.main()
