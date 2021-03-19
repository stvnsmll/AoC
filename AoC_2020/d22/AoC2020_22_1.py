#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 29.12.20              #
#                       #
# Day 22, Part 1        #
#########################


def main(test):

    if test == 't':
        testing = 1
        input_file = "./d22/startingHands_testing.txt"
    else:
        testing = 0
        input_file = "./d22/startingHands.txt"

    # Using readline()
    startingHands_file = open(input_file, 'r')
    hands_data = []

    while True:
        # Get next line from file
        line = startingHands_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        hands_data.append(line.strip())

    startingHands_file.close()

    #for i in hands_data:
    #    print(i)
    #print(hands_data)

    p1_hand = []
    p2_hand = []
    hand = 1
    for i in hands_data:
        if hand == 1:
            toadd = p1_hand
        else:
            toadd = p2_hand
        if i == "":
            hand = 2
        elif i.isnumeric():
            toadd.append(int(i))
        else:
            pass

    print("Starting Hands:")
    print(p1_hand)
    print(p2_hand)

    exit = 0
    turn = 0

    while exit == 0:
        if (len(p1_hand) == 0) or (len(p2_hand) == 0):
            print("Game Over")
            print(f"Turn Count: {turn}")
            exit = 1
        else:
            turn += 1
            p1 = p1_hand[0]
            p2 = p2_hand[0]
            #get winner
            winner = p1_hand
            if p1 > p2:
                p1_hand.append(p1)
                p1_hand.append(p2)
            else:
                p2_hand.append(p2)
                p2_hand.append(p1)
            del p1_hand[0]
            del p2_hand[0]
            #print()
            #print(p1_hand)
            #print(p2_hand)

    #find winner
    winner = p1_hand
    if len(p2_hand) > len(p1_hand):
        winner = p2_hand

    print(f"\nWinning Hand: {winner}")

    #calculate the answer
    answer = 0
    for i in range(len(winner)):
        multiplyer = len(winner) - i
        answer += (winner[i] * multiplyer)


    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


class Tile:
    def __init__(self, refNo, inputdata):
        tile_number = inputdata[0].split()[1].split(":")[0]

        tile_data = []
        tile_data_1s0s = []
        for i in range(10):
            tile_data.append(inputdata[i + 1])
            digits = inputdata[i + 1].replace(".","0").replace("#","1")
            tile_data_1s0s.append(digits)
            #print(inputdata[i + 1])

        top_int = int(tile_data_1s0s[0], 2)
        pot_int = int(tile_data_1s0s[0][::-1], 2)
        bottom_int = int(tile_data_1s0s[9], 2)
        mottob_int = int(tile_data_1s0s[9][::-1], 2)
        left_list = []
        for i in range(10):
            left_list.append(tile_data_1s0s[i][0])
        left_str = listToString(left_list)
        left_int = int(left_str, 2)
        tfel_int = int(left_str[::-1], 2)
        right_list = []
        for i in range(10):
            right_list.append(tile_data_1s0s[i][9])
        right_str = listToString(right_list)
        right_int = int(right_str, 2)
        thgir_int = int(right_str[::-1], 2)

        border_vals = [top_int, pot_int, bottom_int, mottob_int, left_int, tfel_int, right_int, thgir_int]

        self.number = tile_number
        self.refNo = refNo
        self.mydata = tile_data
        self.mydatadigits = tile_data_1s0s
        self.allborders = border_vals

    def printMap(self, var):
        if var == 1:
            maptoprint = self.mydata
        elif var == 0:
            maptoprint = self.mydatadigits
        else:
            print("Input error, must be a 1 or a 0")
            return 1
        for i in maptoprint:
            print(i)
        return 0


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1



if __name__ == "__main__":
    main("r")