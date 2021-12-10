#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 09.12.21              #
#                       #
# Day 09, Part 1        #
#########################

from datetime import datetime
import numpy as np


def aoc2021_09_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 9, Part 1\n~~ running as a test ~~")

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
    border_offset = 1#this makes all border pieces actually inside pieces
    map_x = len(input_data[0]) + (2 * border_offset)#hoirizontal length
    map_y = len(input_data) + (2 * border_offset)#vertaical map length
    print(f"{map_x} {map_y}")
    height_map = np.full((map_y,map_x), 9)
    #print(height_map)
    #print()
    #print(height_map[1][1:(map_x - 1)])
    #print(height_map)
    #print()
    for row in range(len(input_data)):
        height_map[(row + 1)][1:(map_x - 1)] = [int(i) for i in str(input_data[row])]
    #print(height_map)

    list_of_mins = []
    #loc_of_mins = []
    for row in range(1,(map_y - 1)):
        for column in range(1,(map_x - 1)):
            #print(f"[{row}, {column}]")
            value = height_map[row][column]
            top = height_map[row - 1][column]
            left = height_map[row][column - 1]
            right = height_map[row][column + 1]
            bottom = height_map[row + 1][column]
            neighbors = [top, left, right, bottom]
            #print(value)
            #print(neighbors)
            if value < min(neighbors):
                #print(f"Min value found: {value}")
                list_of_mins.append(value)
                #loc_of_mins.append([row, column])
    
    #print(loc_of_mins)
    answer = (sum(list_of_mins) + len(list_of_mins))
    print(len(list_of_mins))
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_09_1("input.txt")