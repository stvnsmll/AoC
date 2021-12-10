#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 10.12.21              #
#                       #
# Day 10, Part 2        #
#########################

from datetime import datetime


def aoc2021_10_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 10, Part 2\n~~ running as a test ~~")

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
    finishing_list = []
    for line in input_data:
        error_found = 0
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
                    error_found = 1
                    break
            #print("", end=" ")
        if len(opens_li) != 0:
            if error_found == 0:
                incomplete_lines.append(line)
                #print(line)
                #print(opens_li[::-1])
                finishing_list.append(opens_li[::-1])
        #print()
        #print(opens_li)
        #print(f"Error Symbols: {error_symbols}")
        #print()

        #}}]])})]

    #print("\n\n\n")
    #print(f"Error Symbols: {error_symbols}")
    symbol_values = {}
    symbol_values[")"] = 3
    symbol_values["]"] = 57
    symbol_values["}"] = 1197
    symbol_values[">"] = 25137

    final_value = 0
    for sym in error_symbols:
        final_value += symbol_values[sym]

    autocomplete_pts = {}
    autocomplete_pts["("] = 1
    autocomplete_pts["["] = 2
    autocomplete_pts["{"] = 3
    autocomplete_pts["<"] = 4

    all_total_scores = []
    for line in finishing_list:
        total_score = 0
        for sym in line:
            total_score *= 5
            total_score += autocomplete_pts[sym]
        #print(total_score)
        #print(f"{line} --> Score: {total_score}")
        all_total_scores.append(total_score)
    
    all_total_scores.sort()
    #print(all_total_scores)
    mid_point = int(len(all_total_scores) / 2)
    #print(mid_point)
    answer = all_total_scores[mid_point]

        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_10_2("input.txt")