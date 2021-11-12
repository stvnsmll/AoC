#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 10.11.21              #
#                       #
# Day 01, Part 2        #
#########################

from datetime import datetime
import numpy as np


def aoc2018_01_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 01, Part 2\n~~ running as a test ~~")

    startTime = datetime.now()

    data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=int)
    list_of_frequencies = np.zeros(shape=(1))
    answer = 42
    total = 0
    while 1:
        for i in data:
            total += int(i)
            if total in list_of_frequencies:
                answer = total
                print(f"\nSolution: {answer}")
                print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
                return answer
            else:
                list_of_frequencies = np.append(list_of_frequencies, total)

    







if __name__ == "__main__":
   aoc2018_01_2("input.txt")