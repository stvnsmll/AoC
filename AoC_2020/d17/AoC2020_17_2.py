#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 12.01.21              #
#                       #
# Day 17, Part 2        #
#########################
import numpy as np

def main(test):
    import numpy as np
    from datetime import datetime
    startTime = datetime.now()

    if test == 't':
        testing = 1
        input_file = "./d17/initialstate_testing.txt"
    else:
        testing = 0
        input_file = "./d17/initialstate.txt"

    # Using readline()
    initstate_file = open(input_file, 'r')
    initstate_data = []

    while True:
        # Get next line from file
        line = initstate_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        initstate_data.append(line.strip())

    initstate_file.close()


    for i in initstate_data:
        print(i)
    print()
    print(initstate_data)

    '''    Cell Orientation

     +------> (+)x
     | .#.
     | ..#
     | ###
     |
     v (+)y


    '''

    global cell_dict
    global cell_count

    cell_dict = {}
    cell_count = 0
    #load the data in class objects of Cell
    for row in range(len(initstate_data)):
        for col in range(len(initstate_data[row])):
            cell_name = str(col) + "^" + str(row) + "^0^0"
            startstate = initstate_data[row][col]
            #print(f"New Cell: {cell_name} --> {startstate}")
            cell_dict[cell_name] = Cell(cell_count, cell_name, col, row, 0, 0, startstate)
            cell_count += 1

    global new_cells

    new_cells = []

    for j in range(6):#loop it 6 times
        print(f"Round #{(j + 1)}")

        for i in cell_dict:
            cell_dict[i].getMyNewState()

        #print(new_cells)
        cells_to_check = new_cells.copy()
        for i in cells_to_check:
            #print(i)
            new_cells.remove(i)
            address = i.split("^")
            new_x = int(address[0])
            new_y = int(address[1])
            new_z = int(address[2])
            new_w = int(address[3])
            cell_dict[i] = Cell(cell_count, i, new_x, new_y, new_z, new_w, ".")
            #print(f"NEW Cell {cell_dict[i].name}")
            cell_dict[i].getMyNewState()
            cell_count += 1
            #print(new_cells)

        for i in cell_dict:
            cell_dict[i].setMyNewState()

    total_active_count = 0
    for i in cell_dict:
        if cell_dict[i].active_state == "#":
            total_active_count += 1

    answer = total_active_count

    #print_full_map()

    print("\nAnswer is: {}".format(answer))


    print('\n\ndone')
    print(f"Runtime Duration: {(datetime.now() - startTime)}")
    return answer


