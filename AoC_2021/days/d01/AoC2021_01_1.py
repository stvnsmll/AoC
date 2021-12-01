#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 01.12.21              #
#                       #
# Day 01, Part 1        #
#########################

from datetime import datetime
import numpy as np


def aoc2021_01_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 01, Part 1\n~~ running as a test ~~")

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
    
    total = 0
    previous_reading = 10000000
    for sonar_reading in input_data:
        if previous_reading < sonar_reading:
            total += 1
        previous_reading = sonar_reading
        

    print(f"\nSolution: {total}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    answer = total
    return answer



if __name__ == "__main__":
   aoc2021_01_1("input.txt")