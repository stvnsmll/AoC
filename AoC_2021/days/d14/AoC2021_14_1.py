#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 22.12.21              #
#                       #
# Day 14, Part 1        #
#########################

from datetime import datetime


def aoc2021_14_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 14, Part 1\n~~ running as a test ~~")

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
    polymer_template = input_data[0]
    insertion_rules_list = list(x.split(" -> ") for x in input_data[2:])
    print(f"\nPolymer Template: {polymer_template}\n")
    insertion_rules = {}
    for rule in insertion_rules_list:
        insertion_rules[rule[0]] = rule[1]
    print("Rules:")
    for rule in insertion_rules:
        print(f"  {rule} makes -> {insertion_rules[rule]}")
    
    print()
    polymer = list(polymer_template)
    print(polymer_template)
    #polymer loop
    for loop in range(10):
        new_polymer = [polymer[0]]
        for i in range(len(polymer) - 1):
            pair = "".join(polymer[i:i + 2])
            new_char = insertion_rules[pair]
            #print(pair)
            #print(new_char)
            new_polymer += [new_char, polymer[i + 1]]
            #print(new_polymer)
            #print()
        polymer = new_polymer.copy()
        #print("".join(new_polymer))

    print()
    print(len(polymer))

    full_list = []
    for rule in insertion_rules:
        full_list += list(rule)
    type_dict = dict.fromkeys(full_list)
    for pType in type_dict:
        type_dict[pType] = 0
    for element in polymer:
        type_dict[element] += 1
    print(type_dict)
    print(max(type_dict.values()))
    print(min(type_dict.values()))

    answer = max(type_dict.values()) - min(type_dict.values())
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_14_1("input.txt")