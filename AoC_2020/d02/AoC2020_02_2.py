#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 02.12.20              #
#                       #
# Day 2, Part 2         #
#########################

import csv

def main(test):
    if test == 't':
        testing = 1
        input_file = "./d02/passwords_testing.csv"
    else:
        testing = 0
        input_file = "./d02/passwords.csv"

    pwreader = csv.DictReader(open(input_file))

    passwords = []
    for line in pwreader:
        passwords.append(line)

    validCount = 0
    PWcount = 0

    for row in passwords:
        PWcount += 1
        matchCount = 0

        # Parse the input
        entry = row['data'].split(': ')
        password = entry[1]
        PWrule = entry[0]
        split1 = PWrule.split()
        char = split1[1]
        split2 = split1[0].split('-')
        pos1 = int(split2[0])
        pos2 = int(split2[1])

        # print(PWrule, password)

        # Check each position (-1 to take care of the 1 indexing instead of 0)
        if password[(pos1 - 1)] == char:
            matchCount += 1
        if password[(pos2 - 1)] == char:
            matchCount += 1
        if matchCount == 1:
            # this was a valid password
            validCount += 1

    print("\nNumber of valid passwords:", validCount)
    print("  out of", PWcount, "entries.")

    print('\n\ndone')
    return validCount


if __name__ == "__main__":
    main("r")