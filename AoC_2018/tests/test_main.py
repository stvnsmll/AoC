
import unittest

import sys
sys.path.append("..")
from test_support import get_solution, make_path


class TestBasic(unittest.TestCase):
    """ Test Cases to skip:
            
        def test_AoC2018_01_1_a(self):
            from days.d01.AoC2018_01_1 import aoc2018_01_1
            filename = make_path(1, 1, "a")#day, part, example
            answer = aoc2018_01_1(filename)
            solution = get_solution(1, 1, "a")
            self.assertEqual(solution, answer)

        def test_AoC2018_01_1_b(self):
            from days.d01.AoC2018_01_1 import aoc2018_01_1
            filename = make_path(1, 1, "b")#day, part, example
            answer = aoc2018_01_1(filename)
            solution = get_solution(1, 1, "b")
            self.assertEqual(solution, answer)

        def test_AoC2018_01_1_c(self):
            from days.d01.AoC2018_01_1 import aoc2018_01_1
            filename = make_path(1, 1, "c")#day, part, example
            answer = aoc2018_01_1(filename)
            solution = get_solution(1, 1, "c")
            self.assertEqual(solution, answer)

        def test_AoC2018_01_2_a(self):
            from days.d01.AoC2018_01_2 import aoc2018_01_2
            filename = make_path(1, 2, "a")#day, part, example
            answer = aoc2018_01_2(filename)
            solution = get_solution(1, 2, "a")
            self.assertEqual(solution, answer)

        def test_AoC2018_01_2_b(self):
            from days.d01.AoC2018_01_2 import aoc2018_01_2
            filename = make_path(1, 2, "b")#day, part, example
            answer = aoc2018_01_2(filename)
            solution = get_solution(1, 2, "b")
            self.assertEqual(solution, answer)

        def test_AoC2018_01_2_c(self):
            from days.d01.AoC2018_01_2 import aoc2018_01_2
            filename = make_path(1, 2, "c")#day, part, example
            answer = aoc2018_01_2(filename)
            solution = get_solution(1, 2, "c")
            self.assertEqual(solution, answer)

        def test_AoC2018_01_2_d(self):
            from days.d01.AoC2018_01_2 import aoc2018_01_2
            filename = make_path(1, 2, "d")#day, part, example
            answer = aoc2018_01_2(filename)
            solution = get_solution(1, 2, "d")
            self.assertEqual(solution, answer)    
    """

    def test_AoC2018_02_1_a(self):
        from days.d02.AoC2018_02_1 import aoc2018_02_1
        filename = make_path(2, 1, "a")#day, part, example
        answer = aoc2018_02_1(filename)
        solution = get_solution(2, 1, "a")
        self.assertEqual(solution, answer)
    
    def test_AoC2018_02_2_a(self):
        from days.d02.AoC2018_02_2 import aoc2018_02_2
        filename = make_path(2, 2, "a")#day, part, example
        answer = aoc2018_02_2(filename)
        solution = get_solution(2, 2, "a", "str")#day, part, example, (optional, type = "string")
        self.assertEqual(solution, answer)



if __name__ == '__main__':
    unittest.main()