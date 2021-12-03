#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 03.12.21              #
#                       #
# Day 03, Part 2        #
#########################

from datetime import datetime


def aoc2021_03_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 03, Part 2\n~~ running as a test ~~")

    startTime = datetime.now()

    # Using readline()
    input_data_file = open(filename, 'r')
    input_data = []
    while True:
        # Get next line from file
        line = input_data_file.readline()
        # if line is empty end of file is reached
        if not line:
            break
        #print(line)
        input_data.append(line.strip())
    input_data_file.close()

    #print(input_data)

    row_sumsOnes = {}
    row_sumsZeros = {}
    for char in range(len(input_data[0])):
        row_sumsOnes[char] = 0
        row_sumsZeros[char] = 0
    

    for row in range(len(input_data)):
        for char in range(len(input_data[0])):
            if int(input_data[row][char]) == 1:
                row_sumsOnes[char] += 1
            else:
                row_sumsZeros[char] += 1
    
    #print(f"Ones:  {row_sumsOnes}")
    #print(f"Zeros: {row_sumsZeros}")

    gamma_rate = []
    for key in row_sumsZeros:
        if row_sumsOnes[key] > row_sumsZeros[key]:
            gamma_rate.append("1")
        else:
            gamma_rate.append("0")

    gamma_rate_int = int(("".join(gamma_rate)), 2)
    print(gamma_rate_int)

    epsilon_rate = []
    for key in row_sumsZeros:
        if row_sumsOnes[key] < row_sumsZeros[key]:
            epsilon_rate.append("1")
        else:
            epsilon_rate.append("0")

    epsilon_rate_int = int(("".join(epsilon_rate)), 2)
    print(epsilon_rate_int)

    #PART 2 below here
    print("\nStart Part 2\n")

    oxygen_rating_list = input_data.copy()
    for column in range(len(input_data[0])):
        #print(f"Column: {column}")
        #find most common digit in all remaining items in the list
        one_count = 0
        zero_count = 0
        for row in oxygen_rating_list:
            if row[column] == "1":
                one_count += 1
            else:
                zero_count += 1
        #print(f"Ones: {one_count}, Zeros: {zero_count}")
        digit_to_keep = 1
        if zero_count > one_count:
            digit_to_keep = 0
        #print(f"Keeping the digit {digit_to_keep}")
        #make a new list that only matches the most common digit in that position
        tmp_list = []
        for row in oxygen_rating_list:
            if row[column] == str(digit_to_keep):
                tmp_list.append(row)
        #print(f"New sorted list: {tmp_list}")
        oxygen_rating_list = tmp_list.copy()
        #if length of the list is 1, that is the rating!
        #   else, loop again.
        if len(oxygen_rating_list) == 1:
            #print(f"Oxygen Rating is: {oxygen_rating_list[0]}")
            break

    oxygen_rating_dec = int((oxygen_rating_list[0]), 2)
    print(f"Oxygen rating: {oxygen_rating_dec}")

    #print("\n\n")

    co2_rating_list = input_data.copy()
    for column in range(len(input_data[0])):
        #print(f"Column: {column}")
        #find most common digit in all remaining items in the list
        one_count = 0
        zero_count = 0
        for row in co2_rating_list:
            if row[column] == "1":
                one_count += 1
            else:
                zero_count += 1
        #print(f"Ones: {one_count}, Zeros: {zero_count}")
        digit_to_keep = 0
        if one_count < zero_count:
            digit_to_keep = 1
        #print(f"Keeping the digit {digit_to_keep}")
        #make a new list that only matches the most common digit in that position
        tmp_list = []
        for row in co2_rating_list:
            if row[column] == str(digit_to_keep):
                tmp_list.append(row)
        #print(f"New sorted list: {tmp_list}")
        co2_rating_list = tmp_list.copy()
        #if length of the list is 1, that is the rating!
        #   else, loop again.
        if len(co2_rating_list) == 1:
            #print(f"Oxygen Rating is: {co2_rating_list[0]}")
            break

    co2_rating_dec = int((co2_rating_list[0]), 2)
    print(f"CO2 rating: {co2_rating_dec}")

    answer = oxygen_rating_dec * co2_rating_dec
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_03_2("input.txt")