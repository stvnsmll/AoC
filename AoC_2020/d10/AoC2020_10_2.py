#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 10.12.20              #
#                       #
# Day 10, Part 2        #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d10/adapters_testing.txt"
    else:
        testing = 0
        input_file = "./d10/adapters.txt"

    # Using readline()
    adapters_file = open(input_file, 'r')
    rowcount = 0
    adapters_data = [0]

    while True:
        # Get next line from file
        line = adapters_file.readline().strip()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        adapters_data.append(int(line))
        rowcount += 1

    #print("\n\n")
    max_adapter = max(adapters_data)
    #print(max_adapter)
    #add your device's final joltage to the end
    adapters_data.append((max_adapter + 3))

    adapters_file.close()

    code_length = rowcount
    answer = 0
    #print()
    #print(adapters_data)
    adapters_data.sort()
    print("Master List: ", end="")
    print(adapters_data)
    print()

    global valid_lists
    valid_lists = []

    #valid_count = count_valid(adapters_data, 0)

    check_max_delta(adapters_data)

    #list.remove(val) removes the value from the list
    #del list[pos] removes the value at postion "pos" from the list

    print("\n\n")
    #valid_lists.sort(reverse=True, key=lenFunc)
    for i in range(len(valid_lists)):
        print("Solution #{}: {}".format((i + 1), valid_lists[i]))

    answer = len(valid_lists)
    print("\nThe answer is {}.".format(answer))
    print()
    print("\nTotal Input Count:", rowcount)

    print('\n\ndone')
    return answer


def count_valid(listtocount, startfrom):
    #print("List to check then count: {}".format(listtocount))
    #if len(listtocount) == 2:
    #    return 0
    #check if the list (len > 2) is a valid per the checker
    if check_max_delta(listtocount) == 1:
        #print("      is a valid list  ----^")
        if listtocount not in valid_lists:
            valid_lists.append(listtocount)
            #print()
        # it WAS a valid list, so keep looping deeper to see if more digits can be dropped
        for i in range(len(listtocount) - 2 - startfrom):# -2 for the start and end of the list (0 and max val) which always stay put.
            newlist = listtocount.copy()
            #print("Removing {} from the list.".format(newlist[i + 1 + startfrom]))
            del newlist[i + 1 + startfrom]
            #print("New list to check (starting at {}): {}".format(i, newlist))
            count_valid(newlist, i)
    else:
        #print("  is NOT a valid list  ----^")
        return 0

def check_max_delta(adapters_data):
    delta_data = []
    for i in range(len(adapters_data) - 1):
        #print(i)
        delta = adapters_data[i + 1] - adapters_data[i]
        if delta > 3:
            return 0
        #print("({}) a: {}, b: {}, delta: {}\n".format(i, adapters_data[i], adapters_data[i + 1], delta))
        delta_data.append(delta)
    print("                          {}".format(delta_data))
    # if never exited for delta exceeding 3, the new list is valid!
    return 1


def lenFunc(e):
  return len(e)


if __name__ == "__main__":
    main("r")