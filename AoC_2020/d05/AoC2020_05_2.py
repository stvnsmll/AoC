#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 05.12.20              #
#                       #
# Day 5, Part 2         #
#########################

def main(test):
    if test == 't':
        testing = 1
        input_file = "./d05/seatplan_testing.txt"
    else:
        testing = 0
        input_file = "./d05/seatplan.txt"

    # Using readline()
    seatplan_file = open(input_file, 'r')
    seatcount = 0
    maxseatID = 0

    airplaneseatmap = [ [ 0 for row in range( 8 ) ]
                            for col in range( 128 ) ]

    while True:
        # Get next line from file
        seatdata = seatplan_file.readline().strip()

        # if line is empty end of file is reached
        if not seatdata:
            break

        # print(seatdata)
        seatrow = seatdata[:-3]
        seatcol = seatdata[-3:]
        seatcoord = getseatcoord(seatrow, seatcol)
        seat_row = int(seatcoord[0] - 1)
        seat_col = int(seatcoord[1] - 1)
        seatID = int(seatcoord[2])
        if testing == 1:
            print("Row Info: " + str(seat_row) + ", Col Info: " + str(seat_col))
        airplaneseatmap[seat_row][seat_col] = seatID

        seatcount += 1

    seatplan_file.close()


    # print("\nHighest Seat ID:", maxseatID)
    print("\nTotal Seat Count:", seatcount)

    # Print the airplane map:

    i = 1
    print("row   1  2  3  4  5  6  7  8")
    for row in airplaneseatmap:
        print(str(i).zfill(3), end = ": ")

        print(row)
        i += 1


    emptyseatcount = 0
    answer = 0
    for row in airplaneseatmap:
        #print(row)
        for i in range(6):
            if row[(i + 1)] == 0:
                emptyseatcount += 1
                if row[i] + 2 == row[(i + 2)]:
                    answer = row[i] + 1
                    break
        if answer != 0:
            break

    print(str(emptyseatcount) + " empty seats...")
    print("\nYour seat ID:", answer)

    print('\n\ndone')
    return answer



def getseatcoord(row, col):
    minrow = 0
    maxrow = 128
    rowmid = 0
    for code in row:
        # print("Min: " + str(int(minrow)) + ", Max: " + str(int(maxrow)))
        rowmid = (minrow + maxrow) / 2
        # print("  Mid: " + str(int(rowmid)))
        # print(code)
        if code == "F":
            maxrow = rowmid
        else:
            minrow = rowmid
    if row[:-1] == "F":
        row = maxrow
    else:
        row = minrow
    # print(int(row))

    mincol = 0
    maxcol = 8
    colmid = 0
    for code in col:
        # print(code)
        colmid = (mincol + maxcol) / 2
        # print(colmid)
        if code == "L":
            maxcol = colmid
        else:
            mincol = colmid
    col = (mincol + maxcol) / 2

    seatID = (row * 8) + col
    seatCoord = [int(row), int(col), seatID]
    return seatCoord



if __name__ == "__main__":
    main("r")