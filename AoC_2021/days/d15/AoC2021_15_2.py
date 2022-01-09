#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 20.12.21              #
#                       #
# Day 15, Part 2        #
#########################

from datetime import datetime
import numpy as np


risk_map = np.zeros((2,2),int)

def aoc2021_15_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 15, Part 2\n~~ running as a test ~~")

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
    map_size_horiz = len(input_data[0])
    map_size_vert = len(input_data)

    full_map = []
    for row in range(map_size_vert):
        row_data = [int(x) for x in input_data[row]]
        full_map.append(row_data)

    #printMap(full_map)

    #full_map = [[8, 1], [2, 3]]
    #printMap(full_map)
    #make the larger map:
    size_to_multiply = 5
    large_map = []
    orig_width = len(full_map[0])
    orig_height = len(full_map)
    new_width = orig_width * size_to_multiply
    new_height = orig_height * size_to_multiply
    for row in range(new_height):
        row_zeros = []
        for col in range(new_width):
            row_zeros.append(0)
        large_map.append(row_zeros)
    for row in range(new_height):
        for col in range(new_width):
            orig_row = row % orig_height
            orig_col = col % orig_width
            new_val = (((full_map[orig_row][orig_col] - 1) + (int(col / orig_width)) + (int(row / orig_height))) % 9) + 1
            large_map[row][col] = new_val
    #printMap(large_map)

    map_size_horiz = len(large_map[0])
    map_size_vert = len(large_map)
    max_dist = map_size_horiz + map_size_horiz
    print(max_dist)

    #for i in range(8):
    #    number_to_remove = i + 1
    #    reduceMap(full_map, number_to_remove)

    global risk_map
    risk_map = np.zeros((map_size_vert,map_size_horiz),int)#(rows, columns)
    risk_map.fill(4000)
    print(f"Rows: {risk_map.shape[0]}")
    print(f"Cols: {risk_map.shape[1]}")
    risk_map[0, 0] = 0
    #print(risk_map)
    loop_count = 10
    for loopno in range(loop_count):
        for man_dist in range(1,max_dist):
            #print(f"Manhattan Distance Check: {man_dist}")
            list_of_coords = []
            for i in range(man_dist + 1):
                list_of_coords.append([i , (man_dist - i)])
            filtered_coords = filterList(list_of_coords)
            #print(f"Coords to Check: {filtered_coords}")
            for coord in filtered_coords:
                risk_map[coord[0], coord[1]] = man_dist#<-- shows the man-distance progression
                #cost to enter this coordinate =
                cost_to_enter = large_map[coord[0]][coord[1]]
                lowest_neighbor_loc = get_lowest_neighbor(coord[1], coord[0])
                
                if lowest_neighbor_loc == None:
                    lowest_neighbor_risk = 5
                else:
                    lowest_neighbor_risk = risk_map[lowest_neighbor_loc[0], lowest_neighbor_loc[1]]
                #print(f"  Lowest neighbor location: {lowest_neighbor_loc}, ")
                #print(lowest_neighbor_risk)
                risk_map[coord[0], coord[1]] = cost_to_enter + lowest_neighbor_risk
            #printMap(full_map)
        print(f"End of loop #{loopno + 1}")
        #printMap(risk_map)
        #print()


    print("\n\nFinal risk map:")
    #printMap(risk_map)
    
    answer = risk_map[risk_map.shape[0] - 1, risk_map.shape[1] - 1]
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer

def printMap(map_input):
    for row in range(len(map_input)):
        for col in range(len(map_input[0])):
            char = map_input[row][col]
            if len(str(char)) == 1:
                char = " " + str(char)
            print(char, end=" ")
        print()
    print()

def reduceMap(full_map, number_to_remove):
    full_mapcopy = [row[:] for row in full_map]
    #print(f"Keeping up to risk level {number_to_remove}:")
    for row in range(len(full_map)):
        for col in range(len(full_map[0])):
            if full_mapcopy[row][col] in range(number_to_remove + 1,10):
                full_mapcopy[row][col] = " "
    #printMap(full_mapcopy)
    full_mapcopy = []

