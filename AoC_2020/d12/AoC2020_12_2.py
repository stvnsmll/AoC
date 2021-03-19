#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 12.12.20              #
#                       #
# Day 12, Part 2        #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d12/navinstructions_testing.txt"
    else:
        testing = 0
        input_file = "./d12/navinstructions.txt"

    # Using readline()
    instructions_file = open(input_file, 'r')
    rowcount = 0
    instr_data = []

    while True:
        # Get next line from file
        line = instructions_file.readline().strip()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        instr_data.append(line)
        rowcount += 1

    instructions_file.close()

    answer = 0
    #print(instr_data)
    instructions = []
    for i in instr_data:
        instructions.append([i[:1], i[1:]])

    #print(instructions)
    print()

    step_counter = 0
    myPos_x = 0
    myPos_y = 0
    wp_offset_x = 10
    wp_offset_y = -1
    myDir = "E"#start facing east

    cardinal = ['N', 'E', 'S', 'W']
    turn = "LR"

    for inst in instructions:
        step_counter += 1
        action = inst[0]
        value = int(inst[1])
        if action == "F":# move to the waypoint {{ value }} times
            for i in range(value):
                myPos_x += wp_offset_x
                myPos_y += wp_offset_y
        elif action in turn:
            turn_count = int(value / 90)

            if action == "L":
                factorA = -1
                factorB = 1
            else:
                factorA = 1
                factorB = -1

            for i in range(turn_count):
                tmp_x = wp_offset_x
                tmp_y = wp_offset_y
                wp_offset_x = factorB * tmp_y
                wp_offset_y = factorA * tmp_x

        else:
            #should be a cardinal movement
            direction = action
            distance = value
            if direction == 'N':
                wp_offset_y -= distance
            elif direction == 'E':
                wp_offset_x += distance
            elif direction == 'S':
                wp_offset_y += distance
            else: #'W'
                wp_offset_x -= distance
        #print("Mid Position {}:\n  new X is {}\n  new Y is {}".format(step_counter, myPos_x, myPos_y))

    print("Final Position:\n  new X is {}\n  new Y is {}".format(myPos_x, myPos_y))

    manhattan = abs(myPos_x) + abs(myPos_y)

    answer = manhattan

    print("\nManhattan Distance = {}".format(manhattan))

    print('\n\ndone')
    return answer


def getQuad(wp_x, wp_y):
    # 3  2
    # 4  1
    if wp_x >= 0:
        if wp_y >= 0:
            return 1
        else:
            return 2
    else:
        if wp_y >= 0:
            return 4
        else:
            return 3


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