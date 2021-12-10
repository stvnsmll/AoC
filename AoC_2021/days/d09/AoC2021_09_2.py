#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 09.12.21              #
#                       #
# Day 09, Part 2        #
#########################

from datetime import datetime
import numpy as np

#global tmp_map
tmp_map = {}
area_total = 0


def aoc2021_09_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 9, Part 2\n~~ running as a test ~~")

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
    loc_of_mins = {}#key = position (x, y), value = size
    mins_count = -1
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
                #print([row, column])
                mins_count += 1
                loc_of_mins[mins_count] = [row, column, 0]#row, column, basin size
                

    
    #print(loc_of_mins)
    for centerpoint in range(len(loc_of_mins)):
        #print(loc_of_mins[centerpoint])
    
        #grow the map stepping the size of the basin
        #y is the row, x is the column
        start_row = loc_of_mins[centerpoint][0]
        start_col = loc_of_mins[centerpoint][1]
        exit = 0
        global tmp_map
        global area_total
        tmp_map = height_map
        area_total = 1
        tmp_map[start_row][start_col] = 10
        row = start_row
        col = start_col


        add_any_neighbors([row, col])
        
        #print("Map should be solved for one locations:")
        #print(tmp_map)
        #count 10's in tmp_map
        #print(area_total)
        loc_of_mins[centerpoint][2] = area_total

    #print(loc_of_mins)

    list_of_sizes = []
    for i in range(len(loc_of_mins)):
        list_of_sizes.append(loc_of_mins[i][2])
    

    list_of_sizes.sort()
    sorted_sizes = list_of_sizes[::-1].copy()
    #print(sorted_sizes[0:3])

    answer = 1
    for i in sorted_sizes[0:3]:
        answer *= i
    
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer

def add_any_neighbors(coord_in):
    row = coord_in[0]
    col = coord_in[1]
    global tmp_map
    global area_total
    #print(f"At location {coord_in}")
    #one at a time, check the positions around a given coordinate:
    #  if the the value at that neighbor is a 9, do nothing
    #  otherwise, set their value to 10 and check any of its neighbors
    #TOP
    #print(f"TOP: {tmp_map[row - 1][col]}")#top
    if tmp_map[row - 1][col] < 9 :
        tmp_map[row - 1][col] = 10
        area_total += 1
        add_any_neighbors([row - 1, col])
    #LEFT
    #print(f"LEFT: {tmp_map[row][col - 1]}")#left
    if tmp_map[row][col - 1] < 9:
        tmp_map[row][col - 1] = 10
        area_total += 1
        add_any_neighbors([row, col - 1])
    #BOTTOM
    #print(f"BOTTOM: {tmp_map[row + 1][col]}")#bottom
    if tmp_map[row + 1][col] < 9:
        tmp_map[row + 1][col] = 10
        area_total += 1
        add_any_neighbors([row + 1, col])
    #RIGHT
    #print(tmp_map[row][col + 1])#right
    if tmp_map[row][col + 1] < 9:
        tmp_map[row][col + 1] = 10
        area_total += 1
        add_any_neighbors([row, col + 1])

if __name__ == "__main__":
   aoc2021_09_2("input.txt")