#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 03.12.21              #
#                       #
# Day 03, Part 1        #
#########################

from datetime import datetime


def aoc2021_03_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 03, Part 1\n~~ running as a test ~~")

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
        input_data.append(line.strip())
    input_data_file.close()

    print(input_data)
    
    answer = 0
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_03_1("input.txt")