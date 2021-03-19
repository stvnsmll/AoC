#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 10.12.20              #
#                       #
# Day 10, Part 1        #
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
    #print(adapters_data)

    delta_data = []

    for i in range(len(adapters_data) - 1):
        #print(i)
        delta = adapters_data[i + 1] - adapters_data[i]
        #print("a: {}, b: {}, delta: {}".format(adapters_data[i], adapters_data[i + 1], delta))
        delta_data.append(delta)
        #print()

    #print(delta_data)
    count_1 = delta_data.count(1)
    count_3 = delta_data.count(3)
    print("1-Step Count: " + str(count_1))
    print("3-Step Count: " + str(count_3))

    answer = count_1 * count_3

    print()


    print("\nTotal Input Count:", rowcount)

    print('\n\ndone')
    return answer


if __name__ == "__main__":
    main("r")