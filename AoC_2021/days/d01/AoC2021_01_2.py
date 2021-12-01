#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 01.12.21              #
#                       #
# Day 01, Part 2        #
#########################

from datetime import datetime
import numpy as np


def aoc2021_01_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 01, Part 2\n~~ running as a test ~~")

    startTime = datetime.now()

    # Using readline()
    input_data_file = open(filename, 'r')
    input_data = []
    while True:
        # Get next line from file
        line = input_data_file.readline()
        # if line is empty end of file is reached
        if not line:
            break
        #print(line)
        input_data.append(int(line.strip()))
    input_data_file.close()

    #print(input_data)
    
    list_of_threes_sum = []
    for i in range(len(input_data) - 2):
        list_of_threes_sum.append((input_data[i] + input_data[i + 1] + input_data[i + 2]))

    #print(list_of_threes_sum)

    total = 0
    previous_reading = 10000000
    for sonar_reading in list_of_threes_sum:
        if previous_reading < sonar_reading:
            total += 1
        previous_reading = sonar_reading

        

    print(f"\nSolution: {total}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    answer = total
    return answer



if __name__ == "__main__":
   aoc2021_01_2("input.txt")