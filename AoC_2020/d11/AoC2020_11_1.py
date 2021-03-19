#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 11.12.20              #
#                       #
# Day 11, Part 1        #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d11/seatmap_testing.txt"
    else:
        testing = 0
        input_file = "./d11/seatmap.txt"

    # Using readline()
    seatmap_file = open(input_file, 'r')
    rowcount = 0
    seat_data = []

    while True:
        # Get next line from file
        line = seatmap_file.readline().strip()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        seat_data.append(line)
        rowcount += 1

    seatmap_file.close()

    answer = 0


    header_footer = "." * (len(seat_data[0]) + 2)
    padded_map = [header_footer]
    for i in seat_data:
        padded_map.append(str("." + i + "."))
    padded_map += [header_footer]
    seprated_map = []
    for i in range(len(padded_map)):
        seprated_map.append(list(padded_map[i]))

    #print()
    origMap = seprated_map
    tempMap = []
    for i in range(len(origMap)):
        tempMap.append(origMap[i].copy())
    printMap("Original Map", origMap)
    #printMap("Temp Map", tempMap)
    #origMap.printMap()
    #origMap.myDimensions()

    y = 1
    x = 0
    print(neighbor_count(origMap, x, y))
    print()

    for i in range(1200):
        print("Cycle #{}".format(i + 1))
        #printMap("New Orig Map", origMap)
        for row in range(len(seat_data)):
            for column in range(len(seat_data[0])):
                #print("ROW: {}, COL: {}".format(row, column))
                #print(origMap[row + 1][column + 1], end=" ")
                #if the seat is empty...
                if origMap[row + 1][column + 1] == "L":
                    #print(" --> seat is empty")
                    #check if it has any occupied neighbors
                    nb_count = neighbor_count(origMap, row, column)
                    #print("Neighbor_Count = {}".format(nb_count))
                    if nb_count == 0:
                        #print("Adding a person to this empty seat.")
                        #print(origMap.map_data[column + 1][row + 1])
                        tempMap[row + 1][column + 1] = "#"
                #if the seat is occupied...
                elif origMap[row + 1][column + 1] == "#":
                    #print(" --> seat is occupied")
                    #check if it has 4 or more adjacent neighbors
                    nb_count = neighbor_count(origMap, row, column)
                    #print("Neighbor_Count = {}".format(nb_count))
                    if nb_count >= 4:
                        #print("Remove the person from this seat.")
                        #print(origMap.map_data[column + 1][row + 1])
                        tempMap[row + 1][column + 1] = "L"
                else:
                    #print(" --> this is a floor.")
                    pass
                #print(tempMap[row + 1][column + 1])
        #printMap("Ending Map", tempMap)
        if origMap == tempMap:
            break

        origMap = []
        for r in range(len(tempMap)):
            origMap.append(tempMap[r].copy())
        #printMap("New Orig Map", origMap)

    #print final map just for fun
    printMap("Final Map", origMap)

    # count occipied seats in origMap
    occ_count = 0
    for i in range(len(origMap)):
        for j in range(len(origMap[0])):
            if origMap[i][j] == "#":
                occ_count += 1
    print("\nAnswer Found: {}".format(occ_count))

    answer = occ_count

    print('\n\ndone')
    return answer


class seatmap:
    def __init__(self, name, map_data):
        #add floor borders to the raw map data
        header_footer = "." * (len(map_data[0]) + 2)
        padded_map = [header_footer]
        for i in map_data:
            padded_map.append(str("." + i + "."))
        padded_map += [header_footer]
        seprated_map = []
        for i in range(len(padded_map)):
            seprated_map.append(list(padded_map[i]))
        self.name = name
        self.map_data = seprated_map.copy()
        self.original_map = seprated_map
        #Global H & W (meaning with the flooe=r borders)
        self.width = len(seprated_map[0])
        self.height = len(seprated_map)

    def printMap(self):
        print("0--> X\n|\nv Y")
        print(self.name)
        for i in self.map_data:
            for j in i:
                print(j, end=" ")
            print()

    def myDimensions(self):
        print("\nMap Dimensions (hXw): {}X{}\n  (1 floor padding added to this value)".format(self.height, self.width))

    def resetMap(self):
        self.map_data = self.original_map.copy()

    def changeSeat(self, y, x, val):
        self.map_data[int(y)][int(x)] = val

    def neighbor_count(self, me_y, me_x):
        #convert to global map (with borders)
        me_X = me_x + 1
        me_Y = me_y + 1
        people_count = 0
        #above ppl count:
        if self.map_data[me_Y - 1][me_X - 1] == "#":
            people_count += 1
        if self.map_data[me_Y - 1][me_X - 0] == "#":
            people_count += 1
        if self.map_data[me_Y - 1][me_X + 1] == "#":
            people_count += 1
        #same row count:
        if self.map_data[me_Y - 0][me_X - 1] == "#":
            people_count += 1
        if self.map_data[me_Y - 0][me_X + 1] == "#":
            people_count += 1
        #below ppl count:
        if self.map_data[me_Y + 1][me_X - 1] == "#":
            people_count += 1
        if self.map_data[me_Y + 1][me_X - 0] == "#":
            people_count += 1
        if self.map_data[me_Y + 1][me_X + 1] == "#":
            people_count += 1

        return people_count


def neighbor_count(mapdata, me_y, me_x):
    #convert to global map (with borders)
    me_X = me_x + 1
    me_Y = me_y + 1
    people_count = 0
    #above ppl count:
    if mapdata[me_Y - 1][me_X - 1] == "#":
        people_count += 1
    if mapdata[me_Y - 1][me_X - 0] == "#":
        people_count += 1
    if mapdata[me_Y - 1][me_X + 1] == "#":
        people_count += 1
    #same row count:
    if mapdata[me_Y - 0][me_X - 1] == "#":
        people_count += 1
    if mapdata[me_Y - 0][me_X + 1] == "#":
        people_count += 1
    #below ppl count:
    if mapdata[me_Y + 1][me_X - 1] == "#":
        people_count += 1
    if mapdata[me_Y + 1][me_X - 0] == "#":
        people_count += 1
    if mapdata[me_Y + 1][me_X + 1] == "#":
        people_count += 1

    return people_count

def printMap(name, seatingchart):
    print("0--> X\n|\nv Y")
    print(name)
    for i in seatingchart:
        for j in i:
            print(j, end=" ")
        print()



if __name__ == "__main__":
    main("r")