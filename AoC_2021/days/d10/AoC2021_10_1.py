#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 10.12.21              #
#                       #
# Day 10, Part 1        #
#########################

from datetime import datetime


def aoc2021_10_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 10, Part 1\n~~ running as a test ~~")

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

    '''
        ): 3 points.
        ]: 57 points.
        }: 1197 points.
        >: 25137 points.
    ''' 
    mapped_pairs = {}#key: close symbol, value: corresponding open symbol
    mapped_pairs[")"] = "("
    mapped_pairs["]"] = "["
    mapped_pairs["}"] = "{"
    mapped_pairs[">"] = "<"

    openers = ["(", "[", "{", "<"]
    incomplete_lines = []
    corrupted_lines = []
    error_symbols = []
    for line in input_data:
        opens_li = []
        for symbol in line:
            #print(symbol, end="")
            if symbol in openers:
                opens_li.append(symbol)
                #print("o", end="")
            else:#its a closing symbol
                last_open = opens_li[-1]
                if mapped_pairs[symbol] == last_open:
                    del opens_li[-1]
                else:
                    corrupted_lines.append(line)
                    error_symbols.append(symbol)
                    break
            #print("", end=" ")
        if len(opens_li) != 0:
            incomplete_lines.append(line)
            
        #print()
        #print(opens_li)
        #print(f"Error Symbols: {error_symbols}")
        #print()

    #print("\n\n\n")
    print(f"Error Symbols: {error_symbols}")
    symbol_values = {}
    symbol_values[")"] = 3
    symbol_values["]"] = 57
    symbol_values["}"] = 1197
    symbol_values[">"] = 25137

    final_value = 0
    for sym in error_symbols:
        final_value += symbol_values[sym]
    
    answer = final_value
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_10_1("input.txt")