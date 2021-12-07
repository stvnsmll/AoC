#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 07.12.21              #
#                       #
# Day 07, Part 1        #
#########################

from datetime import datetime
import statistics


def aoc2021_07_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 7, Part 1\n~~ running as a test ~~")

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

    positions = [int(x) for x in input_data[0].split(",")]
    #print(positions)

    #find the median:
    median = int(statistics.median(positions))
    check_range = 3
    check_step = 1
    fuel_check_dict = {}
    for fuel_check in range((median - check_range),(median + check_range + 1), check_step):
        fuel_check_dict[fuel_check] = fuel_for_all(fuel_check, positions)
    
    for i in fuel_check_dict:
        print(f"{i}: {fuel_check_dict[i]}")
    
    
    answer = fuel_for_all(median, positions)
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer

def fuel_for_all(target, positions):
    fuel_spent = 0
    for crab in positions:
        fuel_spent += abs(crab - target)
    return fuel_spent


if __name__ == "__main__":
   aoc2021_07_1("input.txt")