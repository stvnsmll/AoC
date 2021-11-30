#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 24.11.21              #
#                       #
# Day 07, Part 1        #
#########################

from datetime import datetime

def aoc2018_07_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 07, Part 1\n~~ running as a test ~~")

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

    dict_of_letters = {}
    for line in input_data:
        letter = line[5]
        if letter in dict_of_letters:
            dict_of_letters[letter].add_beforeStep(line)
        else:
            dict_of_letters[letter] = AsmStep(line)
        #print(f"   {line}, letter: {letter}")
    
    #print(dict_of_letters.keys())

    list_of_inputs = []
    list_of_outputs = []
    for item in dict_of_letters:
        list_of_inputs.append(dict_of_letters[item].letter)
        for beforeStep in dict_of_letters[item].beforeStep:
            if beforeStep not in list_of_outputs:
                list_of_outputs.append(beforeStep)
    
    #print(sorted(list_of_inputs))
    #print(sorted(list_of_outputs))

    exit = 0
    possible_starts = []
    while exit == 0:
        for letter in list_of_inputs:
            if letter not in list_of_outputs:
                #exit = 1
                starting_letter = letter
                #break
                possible_starts.append(letter)
        exit = 1
    exit = 0
    #print(f"possible starters: {possible_starts}")
    while exit == 0:
        for letter in list_of_outputs:
            if letter not in list_of_inputs:
                exit = 1
                ending_letter = letter
                break
    
    #print(f"starging letter: {starting_letter}\nending letter: {ending_letter}")

    dict_of_letters[ending_letter] = AsmStep(f"     {ending_letter}")


    for item in dict_of_letters:
        #print(item)
        for beforeStep in dict_of_letters[item].beforeStep:
            #print(f"  {beforeStep}")
            dict_of_letters[beforeStep].add_prerequesite(item)
        #print()

    
    #print("\n\n\n\n\n")
    #for item in sorted(dict_of_letters):
    #    dict_of_letters[item].printDeetz()
    
    #print(f"\nTotal Instruction Count = {len(list_of_inputs) + 1}")

    asm_order = []
    remaining_letters = list_of_inputs.copy()
    #print(remaining_letters)
    remaining_letters.sort()
    #print(remaining_letters)


    asm_order = []
    #print(f"Initial assembly order: {asm_order}")
    available = possible_starts
    available.sort()
    #print(f"  Starting list of available: {available}\n\n")
    exit = 0
    while exit == 0:
        if len(available) == 0:
            exit = 1
            break
        do_next = available[0]
        #print(f"Adding step: {do_next}")
        asm_order.append(do_next)
        available.remove(do_next)
        #print(f"assembly order: {asm_order}")
        # add to the available list IF all of the prerequesets are met
        for next_step in dict_of_letters[do_next].beforeStep:
            #print(f"  {next_step} has prerequesites: {dict_of_letters[next_step].prerequesites}")
            add_yes = True
            for prereq in dict_of_letters[next_step].prerequesites:
                if prereq not in asm_order:
                    add_yes = False
            if add_yes == True:
                available.append(next_step)
                #print(f"         AvailList = {available}")
        available.sort()
        #print(f"     New list of available: {available}")
        #print("\n\n")
    print(asm_order)
    

    
    #print("\n\n\n")
    #print(remaining_letters)
    #print(asm_order)

    answer = "".join(asm_order)
    print(f"\nThe order of sleigh assembly is: {answer}")
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer


class AsmStep:
    def __init__(self, input_string):
        self.letter = input_string[5]
        if len(input_string) > 15:
            self.beforeStep = [input_string[36]]
        else:
            self.beforeStep = []
        self.prerequesites = []

    def add_beforeStep(self, input_string):
        self.beforeStep.append(input_string[36])
        self.beforeStep.sort()
    
    def add_prerequesite(self, letter):
        self.prerequesites.append(letter)
        self.prerequesites.sort()

    def printDeetz(self):
        poststep = str(self.beforeStep)
        prereqs = str(self.prerequesites)
        print(f"{self.letter} must be finished before step(s) {poststep}\n    Prerequesites are: {prereqs}")


if __name__ == "__main__":
   aoc2018_07_1("input.txt")