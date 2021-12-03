#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 03.12.21              #
#                       #
# Day 03, Part 1        #
#########################

from datetime import datetime


def aoc2021_03_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 03, Part 1\n~~ running as a test ~~")

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


    answer = gamma_rate_int * epsilon_rate_int
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_03_1("input.txt")