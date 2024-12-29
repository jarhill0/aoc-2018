import unittest

from aoc_input import AOCInput
import day25


INPUT = AOCInput(25)
EXAMPLE = AOCInput.test_input(
    """0,0,0,0
3,0,0,0
0,3,0,0
0,0,3,0
0,0,0,3
0,0,0,6
9,0,0,0
12,0,0,0"""
)
EXAMPLE2 = AOCInput.test_input(
    """-1,2,2,0
0,0,2,-2
0,0,0,-2
-1,2,0,0
-2,-2,-2,2
3,0,2,-1
-1,3,2,2
-1,0,-1,0
0,2,1,-2
3,0,0,0"""
)
EXAMPLE3 = AOCInput.test_input(
    """1,-1,0,1
2,0,-1,0
3,2,-1,0
0,0,3,1
0,0,-1,-1
2,3,-2,0
-2,2,0,0
2,-2,0,-1
1,-1,0,-1
3,2,0,2"""
)
EXAMPLE4 = AOCInput.test_input(
    """1,-1,-1,-2
-2,-2,0,1
0,2,1,3
-2,3,-2,1
0,2,3,-2
-1,-1,1,-2
0,-2,-1,0
-2,2,3,-1
1,2,2,0
-1,-2,0,-2"""
)


class TestDay25(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(2, day25.part_a(EXAMPLE))
        self.assertEqual(4, day25.part_a(EXAMPLE2))
        self.assertEqual(3, day25.part_a(EXAMPLE3))
        self.assertEqual(8, day25.part_a(EXAMPLE4))
        # self.assertEqual(None, day25.part_a(INPUT))


if __name__ == "__main__":
    unittest.main()