class Cell:
    def __init__(self, refNo, cell_name, global_x, global_y, global_z, global_w, state):
        self.refNo = refNo
        self.name = cell_name
        self.myX = global_x
        self.myY = global_y
        self.myZ = global_z
        self.myW = global_w
        self.active_state = state
        self.next_state = "."
        '''    Cell Orientation
         +------> (+)x
         | .#.
         | ..#
         | ###
         |
         v (+)y             '''

    def getMyNewState(self):
        #Getting the neighbors:
        #    Same-level neighbors.
        top_left = str(self.myX - 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ) + "^" + str(self.myW)
        top_mid = str(self.myX - 0) + "^" + str(self.myY - 1) + "^" + str(self.myZ) + "^" + str(self.myW)
        top_right = str(self.myX + 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ) + "^" + str(self.myW)
        mid_left = str(self.myX - 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ) + "^" + str(self.myW)
        mid_right = str(self.myX + 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ) + "^" + str(self.myW)
        bottom_left = str(self.myX - 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ) + "^" + str(self.myW)
        bottom_mid = str(self.myX - 0) + "^" + str(self.myY + 1) + "^" + str(self.myZ) + "^" + str(self.myW)
        bottom_right =  str(self.myX + 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ) + "^" + str(self.myW)
        #    Above neighbors
        up_top_left = str(self.myX - 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW)
        up_top_mid = str(self.myX - 0) + "^" + str(self.myY - 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW)
        up_top_right = str(self.myX + 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW)
        up_mid_left = str(self.myX - 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ + 1) + "^" + str(self.myW)
        up_mid_mid = str(self.myX - 0) + "^" + str(self.myY - 0) + "^" + str(self.myZ + 1) + "^" + str(self.myW)
        up_mid_right = str(self.myX + 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ + 1) + "^" + str(self.myW)
        up_bottom_left = str(self.myX - 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW)
        up_bottom_mid = str(self.myX - 0) + "^" + str(self.myY + 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW)
        up_bottom_right =  str(self.myX + 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW)
        #   Below neighbors
        down_top_left = str(self.myX - 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW)
        down_top_mid = str(self.myX - 0) + "^" + str(self.myY - 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW)
        down_top_right = str(self.myX + 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW)
        down_mid_left = str(self.myX - 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ - 1) + "^" + str(self.myW)
        down_mid_mid = str(self.myX - 0) + "^" + str(self.myY - 0) + "^" + str(self.myZ - 1) + "^" + str(self.myW)
        down_mid_right = str(self.myX + 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ - 1) + "^" + str(self.myW)
        down_bottom_left = str(self.myX - 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW)
        down_bottom_mid = str(self.myX - 0) + "^" + str(self.myY + 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW)
        down_bottom_right =  str(self.myX + 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW)

        # W below!
        #    Same-level neighbors.
        wD_top_left = str(self.myX - 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ) + "^" + str(self.myW - 1)
        wD_top_mid = str(self.myX - 0) + "^" + str(self.myY - 1) + "^" + str(self.myZ) + "^" + str(self.myW - 1)
        wD_top_right = str(self.myX + 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ) + "^" + str(self.myW - 1)
        wD_mid_left = str(self.myX - 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ) + "^" + str(self.myW - 1)
        wD_mid_mid = str(self.myX - 0) + "^" + str(self.myY - 0) + "^" + str(self.myZ) + "^" + str(self.myW - 1)
        wD_mid_right = str(self.myX + 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ) + "^" + str(self.myW - 1)
        wD_bottom_left = str(self.myX - 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ) + "^" + str(self.myW - 1)
        wD_bottom_mid = str(self.myX - 0) + "^" + str(self.myY + 1) + "^" + str(self.myZ) + "^" + str(self.myW - 1)
        wD_bottom_right =  str(self.myX + 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ) + "^" + str(self.myW - 1)
        #    Above neighbors
        wD_up_top_left = str(self.myX - 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW - 1)
        wD_up_top_mid = str(self.myX - 0) + "^" + str(self.myY - 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW - 1)
        wD_up_top_right = str(self.myX + 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW - 1)
        wD_up_mid_left = str(self.myX - 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ + 1) + "^" + str(self.myW - 1)
        wD_up_mid_mid = str(self.myX - 0) + "^" + str(self.myY - 0) + "^" + str(self.myZ + 1) + "^" + str(self.myW - 1)
        wD_up_mid_right = str(self.myX + 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ + 1) + "^" + str(self.myW - 1)
        wD_up_bottom_left = str(self.myX - 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW - 1)
        wD_up_bottom_mid = str(self.myX - 0) + "^" + str(self.myY + 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW - 1)
        wD_up_bottom_right =  str(self.myX + 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW - 1)
        #   Below neighbors
        wD_down_top_left = str(self.myX - 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW - 1)
        wD_down_top_mid = str(self.myX - 0) + "^" + str(self.myY - 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW - 1)
        wD_down_top_right = str(self.myX + 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW - 1)
        wD_down_mid_left = str(self.myX - 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ - 1) + "^" + str(self.myW - 1)
        wD_down_mid_mid = str(self.myX - 0) + "^" + str(self.myY - 0) + "^" + str(self.myZ - 1) + "^" + str(self.myW - 1)
        wD_down_mid_right = str(self.myX + 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ - 1) + "^" + str(self.myW - 1)
        wD_down_bottom_left = str(self.myX - 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW - 1)
        wD_down_bottom_mid = str(self.myX - 0) + "^" + str(self.myY + 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW - 1)
        wD_down_bottom_right =  str(self.myX + 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW - 1)

        # W above!
        #    Same-level neighbors.
        wA_top_left = str(self.myX - 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ) + "^" + str(self.myW + 1)
        wA_top_mid = str(self.myX - 0) + "^" + str(self.myY - 1) + "^" + str(self.myZ) + "^" + str(self.myW + 1)
        wA_top_right = str(self.myX + 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ) + "^" + str(self.myW + 1)
        wA_mid_left = str(self.myX - 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ) + "^" + str(self.myW + 1)
        wA_mid_mid = str(self.myX - 0) + "^" + str(self.myY - 0) + "^" + str(self.myZ) + "^" + str(self.myW + 1)
        wA_mid_right = str(self.myX + 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ) + "^" + str(self.myW + 1)
        wA_bottom_left = str(self.myX - 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ) + "^" + str(self.myW + 1)
        wA_bottom_mid = str(self.myX - 0) + "^" + str(self.myY + 1) + "^" + str(self.myZ) + "^" + str(self.myW + 1)
        wA_bottom_right =  str(self.myX + 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ) + "^" + str(self.myW + 1)
        #    Above neighbors
        wA_up_top_left = str(self.myX - 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW + 1)
        wA_up_top_mid = str(self.myX - 0) + "^" + str(self.myY - 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW + 1)
        wA_up_top_right = str(self.myX + 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW + 1)
        wA_up_mid_left = str(self.myX - 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ + 1) + "^" + str(self.myW + 1)
        wA_up_mid_mid = str(self.myX - 0) + "^" + str(self.myY - 0) + "^" + str(self.myZ + 1) + "^" + str(self.myW + 1)
        wA_up_mid_right = str(self.myX + 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ + 1) + "^" + str(self.myW + 1)
        wA_up_bottom_left = str(self.myX - 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW + 1)
        wA_up_bottom_mid = str(self.myX - 0) + "^" + str(self.myY + 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW + 1)
        wA_up_bottom_right =  str(self.myX + 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ + 1) + "^" + str(self.myW + 1)
        #   Below neighbors
        wA_down_top_left = str(self.myX - 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW + 1)
        wA_down_top_mid = str(self.myX - 0) + "^" + str(self.myY - 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW + 1)
        wA_down_top_right = str(self.myX + 1) + "^" + str(self.myY - 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW + 1)
        wA_down_mid_left = str(self.myX - 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ - 1) + "^" + str(self.myW + 1)
        wA_down_mid_mid = str(self.myX - 0) + "^" + str(self.myY - 0) + "^" + str(self.myZ - 1) + "^" + str(self.myW + 1)
        wA_down_mid_right = str(self.myX + 1) + "^" + str(self.myY - 0) + "^" + str(self.myZ - 1) + "^" + str(self.myW + 1)
        wA_down_bottom_left = str(self.myX - 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW + 1)
        wA_down_bottom_mid = str(self.myX - 0) + "^" + str(self.myY + 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW + 1)
        wA_down_bottom_right =  str(self.myX + 1) + "^" + str(self.myY + 1) + "^" + str(self.myZ - 1) + "^" + str(self.myW + 1)



        neighbor_cells_list = [top_left, top_mid, top_right, mid_left, mid_right, bottom_left, bottom_mid, bottom_right,
                               up_top_left, up_top_mid, up_top_right, up_mid_left, up_mid_mid, up_mid_right, up_bottom_left, up_bottom_mid, up_bottom_right,
                               down_top_left, down_top_mid, down_top_right, down_mid_left, down_mid_mid, down_mid_right, down_bottom_left, down_bottom_mid, down_bottom_right, wD_mid_mid, wA_mid_mid,
                               wD_top_left, wD_top_mid, wD_top_right, wD_mid_left, wD_mid_right, wD_bottom_left, wD_bottom_mid, wD_bottom_right, wD_up_top_left, wD_up_top_mid, wD_up_top_right, wD_up_mid_left, wD_up_mid_mid, wD_up_mid_right, wD_up_bottom_left, wD_up_bottom_mid, wD_up_bottom_right, wD_down_top_left, wD_down_top_mid, wD_down_top_right, wD_down_mid_left, wD_down_mid_mid, wD_down_mid_right, wD_down_bottom_left, wD_down_bottom_mid, wD_down_bottom_right, wA_top_left, wA_top_mid, wA_top_right, wA_mid_left, wA_mid_right, wA_bottom_left, wA_bottom_mid, wA_bottom_right, wA_up_top_left, wA_up_top_mid, wA_up_top_right, wA_up_mid_left, wA_up_mid_mid, wA_up_mid_right, wA_up_bottom_left, wA_up_bottom_mid, wA_up_bottom_right, wA_down_top_left, wA_down_top_mid, wA_down_top_right, wA_down_mid_left, wA_down_mid_mid, wA_down_mid_right, wA_down_bottom_left, wA_down_bottom_mid, wA_down_bottom_right]

        #print(len(neighbor_cells_list))

        expand_map = 0
        if self.active_state == "#":
            expand_map = 1

        #print(f"Cell {self.name}")
        #if self.name == "2^2^1":
        #    print(f"Cell {self.name} (initially {self.active_state})")
        #    print(neighbor_cells_list)
        active_count = 0
        for i in neighbor_cells_list:
            if i in cell_dict:
                cell_state = cell_dict[i].active_state
                #print(f"exists, and the value is: {cell_state}")
                if cell_state == "#":
                    #if self.name == "2^2^1":
                    #    print(f"Found an active cell: {i}")
                    #    print(f"  mid active cell count = {active_count}")
                    active_count += 1
            else:#the cell didnt exsist
                #print("does not exist")
                if expand_map == 1:
                    #print("expand_to_here!!")
                    if i not in new_cells:
                        new_cells.append(i)
                        #if i == "2^2^1":
                        #    print("BINGO!!!!!")
                            #print(new_cells)

            #print()
        #if self.name == "2^2^1":
        #    print(f"  My Active Neighbor Count: {active_count}")
        if self.active_state == "#": #cell was active
            if active_count in range(2,4):
                self.next_state = "#"
            else:
                self.next_state = "."
        else: #cell was inactive
            if active_count == 3:
                self.next_state = "#"
            else:
                self.next_state = "."
        #if self.name == "2^2^1":
        #    print(f"  My next state will be: {self.next_state}\n")


    def setMyNewState(self):
        self.active_state = self.next_state
        self.next_state = "."


def print_full_map():
    max_val = 0
    for i in cell_dict:
        address = [abs(int(x)) for x in cell_dict[i].name.split("^")]
        #print(address)
        if max(address) > max_val:
            max_val = max(address)

    #create a np array of size  = (max_val * 2) + 1
    size = (max_val * 2) + 1
    #                     z    y     x
    full_map = np.full((size, size, size, size), ".")
    for i in cell_dict:
        address = [int(x) for x in cell_dict[i].name.split("^")]
        my_x = address[0] + max_val # column
        my_y = address[1] + max_val # row
        my_z = address[2] + max_val # depth
        my_w = address[3] + max_val
        if cell_dict[i].active_state == "#":
            full_map[my_w][my_z][my_y][my_x] = "#"

    print(full_map)



def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1



if __name__ == "__main__":
    main("r")