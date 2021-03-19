#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 01.12.20              #
#                       #
# Day 1, Part 2.        #
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
    k = 0
    exit = 0
    product = 0

    for row in expensereport:
        i = int(row['data'])
        #print('i =',i)
        for col in expensereport:
            j = int(col['data'])
            #print('  j =',j)
            total1 = i + j
            if total1 < 2020:
                for height in expensereport:
                    k = int(height['data'])
                    total2 = i + j + k
                    #print('    k =', k, '  total2:', total2)
                    if total2 == 2020:
                        print('i =', i, 'j =', j, 'k = ',k , ' total:', total2)
                        print('found it!!')
                        product = i * j * k
                        print('part 2 answer: ', product)
                        exit = 1
                        break
            if exit == 1:
                break
        if exit == 1:
            break

    print('done')
    return product


if __name__ == "__main__":
    main("r")