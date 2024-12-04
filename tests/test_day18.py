import unittest

from aoc_input import AOCInput
import day18


INPUT = AOCInput(18)
EXAMPLE = AOCInput.test_input(
    """.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|."""
)


class TestDay18(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(1147, day18.part_a(EXAMPLE))
        self.assertEqual(558960, day18.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(207900, day18.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
