#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 05.12.20              #
#                       #
# Day 5, Part 1         #
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

    while True:
        # Get next line from file
        seatdata = seatplan_file.readline().strip()

        # if line is empty end of file is reached
        if not seatdata:
            break

        # print(seatdata)
        seatrow = seatdata[:-3]
        seatcol = seatdata[-3:]
        seatID = getseatID(seatrow, seatcol)
        # print("Row Info: " + seatrow + ", Col Info: " + seatcol)
        # print("  Seat ID: " + str(seatID) + "\n")
        if seatID > maxseatID:
            maxseatID = seatID

        seatcount += 1

    seatplan_file.close()


    print("\nHighest Seat ID:", maxseatID)
    print("Total Seat Count:", seatcount)

    print('\n\ndone')
    return maxseatID

def getseatID(row, col):
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

    return int(seatID)



if __name__ == "__main__":
    main("r")