def get_lowest_neighbor(in_col, in_row):
    global risk_map
    #input a coordinate
    #print(f"Checking Cell: row = {in_row} col = {in_col}")
    #find the value of all neighbors, and return the lowest neighbor's LOCATTION
    if in_row == 0:
        #this is in the top row
        #print(" checking a top row cell")
        #min_risk = bottom risk first.
        min_risk = risk_map[in_row + 1][in_col]
        risk_loc = [in_row + 1, in_col]
        if in_col < (risk_map.shape[1] - 1):#if not the last column
            if risk_map[in_row][in_col + 1] < min_risk:#right
                min_risk = risk_map[in_row][in_col + 1]
                risk_loc = [in_row, in_col + 1]
        if risk_map[in_row][in_col - 1] < min_risk:#left
            min_risk = risk_map[in_row][in_col - 1]
            risk_loc = [in_row, in_col - 1]
    elif in_row == (risk_map.shape[0] - 1):
        #this is in the bottom row
        #print(" checking a bottom row cell")
        #min_risk = top risk first.
        min_risk = risk_map[in_row - 1][in_col]
        risk_loc = [in_row - 1, in_col]
        if in_col < (risk_map.shape[1] - 1):#if not the last column
            if risk_map[in_row][in_col + 1] < min_risk:#right
                min_risk = risk_map[in_row][in_col + 1]
                risk_loc = [in_row, in_col + 1]
        if risk_map[in_row][in_col - 1] < min_risk:#left
            min_risk = risk_map[in_row][in_col - 1]
            risk_loc = [in_row, in_col - 1]
    elif in_col == 0:
        #this is in the left column
        #print(" checking a left column cell")
        #min_risk = top risk first.
        min_risk = risk_map[in_row - 1][in_col]
        risk_loc = [in_row - 1, in_col]
        if risk_map[in_row + 1][in_col] < min_risk:#bottom
            min_risk = risk_map[in_row + 1][in_col]
            risk_loc = [in_row + 1, in_col]
        if risk_map[in_row][in_col + 1] < min_risk:#right
            min_risk = risk_map[in_row][in_col + 1]
            risk_loc = [in_row, in_col + 1]
    elif in_col == (risk_map.shape[1] - 1):
        #this is in the last (right) column
        #print(" checking a right column cell")
        #min_risk = top risk first.
        min_risk = risk_map[in_row - 1][in_col]
        risk_loc = [in_row - 1, in_col]
        if risk_map[in_row + 1][in_col] < min_risk:#bottom
            min_risk = risk_map[in_row + 1][in_col]
            risk_loc = [in_row + 1, in_col]
        if risk_map[in_row][in_col - 1] < min_risk:#left
            min_risk = risk_map[in_row][in_col - 1]
            risk_loc = [in_row, in_col - 1]
    else:
        #this is a middle map location
        #min_risk = top risk first.
        min_risk = risk_map[in_row - 1][in_col]
        risk_loc = [in_row - 1, in_col]
        if risk_map[in_row + 1][in_col] < min_risk:#bottom
            min_risk = risk_map[in_row + 1][in_col]
            risk_loc = [in_row + 1, in_col]
        if risk_map[in_row][in_col + 1] < min_risk:#right
            min_risk = risk_map[in_row][in_col + 1]
            risk_loc = [in_row, in_col + 1]
        if risk_map[in_row][in_col - 1] < min_risk:#left
            min_risk = risk_map[in_row][in_col - 1]
            risk_loc = [in_row, in_col - 1]
    #print(f"  Minimum risk found is: {min_risk}")
    return risk_loc

def filterList(coordinates):
    global risk_map
    max_rows = risk_map.shape[0]
    max_cols = risk_map.shape[1]
    new_list = []
    for coord in coordinates:
        if coord[0] < (max_rows - 0):
            if coord[1] < (max_cols - 0):
                new_list.append(coord)
    return new_list


if __name__ == "__main__":
   aoc2021_15_2("input.txt")