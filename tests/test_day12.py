import unittest

from aoc_input import AOCInput
import day12

EXAMPLE = AOCInput.test_input(
    "initial state: #..#.#..##......###...###\n\n...## => #\n..#.. => #\n.#... => #\n.#.#. => #\n.#.## => #\n.##.. => #\n.#### => #\n#.#.# => #\n#.### => #\n##.#. => #\n##.## => #\n###.. => #\n###.# => #\n####. => #"
)
INPUT = AOCInput(12)


class TestDay12(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(325, day12.part_a(EXAMPLE))
        self.assertEqual(1917, day12.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(1250000000991, day12.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
