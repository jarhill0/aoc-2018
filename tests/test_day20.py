import unittest

from aoc_input import AOCInput
import day20


INPUT = AOCInput(20)
EXAMPLE1 = AOCInput.test_input("^WNE$")
EXAMPLE2 = AOCInput.test_input("^ENWWW(NEEE|SSE(EE|N))$")
EXAMPLE3 = AOCInput.test_input("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$")
EXAMPLE4 = AOCInput.test_input("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$")
EXAMPLE5 = AOCInput.test_input(
    "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
)


class TestDay20(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(3, day20.part_a(EXAMPLE1))
        self.assertEqual(10, day20.part_a(EXAMPLE2))
        self.assertEqual(18, day20.part_a(EXAMPLE3))
        self.assertEqual(23, day20.part_a(EXAMPLE4))
        self.assertEqual(31, day20.part_a(EXAMPLE5))
        self.assertEqual(4501, day20.part_a(INPUT))

    def test_part_b(self):
        self.assertEqual(8623, day20.part_b(INPUT))


if __name__ == "__main__":
    unittest.main()
