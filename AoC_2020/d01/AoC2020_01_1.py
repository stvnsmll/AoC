#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 01.12.20              #
#                       #
# Day 1, Part 1         #
#########################

import csv

def main(test):
    if test == 't':
        testing = 1
        input_file = "./d01/expensereport_testing.csv"
    else:
        testing = 0
        input_file = "./d01/expensereport.csv"

    expensereader = csv.DictReader(open(input_file))

    expensereport = []
    for line in expensereader:
        expensereport.append(line)

    i = 0
    j = 0
    exit = 0
    product = 0

    for row in expensereport:
        i = int(row['data'])
        #print('i =',i)
        for col in expensereport:
            j = int(col['data'])
            total = i + j
            if total == 2020:
                print('i =',i,'j =',j,' total:', total)
                print('found it!!')
                product = i * j
                print('answer: ', product)
                exit = 1
                break
        if exit == 1:
            break

    print('done')
    return product


if __name__ == "__main__":
    main("r")