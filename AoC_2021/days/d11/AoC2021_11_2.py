#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 12.12.21              #
#                       #
# Day 11, Part 2        #
#########################

from datetime import datetime
import numpy as np

tmp_map = np.zeros((12, 12), int)

def aoc2021_11_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 11, Part 2\n~~ running as a test ~~")

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
    growth = 1
    rows = len(input_data) + (2 * growth)
    columns = len(input_data[0]) + (2 * growth)

    starting_map = np.zeros((rows, columns), int)
    starting_map.fill(1)
    for row in range(len(input_data)):
        for col in range(len(input_data[0])):
            starting_map[row + 1][col + 1] = input_data[row][col]
    print(starting_map)
    print()

    global tmp_map

    #    example of a step
    # increment each up by 1

    #this one just to get things started...
    tmp_map = starting_map

    answer = 0

    total_flashes = 0
    number_of_steps = 3000
    for i in range(number_of_steps):
        #then... starting the real loop:
        #tmp_map = starting_map
        #add one to all of the values (and count the number of initial flashers)
        flash_count = 0
        for row in range(1,(rows - 1)):
            for col in range(1,(rows - 1)):
                tmp_map[row][col] += 1

        #print(tmp_map)
        #propogate flashes
        exitloop1 = 0
        while exitloop1 == 0:
            response = 0
            # increase value if a neighbor is > 9
            #print("\n  INCREMENT neighbors start:")
            for col in range(1,(rows - 1)):
                for row in range(1,(rows - 1)):
                    if tmp_map[row][col] > 9:
                        #This is a flash!
                        #print(f"\n   Flash at {row}, {col}")
                        tmp_map[row][col] = -50
                        flash_count += 1
                        response = increment_neighbors(row, col)
            if response == 0:
                #no neighbors flashed
                exitloop1 = 1
                #one final check to make sure there are no more flashing values...
                for row in range(1,(rows - 1)):
                    for col in range(1,(columns - 1)):
                        if tmp_map[row][col] > 9:
                            exitloop1 = 0
            else:
                exitloop1 = 0

            #print("\n\n")
            #print(tmp_map)
            #print(f"Exit loop? (done flashing): {exitloop1}")

        #convert all negative numbers to 0 and count as a flash
        #reset all perimeter values to 1
        flash_count_2 = 0
        for row in range(rows):
            for col in range(columns):
                if row == 0 or row == (rows - 1):
                    tmp_map[row][col] = 1
                if col == 0 or col == (columns - 1):
                    tmp_map[row][col] = 1
                if tmp_map[row][col] < 0:
                    flash_count_2 += 1
                    tmp_map[row][col] = 0
        if flash_count != flash_count_2:
            print("ERROR FOUND -- flash count not matching")
            return 6
        
        #if i < 19:
        #    print(tmp_map, end="\n\n")
        if (i + 1)%10 == 0:
            #print(tmp_map, end="\n\n")
            print(f"AFTER STEP {i + 1}: ({flash_count} flashes)")
        total_flashes += flash_count
        if flash_count == 100:
            print("found it")
            answer = (i + 1)
            print(f"AFTER STEP {i + 1}: ({flash_count} flashes)")
            break
        
    if answer == 0:
        print(f"NOT ENOUGH CYCLES, no common flash found within {number_of_steps} cycles.")
    
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer

def increment_neighbors(row, col):#returns 1 if the flashing continues, 0 if no flashes
    global tmp_map
    tmp_map[row - 1][col - 1] += 1
    topleft = tmp_map[row - 1][col - 1]

    tmp_map[row - 1][col - 0] += 1
    topmid = tmp_map[row - 1][col - 0]

    tmp_map[row - 1][col + 1] += 1
    topright = tmp_map[row - 1][col + 1]

    tmp_map[row - 0][col - 1] += 1
    midleft = tmp_map[row - 0][col - 1]

    tmp_map[row - 0][col + 1] += 1
    midright = tmp_map[row - 0][col + 1]

    tmp_map[row + 1][col - 1] += 1
    bottomleft = tmp_map[row + 1][col - 1]

    tmp_map[row + 1][col - 0] += 1
    bottommid = tmp_map[row + 1][col - 0]

    tmp_map[row + 1][col + 1] += 1
    bottomright = tmp_map[row + 1][col + 1]
    
    my_neighbors = [topleft, topmid, topright, midleft, midright, bottomleft, bottommid, bottomright]
    if max(my_neighbors) > 9:
        #a new flash happened
        return 1
    #else, no new flashes happened
    return 0


if __name__ == "__main__":
   aoc2021_11_2("input.txt")