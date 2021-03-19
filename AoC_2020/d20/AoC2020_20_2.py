#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 26.12.20              #
#                       #
# Day 20, Part 2        #
#########################
import numpy as np
import re


def main(test):
    import numpy as np
    import re
    from math import sqrt
    from datetime import datetime
    startTime = datetime.now()

    if test == 't':
        testing = 1
        input_file = "./d20/tileData_testing.txt"
    else:
        testing = 0
        input_file = "./d20/tileData.txt"

    # Using readline()
    tile_file = open(input_file, 'r')
    alltile_data = []

    while True:
        # Get next line from file
        line = tile_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        alltile_data.append(line.strip())

    tile_file.close()

    alltile_data.append("")

    #for i in alltile_data:
    #    print(i)
    #print(alltile_data)

    #split each tile out from the data list, adding them to a tile class
    tile_count = 0
    rowcount = 0
    one_tile_data = []
    tiles_dict = {}
    for i in range(len(alltile_data)):
        if alltile_data[i] == "":
            #print("Saving the prior tile data")
            tiles_dict[tile_count] = Tile(tile_count, one_tile_data)
            #print("Start a new tile.")
            tile_count += 1
            one_tile_data = []
        else:
            one_tile_data.append(alltile_data[i])


    #print(tiles_dict[0].mydata)
    #print("Map of tile ID 1:")
    #tiles_dict[1].printMap(0)

    every_single_border = []
    for i in range(len(tiles_dict)):
        #print(tiles_dict[i].allborders)
        every_single_border += tiles_dict[i].allborders
    print()

    #print("\nAll Borders:")
    #print(every_single_border)
    corner_pieces = []
    edge_list = []

    for i in range(len(tiles_dict)):
        edge_count = 0
        for j in range(8):
            num_to_check = tiles_dict[i].allborders[j]
            edge_check = every_single_border.count(num_to_check)
            if edge_check == 2:
                pass
            elif edge_check == 1:
                #print("Found an edge piece")
                edge_list.append(num_to_check)
                edge_count += 1
        if edge_count == 4:
            #print(f"FOUND A CORNER! Tile ID: {tiles_dict[i].number}")
            corner_pieces.append(int(tiles_dict[i].refNo))

    #print()
    #print(f"Corner Piece IDs: {corner_pieces}")
    #print(f"Edge list is: {edge_list}", end = "\n\n")

    remaining_tiles = {}
    for i in range(len(tiles_dict)):
        remaining_tiles[i] = tiles_dict[i].allborders

    # build the map:
    # start with first corner
    tile_count = len(remaining_tiles)
    #print(int(sqrt(tile_count)))
    size = int(sqrt(tile_count))
    mapA = np.zeros( (size, size) , dtype=np.int64)

    #orient the first corner piece (top and left must be edges)
    first_piece = corner_pieces[0]
    exit = 0
    while exit == 0:
        if (tiles_dict[first_piece].left in edge_list) and (tiles_dict[first_piece].top in edge_list):
            exit = 1
        else:
            tiles_dict[first_piece].rotate_clockwise(1)
            #print("Rotated first tile.")

    #tiles_dict[first_piece].printMap(1)

    # v-- all between here is troubleshooting
    #rotate only to match the puzle sample
    tiles_dict[first_piece].flip_horiz()
    tiles_dict[first_piece].rotate_clockwise(3)
    print()

    #tiles_dict[first_piece].printMap(0)
    #print(tiles_dict[first_piece].left)
    #print(tiles_dict[first_piece].top)
    # ^-- all between here is troubleshooting

    mapA[0][0] = first_piece
    remaining_tiles.pop(first_piece)
    print(mapA)
    last_x = 0
    last_y = 0

    row_header_right = tiles_dict[first_piece].right
    #print(f"*Row header right: {row_header_right}")
    print()

    # i cycles through every tile in the full list to find where each go.
    for i in range(len(tiles_dict) - 1):
        #j increments i + 1 because the first tile is accounted for (in position [0, 0])
        j = i + 1
        # get bottom int of the prior tile
        last_edge = tiles_dict[mapA[last_y][last_x]].mottob
        #print(listToString(tiles_dict[mapA[last_y][last_x]].mydata[9]))
        bottom_int = int(listToString(tiles_dict[mapA[last_y][last_x]].mydata[9]).replace(".","0").replace("#","1")[::], 2)
        #print(bottom_int)
        last_edge = bottom_int
        #print(f"Prior bottom edge = {last_edge}")
        rotate_at_the_top = 0
        if last_edge in edge_list:
            #the prior tile was at the bottom of a column, proceed to the next column and use the row_header_right value
            #print("at the bottom of a column?")
            if last_y == 0:
                #print("NO! Bazinga! \n\n\n terminate")
                #print(f"Last ID is: {tiles_dict[mapA[last_y][last_x]].refNo}")
                tiles_dict[mapA[last_y][last_x]].flip_vert()
                last_edge = int(listToString(tiles_dict[mapA[last_y][last_x]].mydata[9]).replace(".","0").replace("#","1")[::], 2)
            else:
                #print("yes")
                last_edge = row_header_right
                rotate_at_the_top = 1
                #set x ans y
                last_y = -1
                last_x += 1
        #it's NOT the bottom of a column, so use the last_edge as the bottom
        #print(f"Looking for the last edge of: {last_edge}")
        for k in remaining_tiles:
            #print(k)
            if last_edge in remaining_tiles[k]:
                #found the next tile, rotate/flip accordingly
                #print(f"Found the mext tile: {k}")
                if last_edge in [tiles_dict[k].top, tiles_dict[k].right, tiles_dict[k].mottob, tiles_dict[k].left]:
                    #no fliping necessary, only need to rotate:
                    #!!!BOTTOM DOES NEED TO BE FLIPPED!!!!
                    #print("no flipping")#this seems to be ok too!
                    exit = 0
                    while exit == 0:
                        if tiles_dict[k].top == last_edge:
                            exit = 1
                        else:
                            tiles_dict[k].rotate_clockwise(1)
                            #print("looper")
                elif last_edge == tiles_dict[k].pot:
                    #print("1")
                    tiles_dict[k].flip_horiz()
                elif last_edge == tiles_dict[k].thgir:
                    #print("2")
                    tiles_dict[k].rotate_clockwise(3)
                    tiles_dict[k].flip_horiz()
                elif last_edge == tiles_dict[k].bottom:
                    #print("3")
                    tiles_dict[k].rotate_clockwise(2)
                    tiles_dict[k].flip_horiz()
                elif last_edge == tiles_dict[k].tfel:
                    #print("4")#THIS ONE IS OK!!!
                    tiles_dict[k].rotate_clockwise(1)
                    tiles_dict[k].flip_horiz()
                else:
                    print("\n\n *** rotation error *** \n\n")
                    return 1
                if rotate_at_the_top == 1:
                    #this is for top tiles
                    tiles_dict[k].rotate_clockwise(3)
                    row_header_right = tiles_dict[k].right
                    right_list = []
                    for i in range(10):
                        #print(tiles_dict[k].mydata[i][9], end = "")
                        right_list.append(tiles_dict[k].mydata[i][9])
                    right_int = int(listToString(right_list).replace(".","0").replace("#","1")[::], 2)
                    #print(right_int)
                    row_header_right = right_int
                    #print(f"*Row header right: {row_header_right}")
                #manual correction:
                correction_list = [126, 114, 93, 52, 29, 39, 57, 45, 10, 81, 118, 44, 50, 100, 120, 101, 112, 0, 17, 38, 7, 131, 51, 97, 61, 115, 83, 128, 33, 54, 75, 105, 59, 63, 74, 72, 43, 102, 142]
                if testing == 1:
                    correction_list = []
                if k in correction_list:
                    tiles_dict[k].flip_horiz()
                mapA[last_y + 1][last_x] = k
                remaining_tiles.pop(k)
                last_y += 1
                break
        #print(mapA)
        #print(f"New bottom is: {tiles_dict[k].mottob}")
        #print()

    #print()
    print("My map by keys:")
    print(mapA)
    print()

    #stitch together the maps.
    full_map_with_borders = []

    for map_row in range(size):
        for row in range(10):
            #print(row)
            row_string = ""
            for column in range(len(mapA)):
                row_string += str(listToString(tiles_dict[mapA[map_row][column]].mydata[row]) + " ")
            full_map_with_borders.append(row_string)

    counter = 0
    for i in full_map_with_borders:
        counter += 1
        print(i)
        if counter % 10 == 0:
            print()

    #remove borders from each of the final maps.
    for i in tiles_dict:
        tiles_dict[i].trimBorders()

    full_map = []
    total_hash_count = 0
    for map_row in range(size):
        for row in range(8):
            #print(row)
            row_string = ""
            for column in range(len(mapA)):
                row_string += str(listToString(tiles_dict[mapA[map_row][column]].noBorders[row]))
            total_hash_count += row_string.count('#')
            full_map.append(row_string)

    print("\n\nFull Map:\n")
    for i in full_map:
        print(i)

    #coordinates written as full_map[row][column]
    #print(full_map[0][2])
    #should be .
    #print(full_map[2][0])
    #should be #

    print()

    #Manally flip the map
    #flip vertical
    #new_map_a = full_map[::-1]
    #flip horizontal
    new_map_a = []
    for i in full_map:
            new_map_a.append(list(reversed(i)))
    #rotate right
    #new_map_c = list(zip(*new_map_a[::-1]))
    #new_map_d = list(zip(*new_map_a[::-1]))
    new_map_b = list(zip(*new_map_a[::-1]))

    if testing == 1:
        new_map_a = full_map[::-1]
        new_map_b = list(zip(*new_map_a[::-1]))

    new_map = []
    for i in range(len(new_map_b)):
        new_map.append(listToString(new_map_b[i]))

    for i in new_map:
        print(i)

    #look through the "correctly oriented" map for monsters
    lochness_count = 0
    for i in range(len(new_map) - 2):
        midrow = i + 1
        #print(midrow)
        for col in range((size * 8) - 20):
            #print(f"  ^-- {col}")
            mid_str = new_map[midrow][col:(col + 20)]
            bottom_str = new_map[(midrow + 1)][col:(col + 17)]
            top_char = new_map[(midrow - 1)][(col + 18)]
            string_to_check = mid_str + bottom_str + top_char
            if midrow == 10 and col == 51:
                print(string_to_check)
            if re.search("\A(#....##....##....###)(.#..#..#..#..#..#)(#)\Z",string_to_check):
                print(f"Found a monster!!! ({(lochness_count + 1)})", end = "\n  ")
                print(f"Mid-rw = {(midrow + 1)}, Column = {(col + 1)}")
                print(string_to_check)
                lochness_count += 1

    print(f"Lochness count = {lochness_count}")

    print(total_hash_count)
    answer = total_hash_count - (15 * lochness_count)

    print("\nAnswer is: {}".format(answer))


    print('\n\ndone')
    print(f"Runtime Duration: {(datetime.now() - startTime)}")
    return answer


