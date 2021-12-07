#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 07.12.21              #
#                       #
# Day 07, Part 2        #
#########################

from datetime import datetime
import statistics


def aoc2021_07_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 7, Part 2\n~~ running as a test ~~")

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
    print(f"Median: {median}")
    #start at the median, then adjust
    #  add one and subtract one. which ever has less fuel spent, start checking one by
    #  one in that direction
    median_fuel = fuel_for_all(median, positions)
    up_fuel = fuel_for_all((median + 1), positions)
    down_fuel = fuel_for_all((median - 1), positions)
    answer = 0

    check_distance = 1000
    if up_fuel < median_fuel:
        #answer is upwards!
        tmp_min_fuel = median_fuel
        for i in range((median + 1), (median + check_distance), 1):
            new_fuel = fuel_for_all(i, positions)
            if new_fuel < tmp_min_fuel:
                tmp_min_fuel = new_fuel
            else:
                answer = tmp_min_fuel
        if answer == 0:
            print(f"answer not found, increase check distance (max checked: {(median + check_distance)})")
    elif down_fuel < median_fuel:
        #answer is downwards!
        tmp_min_fuel = median_fuel
        for i in range((median - 1), (median - check_distance), -1):
            new_fuel = fuel_for_all(i, positions)
            if new_fuel < tmp_min_fuel:
                tmp_min_fuel = new_fuel
            else:
                answer = tmp_min_fuel
                break
        if answer == 0:
            print(f"answer not found, increase check distance (max checked: {(median - check_distance)})")
    else:
        #median is the answer!
        answer = median_fuel
        

    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer

def fuel_for_all(target, positions):
    fuel_spent = 0
    for crab in positions:
        distance = abs(crab - target)
        fuel = (distance * (distance + 1)) / 2
        fuel_spent += fuel
    return fuel_spent


if __name__ == "__main__":
   aoc2021_07_2("input.txt")