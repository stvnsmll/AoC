#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 09.12.20              #
#                       #
# Day 9, Part 1         #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d09/XMASinfo_testing.txt"
    else:
        testing = 0
        input_file = "./d09/XMASinfo.txt"

    # Using readline()
    XMASinfo_file = open(input_file, 'r')
    rowcount = 0
    XMAS_data = []

    while True:
        # Get next line from file
        line = XMASinfo_file.readline().strip()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        XMAS_data.append(int(line))
        rowcount += 1

    XMASinfo_file.close()

    preamble_length = 25 if testing == 0 else 5
    preamble = XMAS_data[:preamble_length]
    code_length = rowcount
    answer = 0
    #print(XMAS_data)

    for i in range(code_length - preamble_length):
        #print("Step Number: " + str(i))
        preamble = XMAS_data[i:(i + preamble_length)]
        digit_to_check = XMAS_data[(i + preamble_length)]
        #print(preamble, digit_to_check)
        sum_found = check_for_sums(preamble, digit_to_check)
        if not sum_found:
            answer = digit_to_check
            break

    print()


    print("\nTotal Input Count:", rowcount)

    print('\n\ndone')
    return answer

def check_for_sums(input_list, target):
    #print(" Looking for two numbers that sum up to:", str(target), end="\n In this list: ")
    #print(input_list)
    for i in range(len(input_list)):
        tmp_list = input_list.copy()
        remainder = target - input_list[i]
        del tmp_list[i]
        if remainder in tmp_list:
            #print("Sum Found wiht: " + str(input_list[i]) + " and " + str(remainder) + "\n")
            return True
    print("No Sum Found for {}!".format(target))
    #print()
    return False


if __name__ == "__main__":
    main("r")