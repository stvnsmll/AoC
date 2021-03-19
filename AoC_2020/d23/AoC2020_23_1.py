#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 31.12.20              #
#                       #
# Day 23, Part 1        #
#########################


def main(test):

    if test == 't':
        testing = 1
        input_file = "./d23/startingCups_testing.txt"
    else:
        testing = 0
        input_file = "./d23/startingCups.txt"

    # Using readline()
    startingCups_file = open(input_file, 'r')
    cup_data = []

    while True:
        # Get next line from file
        line = startingCups_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        cup_data.append(line.strip())

    startingCups_file.close()


    #print(list(cup_data[0]))
    cup_list = list(map(int, list(cup_data[0])))
    print(cup_list)

    start_cup = 0
    list_len = len(cup_list)

    for i in range(100):
        print(cup_list)
        start_val = cup_list[start_cup]
        next_cup = start_cup + 1
        if next_cup > list_len:
            next_cup = 0
        print(f"Start Cup Value: {start_val}")
        next_three = cup_list[(start_cup + 1):(start_cup + 4)]
        print(next_three)
        #remove these "next_three" from the circle
        new_list = cup_list.copy()
        new_list.pop(start_cup + 1)
        new_list.pop(start_cup + 1)
        new_list.pop(start_cup + 1)
        print(f"New list {new_list}")
        #select destination cup
        max_in_remaining = max(new_list)
        targetVal = start_val - 1
        exit = 0
        while exit == 0:
            #print(f"Looking for value: {targetVal}")
            if targetVal < 0:
                targetVal = max_in_remaining
            for j in new_list:
                if j == targetVal:
                    dest_val = j
                    exit = 1
            targetVal -= 1
        print(f"Destination Value: {dest_val}")
        dest_pos = new_list.index(dest_val)
        print(f"Destination Location: {dest_pos}")
        final_list = new_list[:(dest_pos + 1)] + next_three + new_list[(dest_pos + 1):]
        print(f"Final List: {final_list}")

        #setup for the next loop (cycle start of list to the end of the list)
        start_val = new_list[start_cup + 1]
        start_cup = final_list.index(start_val) - 1
        digit_to_move = final_list[0]
        final_list.pop(0)
        final_list.append(digit_to_move)
        cup_list = final_list
        print()

    # Get value 1 at the start of the list keep rotating it
    for i in range(len(cup_list)):
        print(i)
        first_val = cup_list[0]
        cup_list.pop(0)
        if first_val == 1:
            break
        else:
            cup_list.append(first_val)
            print(cup_list)

    print(listToString(cup_list))
    answer = int(listToString(cup_list))


    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


class Cup:
    def __init__(self, myNumber, myPosition):
        self.myNumber = myNumber
        self.myPosition = myPosition
        self.myNext = ""

    def getThirdAhead(self):
        if self.myNext == "":
            print("error, no next found")
            return 1
        thirdAhead = self.myNext.myNext.myNext
        return thirdAhead


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += str(ele)
    # return string
    return str1





if __name__ == "__main__":
    main("r")