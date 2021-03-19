#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 25.12.20              #
#                       #
# Day 25, Part 1        #
#########################
#import re

def main(test):
    #import re

    if test == 't':
        testing = 1
        input_file = "./d25/publicKeys_testing.txt"
    else:
        testing = 0
        input_file = "./d25/publicKeys.txt"

    # Using readline()
    key_file = open(input_file, 'r')
    rowcount = 0
    bothkeys = []

    while True:
        # Get next line from file
        line = key_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        bothkeys.append(line.strip())
        rowcount += 1

    key_file.close()

    cardKey = int(bothkeys[0])
    doorKey = int(bothkeys[1])

    subjNum = 7
    startVal = 1
    max_loop_count = 10000000

    card_loop = transform(startVal, subjNum, cardKey, max_loop_count)
    door_loop = transform(startVal, subjNum, doorKey, max_loop_count)

    print(f"Card loop count: {card_loop}")
    print(f"Door loop count: {door_loop}")

    startVal = 1
    subjNum = doorKey

    encryption_key = transform(startVal, subjNum, 595959595959595, card_loop)
    print(encryption_key)

    answer = encryption_key


    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


def transform(startVal, subjNum, publicKey, max_loop_count):
    counter = 1
    exit = 0
    while exit == 0:
        newval = startVal * subjNum
        newval = newval % 20201227
        if newval == publicKey:
            #print(counter)
            exit = 1
        else:
            startVal = newval
            counter += 1
        if counter > max_loop_count:
            counter = newval
            exit = 1

    return counter


if __name__ == "__main__":
    main("r")