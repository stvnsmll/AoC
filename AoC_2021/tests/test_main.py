
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

        def test_AoC2021_08_1_a(self):
            [year, day, part, example, solution_type] = [2021, 8, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_08_2_a(self):
            [year, day, part, example, solution_type] = [2021, 8, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_08_2_b(self):
            [year, day, part, example, solution_type] = [2021, 8, 2, "b", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_09_1_a(self):
            [year, day, part, example, solution_type] = [2021, 9, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_09_2_a(self):
            [year, day, part, example, solution_type] = [2021, 9, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_10_1_a(self):
            [year, day, part, example, solution_type] = [2021, 10, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_10_2_a(self):
            [year, day, part, example, solution_type] = [2021, 10, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_11_1_a(self):
            [year, day, part, example, solution_type] = [2021, 11, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_11_2_a(self):
            [year, day, part, example, solution_type] = [2021, 11, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_12_1_a(self):
            [year, day, part, example, solution_type] = [2021, 12, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
            
        def test_AoC2021_12_1_b(self):
            [year, day, part, example, solution_type] = [2021, 12, 1, "b", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_12_1_c(self):
            [year, day, part, example, solution_type] = [2021, 12, 1, "c", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_12_2_a(self):
            [year, day, part, example, solution_type] = [2021, 12, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_12_2_b(self):
            [year, day, part, example, solution_type] = [2021, 12, 2, "b", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_12_2_c(self):
            [year, day, part, example, solution_type] = [2021, 12, 2, "c", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_13_1_a(self):
            [year, day, part, example, solution_type] = [2021, 13, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_13_2_a(self):
            [year, day, part, example, solution_type] = [2021, 13, 2, "a", "str"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_15_1_a(self):
            [year, day, part, example, solution_type] = [2021, 15, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_14_1_a(self):
            [year, day, part, example, solution_type] = [2021, 14, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_14_2_a(self):
            [year, day, part, example, solution_type] = [2021, 14, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_15_2_a(self):
            [year, day, part, example, solution_type] = [2021, 15, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)

        def test_AoC2021_16_1_a(self):
            [year, day, part, example, solution_type] = [2021, 16, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
    
        def test_AoC2021_16_2_a(self):
            [year, day, part, example, solution_type] = [2021, 16, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_17_1_a(self):
            [year, day, part, example, solution_type] = [2021, 17, 1, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
        
        def test_AoC2021_17_2_a(self):
            [year, day, part, example, solution_type] = [2021, 17, 2, "a", "int"]#works with int or str
            [solution, answer] = solve_with_test(year, day, part, example, solution_type)
            self.assertEqual(solution, answer)
    """

    def test_AoC2021_18_1_a(self):
        [year, day, part, example, solution_type] = [2021, 18, 1, "a", "int"]#works with int or str
        [solution, answer] = solve_with_test(year, day, part, example, solution_type)
        self.assertEqual(solution, answer)

if __name__ == '__main__':
    unittest.main()