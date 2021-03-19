#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 11.12.20              #
#                       #
# Day 11, Part 2        #
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

    #y = 1
    #x = 0
    #print(neighbor_count(origMap, x, y))
    print()

    for i in range(2000):
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
                        tempMap[row + 1][column + 1] = "#"
                #if the seat is occupied...
                elif origMap[row + 1][column + 1] == "#":
                    #print(" --> seat is occupied")
                    #check if it has 4 or more adjacent neighbors
                    nb_count = neighbor_count(origMap, row, column)
                    #print("Neighbor_Count = {}".format(nb_count))
                    if nb_count >= 5:
                        #print("Remove the person from this seat.")
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


def neighbor_count(mapdata, me_y, me_x):
    #convert to global map (with borders)
    maxW = len(mapdata[0])-1
    maxH = len(mapdata)-1
    me_X = me_x + 1
    me_Y = me_y + 1
    people_count = 0
    a=b=c=d=f=g=h=i="."
    #above ppl count:
    #11.2 change this to check all directions (not just adjacent cells)
    #top left
    exit = 0
    new_x = me_X
    new_y = me_Y
    while exit == 0:
        new_x -= 1
        new_y -= 1
        if new_x == 0 or new_y == 0:
            exit = 1
        else:
            if mapdata[new_y][new_x] == "#":
                a = "#"
                people_count += 1
                exit = 1
            elif mapdata[new_y][new_x] == "L":
                a = "L"
                exit = 1
    #print("A: {}".format(people_count))
    #top center
    exit = 0
    new_x = me_X
    new_y = me_Y
    while exit == 0:
        new_y -= 1
        if new_y == 0:
            exit = 1
        else:
            if mapdata[new_y][new_x] == "#":
                b = "#"
                people_count += 1
                exit = 1
            elif mapdata[new_y][new_x] == "L":
                b = "L"
                exit = 1
    #print("B: {}".format(people_count))
    #top right
    exit = 0
    new_x = me_X
    new_y = me_Y
    while exit == 0:
        new_x += 1
        new_y -= 1
        if new_x == maxW or new_y == 0:
            exit = 1
        else:
            if mapdata[new_y][new_x] == "#":
                c = "#"
                people_count += 1
                exit = 1
            elif mapdata[new_y][new_x] == "L":
                c = "L"
                exit = 1
    #print("C: {}".format(people_count))
    #straight left
    exit = 0
    new_x = me_X
    new_y = me_Y
    while exit == 0:
        new_x -= 1
        if new_x == 0:
            exit = 1
        else:
            if mapdata[new_y][new_x] == "#":
                d = "#"
                people_count += 1
                exit = 1
            elif mapdata[new_y][new_x] == "L":
                d = "L"
                exit = 1
    #print("D: {}".format(people_count))
    #straight right
    exit = 0
    new_x = me_X
    new_y = me_Y
    while exit == 0:
        new_x += 1
        if new_x == maxW:
            exit = 1
        else:
            if mapdata[new_y][new_x] == "#":
                f = "#"
                people_count += 1
                exit = 1
            elif mapdata[new_y][new_x] == "L":
                f = "L"
                exit = 1
    #print("F: {}".format(people_count))
    #bottom left
    exit = 0
    new_x = me_X
    new_y = me_Y
    while exit == 0:
        new_x -= 1
        new_y += 1
        if new_x == 0 or new_y == maxH:
            exit = 1
        else:
            if mapdata[new_y][new_x] == "#":
                g = "#"
                people_count += 1
                exit = 1
            elif mapdata[new_y][new_x] == "L":
                g = "L"
                exit = 1
    #print("G: {}".format(people_count))
    #bottom center
    exit = 0
    new_x = me_X
    new_y = me_Y
    while exit == 0:
        new_y += 1
        if new_y == maxH:
            exit = 1
        else:
            if mapdata[new_y][new_x] == "#":
                h = "#"
                people_count += 1
                exit = 1
            elif mapdata[new_y][new_x] == "L":
                h = "L"
                exit = 1
    #print("H: {}".format(people_count))
    #bottom right
    exit = 0
    new_x = me_X
    new_y = me_Y
    while exit == 0:
        new_x += 1
        new_y += 1
        if new_x == maxW or new_y == maxH:
            exit = 1
        else:
            if mapdata[new_y][new_x] == "#":
                i = "#"
                people_count += 1
                exit = 1
            elif mapdata[new_y][new_x] == "L":
                i = "L"
                exit = 1

    #print("{} {} {}\n{} X {}\n{} {} {}".format(a,b,c,d,f,g,h,i))

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