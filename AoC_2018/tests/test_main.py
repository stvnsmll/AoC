
import unittest
import importlib

import sys
sys.path.append("..")
from test_support import solve_with_test


class TestBasic(unittest.TestCase):
    """ Test Cases to skip:
        
        def test_AoC2018_01_1_a(self):
            [year, day, part, example, solution_type] = [2018, 1, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2018_01_1_b(self):
            [year, day, part, example, solution_type] = [2018, 1, 1, "b", "int"]#works with int or string
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2018_01_1_c(self):
            [year, day, part, example, solution_type] = [2018, 1, 1, "c", "int"]#works with int or string
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2018_01_2_a(self):
            [year, day, part, example, solution_type] = [2018, 1, 2, "a", "int"]#works with int or string
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2018_01_2_b(self):
            [year, day, part, example, solution_type] = [2018, 1, 2, "b", "int"]#works with int or string
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2018_01_2_c(self):
            [year, day, part, example, solution_type] = [2018, 1, 2, "c", "int"]#works with int or string
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2018_01_2_d(self):
            [year, day, part, example, solution_type] = [2018, 1, 2, "d", "int"]#works with int or string
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)    

        def test_AoC2018_02_1_a(self):
            [year, day, part, example, solution_type] = [2018, 2, 1, "a", "int"]#works with int or string
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2018_02_2_a(self):
            [year, day, part, example, solution_type] = [2018, 2, 2, "a", "str"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
    """

    def test_AoC2018_03_1_a(self):
        [year, day, part, example, solution_type] = [2018, 3, 1, "a", "int"]#works with int or str
        [solution, answer] = solve_with_test(year, day, part, example, solution_type)
        self.assertEqual(solution, answer)

    def test_AoC2018_03_2_a(self):
        [year, day, part, example, solution_type] = [2018, 3, 2, "a", "int"]#works with int or str
        [solution, answer] = solve_with_test(year, day, part, example, solution_type)
        self.assertEqual(solution, answer)

if __name__ == '__main__':
    unittest.main()