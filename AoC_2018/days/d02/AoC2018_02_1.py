#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 11.11.21              #
#                       #
# Day 02, Part 1        #
#########################

from datetime import datetime
import numpy as np


def aoc2018_02_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 02, Part 1\n~~ running as a test ~~")

    startTime = datetime.now()

    data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=str)
    
    #print(data)
    total_sets = [0, 0] #[twos, threes]
    for row in data:
        #print(row)
        row_counts = countSets(row)
        tmp_total = [total_sets[0] + row_counts[0], total_sets[1] + row_counts[1]]
        total_sets = tmp_total

    print(total_sets)
    
    checksum = total_sets[0] * total_sets[1]

    print(f"\nSolution: {checksum}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    answer = checksum
    return answer



def countSets(one_row):
    two_set = 0
    three_set = 0
    for i in one_row:
        tmp_count = one_row.count(i)
        #print(tmp_count)
        #print(f"{i} occures {tmp_count} times")
        if tmp_count == 2:
            two_set = 1
        if tmp_count == 3:
            three_set = 1
    #print([two_set, three_set])
    #print(two_set + three_set)
    return [two_set, three_set]
        

if __name__ == "__main__":
   aoc2018_02_1("input.txt")