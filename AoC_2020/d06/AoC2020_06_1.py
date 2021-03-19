#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 06.12.20              #
#                       #
# Day 6, Part 1         #
#########################

import csv

def main(test):
    if test == 't':
        testing = 1
        input_file = "./d06/customsans_testing.txt"
    else:
        testing = 0
        input_file = "./d06/customsans.txt"

    # Using readline()
    customsfile_file = open(input_file, 'r')
    rowcount = 0
    familycount = 0
    familymembercount = 0
    customs_responses = []
    tmpstring = ""
    master_yes_count = 0

    while True:
        rowcount += 1

        # Get next line from file
        line = customsfile_file.readline()

        # if line is empty
        # end of file is reached
        if not line:
            master_yes_count += processFamilyData(tmpstring, familymembercount)
            familymembercount += 1
            break

        if line == "\n":
            master_yes_count += processFamilyData(tmpstring, familymembercount)
            tmpstring = ""
            familycount += 1
            familymembercount = 0
        else:
            tmpstring += (line.strip())
            familymembercount += 1
            # print("Passport #{}: {}".format((psportcount + 1), line.strip()))

    customsfile_file.close()

    print("\nCount of families:", (familycount + 1))
    print("Total Rows:", rowcount)
    print("\nTotal Number of Yes Responses:", master_yes_count)

    print('\n\ndone')
    return master_yes_count

def processFamilyData(customsresponses, familymembercount):
    # print("Customs String: {}".format(customsresponses))
    unique_char_count = len(set(customsresponses))
    # print(unique_char_count)
    # print(familymembercount)
    # print(" --end of customs form--")
    return unique_char_count


if __name__ == "__main__":
    main("r")