class Tile:
    def __init__(self, refNo, inputdata):
        tile_number = inputdata[0].split()[1].split(":")[0]

        tile_data = []
        tile_data_1s0s = []
        for i in range(10):
            tile_data.append(inputdata[i + 1])
            digits = inputdata[i + 1].replace(".","0").replace("#","1")
            tile_data_1s0s.append(digits)
            #print(inputdata[i + 1])

        top_int = int(tile_data_1s0s[0], 2)
        pot_int = int(tile_data_1s0s[0][::-1], 2)
        bottom_int = int(tile_data_1s0s[9], 2)
        mottob_int = int(tile_data_1s0s[9][::-1], 2)
        left_list = []
        for i in range(10):
            left_list.append(tile_data_1s0s[i][0])
        left_str = listToString(left_list)
        left_int = int(left_str, 2)
        tfel_int = int(left_str[::-1], 2)
        right_list = []
        for i in range(10):
            right_list.append(tile_data_1s0s[i][9])
        right_str = listToString(right_list)
        right_int = int(right_str, 2)
        thgir_int = int(right_str[::-1], 2)

        border_vals = [top_int, pot_int, right_int, thgir_int, bottom_int, mottob_int, left_int, tfel_int]

        self.number = tile_number
        self.refNo = refNo
        self.mydata = tile_data
        self.mydatadigits = tile_data_1s0s
        self.allborders = border_vals
        #change these once the orientation is final
        self.flip = 'normal'
        self.rotation = 0
        self.top = border_vals[0]
        self.pot = border_vals[1]
        self.right = border_vals[2]
        self.thgir = border_vals[3]
        self.bottom = border_vals[4]
        self.mottob = border_vals[5]
        self.left = border_vals[6]
        self.tfel = border_vals[7]

    def printMap(self, var):
        if var == 1:
            maptoprint = self.mydata
        elif var == 0:
            maptoprint = self.mydatadigits
        else:
            print("Input error, must be a 1 or a 0")
            return 1
        for i in maptoprint:
            print(listToString(i))
        return 0

    def rotate_clockwise(self, number):
        #if number = 1, rotate clockwise 1 time, if number is 3: rotate counter clockwise 1 time
        if number == 0:
            print("No rotation operation")
            return 0
        #new_map = list(zip(*self.mydata[::-1]))
        new_map = self.mydata
        for i in range(number):
            new_map = list(zip(*new_map[::-1]))
            new_top = self.left
            new_pot = self.tfel
            new_right = self.top
            new_thgir = self.pot
            new_bottom = self.thgir
            new_mottob = self.right
            new_left = self.mottob
            new_tfel = self.bottom
            Tile.reassign_map(self, new_map, new_top, new_pot, new_right, new_thgir, new_bottom, new_mottob, new_left, new_tfel)
            #print("-R-", end="")
        #Tile.printMap(self,1)

    def flip_vert(self):
        new_map = self.mydata[::-1]
        new_top = self.bottom
        new_pot = self.mottob
        new_right = self.thgir
        new_thgir = self.right
        new_bottom = self.top
        new_mottob = self.pot
        new_left = self.tfel
        new_tfel = self.left
        Tile.reassign_map(self, new_map, new_top, new_pot, new_right, new_thgir, new_bottom, new_mottob, new_left, new_tfel)
        #print("-Fv-", end="")
        #Tile.printMap(self,1)

    def flip_horiz(self):
        new_map = []
        for i in self.mydata:
            new_map.append(list(reversed(i)))
        new_top = self.pot
        new_pot = self.top
        new_right = self.left
        new_thgir = self.tfel
        new_bottom = self.mottob
        new_mottob = self.bottom
        new_left = self.right
        new_tfel = self.thgir
        Tile.reassign_map(self, new_map, new_top, new_pot, new_right, new_thgir, new_bottom, new_mottob, new_left, new_tfel)
        #print("-Fh-", end="")
        #Tile.printMap(self,1)

    def reassign_map(self, new_map, top, pot, right, thgir, bottom, mottob, left, tfel):
        self.mydata = new_map
        self.top = top
        self.pot = pot
        self.right = right
        self.thgir = thgir
        self.bottom = mottob
        self.mottob = bottom
        self.left = left
        self.tfel = tfel

    def trimBorders(self):
        #print(f"Trimming borders for {self.refNo}")
        #remove the top and bottom:
        tmp_map = self.mydata[1:-1]
        middle_map = []
        for i in tmp_map:
            middle_map.append(listToString(i[1:-1]))
        self.noBorders = np.array(middle_map)
        #print(self.noBorders)
        #print(self.noBorders[0])
        #print(self.mydata)
        #print(middle_map)
        #for i in self.mydata:
        #    print(listToString(i))
        #print(f"Final map for: {self.refNo}")
        #for i in middle_map:
        #    print(" " + listToString(i))
        #print()


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