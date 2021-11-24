#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 22.11.21              #
#                       #
# Day 06, Part 2        #
#########################

from datetime import datetime
import numpy as np

def aoc2018_06_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 06, Part 2\n~~ running as a test ~~")

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

    raw_coordinates = {}

    max_x = 0
    max_y = 0
    for i in range(len(input_data)):
        split_coords = input_data[i].split(", ")
        if int(split_coords[0]) > max_x: max_x = int(split_coords[0])
        if int(split_coords[1]) > max_y: max_y = int(split_coords[1])
        raw_coordinates[i] = [int(split_coords[0]), int(split_coords[1])]
    

    answer = solve_map(raw_coordinates, max_x, max_y)
    

    #soreted_area = dict(sorted(area_count.items(), key=lambda item: item[1]))
    #for item in soreted_area:
    #    print(f"{item}:{soreted_area[item]}")
    print(f"\nThe area of the map within min distance to enough origins is {answer}")
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer


def solve_map(coordinates, max_x, max_y):
    lessthanvalue = 10000
    if __name__ != "__main__":
        lessthanvalue = 32

    #print(f"\n{coordinates}")
    #print(f"max grid size: {max_x} x {max_y}")

    #full_map = np.zeros((max_y+2, max_x+2), int)
    #full_map.fill("-1")

    #for coord in coordinates:
    #    full_map[coordinates[coord][1], coordinates[coord][0]] = coord#coord doesn't show it's a home spot

    #printMap(full_map)

    '''
    x = 8
    y = 6
    full_map[y,x] = closest_origin([x, y], coordinates)

    printMap(full_map)
    '''

    area_count = {}
    for root in coordinates:
        area_count[root] = 0
    #print(area_count)
    low_distance_count = 0

    for row in range(max_y + 2):
        for col in range(max_x + 2):
            my_address = [col, row]
            distance_to_all = calc_all_distances(my_address, coordinates)
            if distance_to_all < lessthanvalue:
                low_distance_count += 1
            #full_map[row, col] = distance_to_all
            #if type(closest) == int:
            #    area_count[closest] += 1
    
    return low_distance_count


def calc_all_distances(my_address, origins):
    distance_to_all = 0
    for root in origins:
        distance_to_all += calc_distance(my_address, origins[root])
    return distance_to_all


def calc_distance(coord1, coord2):
    #input coords must both be two character lists consisting of [x, y] coordinates
    x_distance = abs(coord2[0] - coord1[0])
    y_distance = abs(coord2[1] - coord1[1])
    return (x_distance + y_distance)

def closest_origin(mycoord, origins):
    #origins must always be the master coordinates dictionary
    closest_dict = {}
    for root in origins:
        closest_dict[root] = calc_distance(mycoord, origins[root])
    #print(closest_dict)
    min_distance = min(closest_dict.values())
    #print(min_distance)
    if sum(x == min_distance for x in closest_dict.values()) > 1:
        #print("border!")
        return "-1"
    return min(closest_dict, key=closest_dict.get)


def printMap(map):
    print()
    for line in map:
        print("   ", end = "")
        for char in line:
            print(char, end = " ")
        print()
    print()


if __name__ == "__main__":
   aoc2018_06_2("input.txt")