#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 14.01.21              #
#                       #
# Day 24, Part 1        #
#########################


def main(test):
    from datetime import datetime
    startTime = datetime.now()

    if test == 't':
        testing = 1
        input_file = "./d24/tilelist_testing.txt"
    else:
        testing = 0
        input_file = "./d24/tilelist.txt"

    # Using readline()
    tilelist_file = open(input_file, 'r')
    tilelist_data = []

    while True:
        # Get next line from file
        line = tilelist_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        tilelist_data.append(line.strip())

    tilelist_file.close()

    all_instructions = []
    for i in tilelist_data:
        #print(i)
        partA = i.replace("se","2").replace("sw","3").replace("nw","5").replace("ne","6")
        partB = partA.replace("e", "1").replace("w","4")
        tile_inst = list(map(int, list(partB)))
        all_instructions.append(tile_inst)
        #print(cell_inst)
        #print()
    print()

    #print(all_instructions)

    '''    Tile Orientation:
                        e = 1     (x + 2, y + 0)
          5     6       se = 2    (x + 1, y + 1)
            / \         sw = 3    (x - 1, y + 1)
         4  | |  1      w = 4     (x - 2, y - 0)
            \ /         nw = 5    (x - 1, y - 1)
          3      2      ne = 6    (x + 1, y - 1)

    '''

    global tile_dict

    tile_dict = {}
    instruction_count = 0
    #iterate through each row of the input list
    for instruct in all_instructions:
        #print(f"Working on instruction #{instruction_count}")
        # each instruction always starts at the 0,0 reference tile
        current_x = 0
        current_y = 0

        #get the adress of the next tile
        next_addr = ""
        for step in instruct:
            #print(step)
            if step == 1:
                new_x = current_x + 2
                new_y = current_y
            elif step == 2:
                new_x = current_x + 1
                new_y = current_y + 1
            elif step == 3:
                new_x = current_x - 1
                new_y = current_y + 1
            elif step == 4:
                new_x = current_x - 2
                new_y = current_y
            elif step == 5:
                new_x = current_x - 1
                new_y = current_y - 1
            elif step == 6:
                new_x = current_x + 1
                new_y = current_y - 1

            next_addr = str(new_x) + "^" + str(new_y)
            if next_addr not in tile_dict:
                #create new tile at this location
                tile_dict[next_addr] = Tile(next_addr, new_x, new_y)
                #print(f"Created a new tile at location {next_addr}")

            #set current location to the new location
            current_x = new_x
            current_y = new_y

        #last addrress = "next_addr"
        tile_dict[next_addr].switch()

        instruction_count += 1
        #print()

    black_tile_count = 0
    for i in tile_dict:
        if tile_dict[i].color == 1:
            black_tile_count += 1

    answer = black_tile_count

    print("\nAnswer is: {}".format(answer))


    print('\n\ndone')
    print(f"Runtime Duration: {(datetime.now() - startTime)}")
    return answer


class Tile:
    def __init__(self, tile_name, global_x, global_y):
        self.name = tile_name
        self.myX = global_x
        self.myY = global_y
        self.color = 0
        #            0 = white, 1 = black  (tiles start white)

        '''    Tile Orientation  (x,y)
            0   1   2   3   4   5   6
         +------> (+)x
     0   | 0,0     2,0     4,0     6,0
     1   |     1,1     3,1     5,1
     2   | 0,2     2,2     4,2     6,2
     3   |     1,3     3,3     5,3
     4   | 0,4     2,4     4,4     6,4
         |
         v (+)y                        '''

    def switch(self):
        if self.color == 0:
            self.color = 1
        else:
            self.color = 0



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