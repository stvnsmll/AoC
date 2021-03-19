#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 02.12.20              #
#                       #
# Day 2, Part 1         #
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

        # Parse the input
        entry = row['data'].split(': ')
        password = entry[1]
        PWrule = entry[0]
        split1 = PWrule.split()
        char = split1[1]
        split2 = split1[0].split('-')
        minChar = int(split2[0])
        maxChar = int(split2[1])

        # print(PWrule, password)

        charcount = password.count(char)
        if minChar <= charcount <= maxChar:
            validCount += 1
            # print("A VALID PASSWORD!")
        else:
            pass
            # print("not a valid password")

    print("\nNumber of valid passwords:", validCount)
    print("  out of", PWcount, "entries.")

    print('\n\ndone')
    return validCount


if __name__ == "__main__":
    main("r")