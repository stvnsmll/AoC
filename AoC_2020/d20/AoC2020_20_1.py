#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 26.12.20              #
#                       #
# Day 20, Part 1        #
#########################


def main(test):

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
    tiles_dict[0].printMap(0)
    print()

    every_single_border = []
    for i in range(len(tiles_dict)):
        #print(tiles_dict[i].allborders)
        every_single_border += tiles_dict[i].allborders

    #print(every_single_border)
    corner_pieces = []

    for i in range(len(tiles_dict)):
        edge_count = 0
        for j in range(8):
            num_to_check = tiles_dict[i].allborders[j]
            edge_check = every_single_border.count(num_to_check)
            if edge_check == 2:
                pass
            elif edge_check == 1:
                #print("Found an edge piece")
                edge_count += 1
        if edge_count == 4:
            print(f"FOUND A CORNER! Tile ID: {tiles_dict[i].number}")
            corner_pieces.append(int(tiles_dict[i].number))

    print()
    print(f"Corner Piece IDs: {corner_pieces}")


    answer = 1
    for i in range(4):
        answer *= corner_pieces[i]




    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
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

        border_vals = [top_int, pot_int, bottom_int, mottob_int, left_int, tfel_int, right_int, thgir_int]

        self.number = tile_number
        self.refNo = refNo
        self.mydata = tile_data
        self.mydatadigits = tile_data_1s0s
        self.allborders = border_vals

    def printMap(self, var):
        if var == 1:
            maptoprint = self.mydata
        elif var == 0:
            maptoprint = self.mydatadigits
        else:
            print("Input error, must be a 1 or a 0")
            return 1
        for i in maptoprint:
            print(i)
        return 0

'''
    def checkforrepeat(self):
        if self.stepused == -1:
            return False
        else:
            return True
'''


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