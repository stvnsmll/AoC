
import unittest

import sys
sys.path.append("..")
from test_support import solve_with_test


class TestBasic(unittest.TestCase):
    """ Test Cases to skip:
        
        def test_AoC2021_01_1_a(self):
            [year, day, part, example, solution_type] = [2021, 1, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_01_2_a(self):
            [year, day, part, example, solution_type] = [2021, 1, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_02_1_a(self):
            [year, day, part, example, solution_type] = [2021, 2, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_02_2_a(self):
            [year, day, part, example, solution_type] = [2021, 2, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_03_1_a(self):
            [year, day, part, example, solution_type] = [2021, 3, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_03_2_a(self):
            [year, day, part, example, solution_type] = [2021, 3, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_04_1_a(self):
            [year, day, part, example, solution_type] = [2021, 4, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_04_2_a(self):
            [year, day, part, example, solution_type] = [2021, 4, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_05_1_a(self):
            [year, day, part, example, solution_type] = [2021, 5, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_05_2_a(self):
            [year, day, part, example, solution_type] = [2021, 5, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_06_1_a(self):
            [year, day, part, example, solution_type] = [2021, 6, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_06_2_a(self):
            [year, day, part, example, solution_type] = [2021, 6, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
    
        def test_AoC2021_07_1_a(self):
            [year, day, part, example, solution_type] = [2021, 7, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_07_2_a(self):
            [year, day, part, example, solution_type] = [2021, 7, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

    """
    
    def test_AoC2021_08_1_a(self):
        [year, day, part, example, solution_type] = [2021, 8, 1, "a", "int"]#works with int or str
        [solution, answer] = solve_with_test(year, day, part, example, solution_type)
        self.assertEqual(solution, answer)

if __name__ == '__main__':
    unittest.main()