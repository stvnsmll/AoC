#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 03.12.20              #
#                       #
# Day 3, Part 2         #
#########################

import csv

def main(test):
    if test == 't':
        testing = 1
        input_file = "./d03/slopemap_testing.csv"
    else:
        testing = 0
        input_file = "./d03/slopemap.csv"

    mapreader = csv.DictReader(open(input_file))

    slopemap = []
    for line in mapreader:
        slopemap.append(list(line['data']))

    # print(slopemap[1][0])

    # Selected Sledder Slope
    dx = 1
    dy = 1
    treehitcount1 = counthits(slopemap, dx, dy)

    dx = 3
    dy = 1
    treehitcount2 = counthits(slopemap, dx, dy)

    dx = 5
    dy = 1
    treehitcount3 = counthits(slopemap, dx, dy)

    dx = 7
    dy = 1
    treehitcount4 = counthits(slopemap, dx, dy)

    dx = 1
    dy = 2
    treehitcount5 = counthits(slopemap, dx, dy)


    total = treehitcount1 * treehitcount2 * treehitcount3 * treehitcount4 * treehitcount5



    print("Number of trees hit:", total)
    return total


def counthits(slopemap, dx, dy):
    # get dimensions
    height = len(slopemap)
    width = len(slopemap[0])
    # print(height, 'x', width)

    # current sledder location
    me_x = 0
    me_y = 0

    impactcount = 0
    totalcount = 0

    # Traverse the slope map, count trees that you hit
    while me_y < (height - 1):
        # Starting sled location
        # print("Sled starts at:", me_x, ",", me_y)

        # move the sled
        me_y += dy
        me_x = (me_x + dx) % width
        # print("Sled position:", me_x, ",", me_y)

        # check for tree impact
        # print(slopemap[me_y][me_x])
        if slopemap[me_y][me_x] == "#":
            impactcount += 1

        totalcount += 1

    # Print results
    # print()
    #print("Number of trees hit:", impactcount)
    #print("Total number of nodes:", totalcount)

    #print('\n\ndone')
    return impactcount


if __name__ == "__main__":
    main("r")