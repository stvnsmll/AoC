#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 08.12.21              #
#                       #
# Day 08, Part 1        #
#########################

from datetime import datetime


def aoc2021_08_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 8, Part 1\n~~ running as a test ~~")

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
    signals = {}#[signal number][0=signal paterns, 1=output values][value for each]
    stepper = 0
    for line in input_data:
        parts = line.split(" | ")
        signals[stepper] = parts[0].split(" "), parts[1].split(" ")
        stepper += 1
    
    #for i in signals:
    #    print(signals[i])
    
    #print("\n\n")

    print("check digits in output value")
    lenght_valid = [2, 3, 4, 7]
    valid_digit_count = 0
    for signal in signals:
        for output in signals[signal][1]:
            if len(output) in lenght_valid:
                valid_digit_count += 1

    answer = valid_digit_count
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_08_1("input.txt")