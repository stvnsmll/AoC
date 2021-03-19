#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 04.12.20              #
#                       #
# Day 4, Part 1         #
#########################

import csv

def main(test):
    if test == 't':
        testing = 1
        input_file = "./d04/psportbash_testing.txt"
    else:
        testing = 0
        input_file = "./d04/psportbash.txt"

    # Using readline()
    psportbash_file = open(input_file, 'r')
    rowcount = 0
    psportcount = 0
    passports = []
    tmpstring = ""
    validpassportcount = 0

    while True:
        rowcount += 1

        # Get next line from file
        line = psportbash_file.readline()

        # if line is empty
        # end of file is reached
        if not line:
            validpassportcount += processPassportData(tmpstring)
            break

        if line == "\n":
            validpassportcount += processPassportData(tmpstring)
            tmpstring = ""
            psportcount += 1
        else:
            tmpstring += (line.strip() + " ")
            # print("Passport #{}: {}".format((psportcount + 1), line.strip()))

    psportbash_file.close()

    print("\nCount of passports:", (psportcount + 1))
    print("Total Rows:", rowcount)
    print("\nValid Passports:", validpassportcount)

    print('\n\ndone')
    return validpassportcount

def processPassportData(passportdata):
    #print("Passport: {}".format(passportdata))
    fieldcount = 0
    validpassport = 0
    for i in passportdata:
        if i == ':':
            fieldcount += 1
    #print(fieldcount)
    if 'cid:' in passportdata:
        #print("has a country code")
        fieldcount -= 1
    else:
        #print("no country code")
        pass
    #print(fieldcount)
    if fieldcount == 7:
        validpassport = 1
    #print(" --end of passport--")
    return validpassport


if __name__ == "__main__":
    main("r")