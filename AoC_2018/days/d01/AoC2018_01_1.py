#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 10.11.21              #
#                       #
# Day 01, Part 1        #
#########################

from datetime import datetime
import numpy as np


def aoc2018_01_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 01, Part 1\n~~ running as a test ~~")

    startTime = datetime.now()

    data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=int)
    
    total = 0
    for i in data:
        total += int(i)
    


    print(f"\nSolution: {total}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    answer = total
    return answer



if __name__ == "__main__":
   aoc2018_01_1("input.txt")