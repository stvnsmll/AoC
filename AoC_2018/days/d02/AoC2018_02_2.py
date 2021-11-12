#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 12.11.21              #
#                       #
# Day 02, Part 2        #
#########################

from datetime import datetime
import numpy as np


def aoc2018_02_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 02, Part 2\n~~ running as a test ~~")

    startTime = datetime.now()

    data = np.loadtxt(filename, delimiter=',', skiprows=0, dtype=str)

    answer = ""
    
    #print(data)
    for j in range(len(data)):
        row = data[j]
        found_it = False
        for k in range(len(data) - (j + 1)):
            if one_dif_only(row, data[(j+1):][k]):
                found_it = True
                answer = common_letters(row, data[(j+1):][k])
                break
        if found_it: break
                
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer


def one_dif_only(str1, str2):
    error_count = 0
    i = 0
    for char in str1:
        if char != str2[i]:
            error_count += 1
        i += 1
    if error_count == 1:
        return True
    return False

def common_letters(str1, str2):
    common = ""
    i = 0
    for char in str1:
        if char == str2[i]:
            common += char
        i += 1
    print(common)
    return common


if __name__ == "__main__":
   aoc2018_02_2("input.txt")