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
    from datetime import datetime
    startTime = datetime.now()

    if test == 't':
        tmp_starting = 1
        input_file = "./d23/startingCups_testing.txt"
    else:
        tmp_starting = 0
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

    global cup_dict
    cup_dict = {}

    start_pos = 1
    #put in the first cup:
    #  defining a class instance of a cup: Cup(myNumber, myPosition)
    cup_dict[cup_list[0]] = Cup(cup_list[0], 0)
    point_to_first = cup_list[0]
    prior_val = cup_list[0]
    cup_list.pop(0)
    for i in cup_list:
        cup_dict[i] = Cup(i, start_pos)
        cup_dict[prior_val].myNext = i
        prior_val = i
        start_pos += 1

    print(prior_val)
    print(start_pos)

    #add more cups in numerical order:
    max_in_cup_list = max(cup_list)
    print(f"Max in cup_list = {max_in_cup_list}")
    add_to_number = 1000000
    for i in range(add_to_number - max_in_cup_list):
        j = i + max_in_cup_list + 1
        #print(j)
        cup_dict[j] = Cup(j, start_pos)
        cup_dict[prior_val].myNext = j
        prior_val = j
        start_pos += 1


    #set the last cup's "next" to point to the first one.
    cup_dict[prior_val].myNext = point_to_first
    #set the first cup's predecessor to the point to the last cup.
    #cup_dict[point_to_first].myPred = prior_val

    #print the data:
    #for i in cup_dict:
    #    cup_dict[i].printMe()

    #NEXT:
    # start playing the game!
    max_digit = 1000000

    #tmp_start some operations
    start_digit = point_to_first

    #print(f"Third after start ({start_digit}) is cup number:")
    tmp_start = cup_dict[start_digit].getThirdAhead()
    #print(tmp_start)
    cup_pull_list = []
    cup_pull_list.append(cup_dict[start_digit].myNext)
    cup_pull_list.append(cup_dict[cup_pull_list[-1]].myNext)
    cup_pull_list.append(cup_dict[cup_pull_list[-1]].myNext)
    #mend the list after the three cups have been pulled out
    cup_dict[start_digit].myNext = cup_dict[start_digit].getThirdAhead()
    #print(cup_pull_list)
    destination = (start_digit - 1)
    #print(f"Destination: {destination}")
    #insert the three cups into the destination location
    tmp_split_end = cup_dict[destination].myNext
    cup_dict[destination].myNext = cup_pull_list[0]
    cup_dict[cup_pull_list[2]].myNext = tmp_split_end
    #print_list(cup_dict, 3)
    print()


    for i in range(9999999):
        if i%1000000 == 0:
            print(f"Iteration #{i}")
        start_digit = tmp_start
        #print(f"Third after start ({start_digit}) is cup number:")
        tmp_start = cup_dict[start_digit].getThirdAhead()
        #print(tmp_start)
        cup_pull_list = []
        cup_pull_list.append(cup_dict[start_digit].myNext)
        cup_pull_list.append(cup_dict[cup_pull_list[-1]].myNext)
        cup_pull_list.append(cup_dict[cup_pull_list[-1]].myNext)
        #print(cup_pull_list)
        #mend the list after the three cups have been pulled out
        cup_dict[start_digit].myNext = cup_dict[start_digit].getThirdAhead()
        destination = (start_digit - 1)
        if destination == 0:
            destination = max_digit
        while destination in cup_pull_list:
            destination -= 1
            if destination == 0:
                destination = max_digit
        #print(f"Destination: {destination}")
        #insert the three cups into the destination location
        tmp_split_end = cup_dict[destination].myNext
        cup_dict[destination].myNext = cup_pull_list[0]
        cup_dict[cup_pull_list[2]].myNext = tmp_split_end
        #print_list(cup_dict, 3)
        #print()


    #print("\n\n\n")
    #cup_list = print_list(cup_dict, 1)
    #print(listToString(cup_list))

    first_after = cup_dict[1].myNext
    second_after = cup_dict[first_after].myNext

    print(f"Two digits = {first_after} and {second_after}")


    answer = int(first_after * second_after)


    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')

    print("Runtime Duration: ", end = "")
    print(datetime.now() - startTime)
    return answer



class Cup:
    def __init__(self, myNumber, myPosition):
        self.myNumber = myNumber
        self.myPosition = myPosition
        #self.myPred = myPred
        self.myNext = 1234567890

    def getThirdAhead(self):
        #if self.myNext == "":
        #    print("error, no next found")
        #    return 1
        thirdAhead = cup_dict[cup_dict[cup_dict[self.myNext].myNext].myNext].myNext
        return thirdAhead

    def printMe(self):
        print(f"Number: {self.myNumber}")
        print(f"My position: {self.myPosition}")
        #print(f"My predecessor: {self.myPred}")
        print(f"My next: {self.myNext}")
        print()


def  print_list(printDict, startVal):
    #create list
    printList = []
    printList.append(startVal)
    for i in range(len(printDict) - 1):
        printList.append(printDict[printList[-1]].myNext)
    print(printList)

    printList.pop(0)
    return printList



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