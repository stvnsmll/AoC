#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 22.12.21              #
#                       #
# Day 14, Part 2        #
#########################

from datetime import datetime


def aoc2021_14_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 14, Part 2\n~~ running as a test ~~")

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
        insertion_rules[rule[0]] = [(rule[0][0] + rule[1]), (rule[1] + rule[0][1])]
    print("Rules:")
    for rule in insertion_rules:
        print(f"  {rule} makes -> {insertion_rules[rule]}")
    
    full_list = []
    for rule in insertion_rules:
        full_list += list(rule)
    type_dict = dict.fromkeys(full_list)
    for pType in type_dict:
        type_dict[pType] = 0
    for element in polymer_template:
        type_dict[element] += 1
    print("\nDictionary of element types:")
    print(type_dict)

    print()
    polymer = polymer_template
    final_string = ""
    #polymer = "NN"
    print(f"Input polymer template: {polymer_template}\n")
    #polymer loop
    rule_count = {}
    for i in insertion_rules:
        rule_count[i] = 0
    print("Blank Rule Count:")
    print(rule_count)

    loop_depth = 40
    print(polymer)
    polymer_list = []
    for i in range(len(polymer_template) - 1):
        polymer_list.append(polymer_template[i:i + 2])
        rule_count[polymer_template[i:i + 2]] += 1
    print(rule_count)
    for _ in range(loop_depth):
        new_rules = rule_count.copy()
        for polymer, count in list(rule_count.items()):
            if count > 0:
                #print(f"Polymer: {polymer} ==> {count}")
                children = insertion_rules[polymer]
                type_dict[children[0][1]] += count
                #print(f"  children: {children}, counting up letter {children[0][1]}")
                new_rules[children[0]] += count
                new_rules[children[1]] += count
                new_rules[polymer] -= count
        rule_count = new_rules.copy()
        #print("END OF LOOP")
        #print(f"New list of rules: \n{new_rules}")
        #print()
        



    print("DONE WITH LOOPING")
    final_string += polymer_template[-1]
    print()
    print(len(polymer))
    print(final_string)

    print(type_dict)
    
    print(max(type_dict.values()))
    print(min(type_dict.values()))

    answer = max(type_dict.values()) - min(type_dict.values())
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_14_2("input.txt")