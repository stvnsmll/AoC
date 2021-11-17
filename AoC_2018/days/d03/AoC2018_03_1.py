#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 14.11.21              #
#                       #
# Day 03, Part 1        #
#########################

from datetime import datetime
import numpy as np

def aoc2018_03_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 03, Part 1\n~~ running as a test ~~")

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
    
    """#view the input data
        for i in input_data:
            print(i)
        print(input_data) """

    #convert the data into objects
    all_fabrics = []
    for line in input_data:
        all_fabrics.append(FabricMap(line))

    #get the max size of the map to create the blank np array
    global_max_X = 0
    global_max_Y = 0

    for fabricmap in all_fabrics:
        if fabricmap.maxX > global_max_X:
            global_max_X = fabricmap.maxX
        if fabricmap.maxY > global_max_Y:
            global_max_Y = fabricmap.maxY

    global_max_X += 1
    global_max_Y += 1

    #print(global_max_X)
    #print(global_max_Y)

    #generate the blank np array
    full_fabric_map = np.zeros((global_max_Y, global_max_X), str)
    #print(full_fabric_map)

    #for each cell of each fabricmap, fill in the full_fabric_map with the name if it was '', else X
    for fabricmap in all_fabrics:
        x_offset = fabricmap.fromLeft
        y_offset = fabricmap.fromTop
        #first go by rows
        for x_pos in range(fabricmap.width):
            for y_pos in range(fabricmap.height):
                #print(x_pos)
                #print(y_pos)
                global_x_pos = x_offset + x_pos
                global_y_pos = y_offset + y_pos
                #print(global_x_pos)
                #print(global_y_pos)
                if full_fabric_map[global_y_pos, global_x_pos] == '':
                    full_fabric_map[global_y_pos, global_x_pos] = fabricmap.name
                else:
                    full_fabric_map[global_y_pos, global_x_pos] = "O"

    overlap_count = 0
    for line in full_fabric_map:
        for i in line:
            if i == "O":
                overlap_count += 1

    #print(full_fabric_map)

    print(f"Solution is: {overlap_count} (the number of overlapping fabric spaces)")
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    answer = overlap_count
    return answer


        

class FabricMap:
    '''
    Incoming code format: '#1 @ 1,3: 4x4' --> '#name @ x_gap,y_gap: x_width x y_height'
    Coordinate Orientation

     +-----------> (+)x
     | ......
     | ......
     | ......
     | .1111.
     | .1111.
     | .1111.
     | .1111.
     | ......
     | 
     v (+)y


    '''
    def __init__(self, code):
        code = code.replace("#","").replace(" @ ","x").replace(",","x").replace(": ","x")
        split_code = code.split("x")
        self.name = split_code[0]
        self.fromLeft = int(split_code[1])
        self.fromTop = int(split_code[2])
        self.width = int(split_code[3])
        self.height = int(split_code[4])
        self.maxX = self.fromLeft + self.width
        self.maxY = self.fromTop + self.height
        #print(self.maxX)
        #print(self.maxY)    

if __name__ == "__main__":
   aoc2018_03_1("input.txt")