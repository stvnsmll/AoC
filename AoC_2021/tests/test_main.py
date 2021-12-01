
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


    """

    def test_AoC2021_01_2_a(self):
        [year, day, part, example, solution_type] = [2021, 1, 2, "a", "int"]#works with int or str
        [solution, answer] = solve_with_test(year, day, part, example, solution_type)
        self.assertEqual(solution, answer)



if __name__ == '__main__':
    unittest.main()