#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 02.12.21              #
#                       #
# Day 02, Part 1        #
#########################

from datetime import datetime


def aoc2021_02_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 02, Part 1\n~~ running as a test ~~")

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

    #print(input_data)
    
    fowardDistance = 0
    depth = 0

    for instruction in input_data:
        [direction, magnitude] = instruction.split(" ")
        if direction == "forward":
            fowardDistance += int(magnitude)
        elif direction == "up":
            depth -= int(magnitude)
        elif direction == "down":
            depth += int(magnitude)
        else:
            print(direction)
            return "weird error"
    
    answer = depth * fowardDistance
        

    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_02_1("input.txt")