#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 05.12.21              #
#                       #
# Day 05, Part 2        #
#########################

from datetime import datetime
import numpy as np


def aoc2021_05_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 5, Part 2\n~~ running as a test ~~")

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

    all_lines = []
    #each line is formatted: [x1, y1, x2, y2]
    for instruction in input_data:
        line_data = [int(x) for x in instruction.replace(" -> ",",").split(",")]
        all_lines += [line_data]
    #print(all_lines)

    # for part 1, only keep the horizontal or vertical lines
    max_map_x = 0
    max_map_y = 0
    simple_lines = []
    diag_lines = []
    for instr in all_lines:
        if (instr[0] == instr[2]) or (instr[1] == instr[3]):
            simple_lines += [instr]
        else:
            diag_lines += [instr]
        if instr[0] > max_map_x:
            max_map_x = instr[0]
        if instr[2] > max_map_x:
            max_map_x = instr[2]
        if instr[1] > max_map_y:
            max_map_y = instr[1]
        if instr[3] > max_map_y:
            max_map_y = instr[3]
    print(simple_lines)
    #print(max_map_y)
    #print(max_map_x)
    coverage_map = np.zeros((max_map_y + 1, max_map_x + 1), dtype=int)
    #print(coverage_map)
    for instr in simple_lines:
        #print(instr)
        if instr[0] == instr[2]:
            #print("   x-direction")
            #x-direction line, increment the y from y1 to y2, adding to both maps
            minline = min(instr[1], instr[3])
            maxline = max(instr[1], instr[3])
            #print(f"   {minline} to {maxline}")
            for i in range(maxline - minline + 1):
                coverage_map[minline + i][instr[0]] += 1#-1s are for the 0-index shift
        else:
            #print("   y-direction")
            #y-direction line, increment the y from y1 to y2, adding to both maps
            minline = min(instr[0], instr[2])
            maxline = max(instr[0], instr[2])
            #print(f"   {minline} to {maxline}")
            for i in range(maxline - minline + 1):
                coverage_map[instr[1]][minline + i] += 1
        #print(coverage_map)

    #print(coverage_map)

    #now do diagonal lines
    for instr in diag_lines:
        #each line is formatted: [x1, y1, x2, y2]
        #place the starting and ending points:
        coverage_map[instr[1]][instr[0]] += 1
        coverage_map[instr[3]][instr[2]] += 1
        #get the direction (increasing = 1, decreasing = 2)
        x_dir = 1
        y_dir = 1
        exit = 0
        if instr[0] > instr[2]:
            x_dir = 2
        if instr[1] > instr[3]:
            y_dir = 2
        if x_dir == 1 and y_dir == 1:
            #x and y are increasing
            increment = 1
            while exit == 0:
                new_coord = [(instr[0] + increment), (instr[1] + increment)]
                if new_coord == [instr[2], instr[3]]:
                    exit = 1
                else:
                    coverage_map[new_coord[1]][new_coord[0]] += 1
                increment += 1
        if x_dir == 1 and y_dir == 2:
            #x is increasing, y is decreasing
            increment_x = 1
            increment_y = -1
            while exit == 0:
                new_coord = [(instr[0] + increment_x), (instr[1] + increment_y)]
                if new_coord == [instr[2], instr[3]]:
                    exit = 1
                else:
                    coverage_map[new_coord[1]][new_coord[0]] += 1
                increment_x += 1
                increment_y -= 1
        if x_dir == 2 and y_dir == 1:
            #x is decreasing, y is increasing
            increment_x = -1
            increment_y = 1
            while exit == 0:
                new_coord = [(instr[0] + increment_x), (instr[1] + increment_y)]
                if new_coord == [instr[2], instr[3]]:
                    exit = 1
                else:
                    coverage_map[new_coord[1]][new_coord[0]] += 1
                increment_x -= 1
                increment_y += 1
        if x_dir == 2 and y_dir == 2:
            #x and y are decreasing
                        #x and y are increasing
            increment = -1
            while exit == 0:
                new_coord = [(instr[0] + increment), (instr[1] + increment)]
                if new_coord == [instr[2], instr[3]]:
                    exit = 1
                else:
                    coverage_map[new_coord[1]][new_coord[0]] += 1
                increment -= 1

    #print(coverage_map)

    overlap_count = 0
    for row in coverage_map:
        for column in row:
            if column > 1:
                overlap_count += 1
    

    answer = overlap_count
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_05_2("input.txt")