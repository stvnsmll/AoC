#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 15.12.21              #
#                       #
# Day 13, Part 2        #
#########################

from datetime import datetime


def aoc2021_13_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 13, Part 2\n~~ running as a test ~~")

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

    print(input_data)
    coords = []#[x,y]
    folds = []
    set_count = 0
    for i in input_data:
        if i == "":
            set_count += 1
            continue
        if set_count == 0:
            coords.append([int(x) for x in (i.split(","))])
        else: 
            folds.append(i.split(" ")[2].split("="))
    #for i in coords:
    #    print(i)
    #print(folds)
    '''
    + -------- > x
    |
    |
    |
    v y

    x-fold is vertical, y is horizontal
    '''

    for fold in folds:
        fold_dir = fold[0]
        print(fold_dir)
        fold_middle = int(fold[1])
        new_coords = []
        delete_coords = []
        if fold_dir == "y":
            # Y - fold
            for i in coords:
                #print(f"Checking coord {i} in fold {first_fold}")
                #x fold
                tmp_coord = []
                if i[1] > fold_middle:
                    #print("  Yes affected by fold!")
                    tmp_coord = [i[0], (fold_middle - (i[1] - fold_middle))]
                    #print(f"  New Coord: {tmp_coord}")
                    if tmp_coord in coords:
                        #do nothing (this is now a repeat point)
                        #print("  This is a repeat point... skip")
                        pass
                    else:
                        #print("  This is new, add it!")
                        new_coords.append(tmp_coord)
                    #this deletes any coordinates that were on the "folded" side of the map
                    delete_coords.append(i)
                else:
                    #print("  Not affected by fold.")
                    pass
                #print()
        else:
            # X - fold
            for i in coords:
                #print(f"Checking coord {i} in fold {first_fold}")
                #x fold
                tmp_coord = []
                if i[0] > fold_middle:
                    #print("  Yes affected by fold!")
                    tmp_coord = [(fold_middle - (i[0] - fold_middle)), i[1]]
                    #print(f"  New Coord: {tmp_coord}")
                    if tmp_coord in coords:
                        #do nothing (this is now a repeat point)
                        #print("  This is a repeat point... skip")
                        pass
                    else:
                        #print("  This is new, add it!")
                        new_coords.append(tmp_coord)
                    #this deletes any coordinates that were on the "folded" side of the map
                    delete_coords.append(i)
                else:
                    #print("  Not affected by fold.")
                    pass
                #print()

        #for i in coords:
        #    if i in delete_coords:
        #        coords.remove(i)
        reduced_coords = list(filter(lambda x: x not in delete_coords, coords))
        #print(reduced_coords)
        coords = reduced_coords + new_coords

    #for i in coords:
        #print(i)
    #print(len(coords))

    
    first_row = printMap(coords)
    first_row += "\n"
    
    answer = first_row
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer

def printMap(coords):
    #coord = [x,y]
    max_x = 0
    max_y = 0
    first_row = ""
    for coord in coords:
        if coord[0] > max_x:
            max_x = coord[0]
        if coord[1] > max_y:
            max_y = coord[1]
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if [x, y] in coords:
                print("#", end="")
                if y == 0:
                    first_row += "#"
            else:
                print(" ", end="")
                if y == 0:
                    first_row += "."
        print()
    return first_row
    



if __name__ == "__main__":
   aoc2021_13_2("input.txt")