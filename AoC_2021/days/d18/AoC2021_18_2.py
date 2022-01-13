#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 13.01.22              #
#                       #
# Day 18, Part 2        #
#########################

from datetime import datetime


def aoc2021_18_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 18, Part 2\n~~ running as a test ~~")

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

    print(input_data)
    print()
    solution_list = []
    for str1 in input_data:
        for str2 in input_data:
            if str1 != str2:
                added_str = "[" + str1 + "," + str2 + "]"
                resultant = check_rules_looper(added_str)
                one_mag = get_magnitude(resultant)
                solution_list.append(one_mag)

    print(len(solution_list))

    answer = max(solution_list)
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer


def get_magnitude(string_data):
    full_number = eval(string_data)
    if type(full_number) == int:
        return full_number
    solution = (3 * get_magnitude(str(full_number[0]))) + (2 * get_magnitude(str(full_number[1])))
    return solution


def check_rules_looper(start_string):
    checked_string = check_rules(start_string)

    while checked_string != start_string:
        start_string = checked_string
        checked_string = check_rules(start_string)
    
    return checked_string
    

def check_rules(incoming_string):
    #1 check if a pair is nested inside 4 pairs (5 levels deep) ----> if so, explode
    #2 check if a regular number is >9 ----> if so, split
    #return the simplified string
    new_string = incoming_string
    if depth_check(incoming_string):
        #print("EXPLODE REQUIRED NOW!")
        exploded_string = explode(incoming_string)
        new_string = exploded_string
    elif split_check(incoming_string):
        #print("SPLIT REQUIRED NOW (>9)!")
        split_string = split_str(incoming_string)
        new_string = split_string
    return new_string

def depth_check(incoming_string):
    #return TRUE if there is a depth greater than 4...
    open_bracket_count = 0
    for i in incoming_string:
        if i == "[":
            open_bracket_count += 1
        elif i == "]":
            open_bracket_count -= 1

        if open_bracket_count == 5:
            return True
    return False

def split_check(incoming_string):
    #return True if any real number is > 9, otherwise return False
    all_numbers = incoming_string.replace("[", ",").replace("]", ",").split(",")
    #print(all_numbers)
    for number in all_numbers:
        if number:
            if int(number) > 9:
                return True
    return False

def explode(incoming_string):
    #returns the new string after one explode operation
    #get to the first location that is > 4 levels deep
    #print(f"\nString to Explode: {incoming_string}")
    open_bracket_count = 0
    x_pos = 0
    exit = 0
    while exit == 0:
        if incoming_string[x_pos] == "[":
            open_bracket_count += 1
        elif incoming_string[x_pos] == "]":
            open_bracket_count -= 1
        x_pos += 1
        if open_bracket_count == 5:
            #do the explode at this location
            exit = 1
    
    #print(f"Explode at position: {x_pos}")
    rest_of_number = incoming_string[(x_pos):].split("]")[0]
    #print(rest_of_number)
    full_number_to_explode = eval("[" + rest_of_number + "]")
    #print(full_number_to_explode)
    left_val = full_number_to_explode[0]
    right_val = full_number_to_explode[1]
    #print(f"value at x_pos: {incoming_string[x_pos]}")
    #print(f"Number to Explode: [{left_val},{right_val}]")

    remainder_left = incoming_string[0:(x_pos - 1)]
    #print(f"Remainder left: {remainder_left}")
    remainder_right = incoming_string[x_pos + len(rest_of_number) + 1:]
    #print(f"Remainder right: {remainder_right}")


    chars_to_skip = ["[", "]", ","]
    replace_left_start = x_pos - 2
    while remainder_left[replace_left_start] in chars_to_skip:
        #print(remainder_left[replace_left_start])
        replace_left_start -= 1
        if replace_left_start == 0:
            #print("DONT LOOP - no number to add to the left")
            break
    if replace_left_start != 0:
        #this will change the remainder_left contents...
        #get the replace_left_end
        #print(f"RLS: {replace_left_start}")
        #print(remainder_left[replace_left_start])
        #print(remainder_left[:replace_left_start + 1].replace("[", "").replace("]", "").split(",")[-1])
        left_to_replace = remainder_left[:replace_left_start + 1].replace("[", "").replace("]", "").split(",")[-1]
        #print(f"Left to replcace: {left_to_replace}")
        replace_left_end = replace_left_start - len(left_to_replace)
        #print(replace_left_end)
        left_to_replace = int(left_to_replace)
        new_left = left_to_replace + left_val
        #print(f" Number to replace (left): {left_to_replace}")
        #print(f" New Number (left): {new_left}")
        left_limit = replace_left_start - len(str(left_to_replace)) + 1
        #print(f"left limit: {left_limit}")
        remainder_left = remainder_left[:left_limit] + str(new_left) + remainder_left[left_limit + len(str(left_to_replace)):]
        #print(remainder_left)

    right_offset_start = 1
    while remainder_right[right_offset_start] in chars_to_skip:
        #print(remainder_right[right_offset_start])
        right_offset_start += 1
        if right_offset_start == len(remainder_right):
            #print("DONT LOOP - no number to add to the right")
            break
    if right_offset_start != len(remainder_right):
        #this will change the remainder_right contents...
        #get the replace_right_end
        #print(remainder_right[right_offset_start])
        right_to_replace = remainder_right[right_offset_start:].replace("[", "").replace("]","").split(",")[0]
        #print(right_to_replace)
        right_offset_end = len(right_to_replace) + right_offset_start
        #print(right_offset_end)
        right_to_replace = int(right_to_replace)
        new_right = right_to_replace + right_val
        #print(f" Number to replace (right): {right_to_replace}")
        #print(f" New Number (right): {new_right}")
        remainder_right = remainder_right[:right_offset_start] + str(new_right) + remainder_right[right_offset_start + len(str(right_to_replace)):]
        #print(remainder_right)
    
    #print()
    final_exploded_string = remainder_left + "0" + remainder_right
    #print(final_exploded_string)
    #print("done with explode\n")
    return(final_exploded_string)


def split_str(incoming_string):
    #returns the new string after one split operation
    #print(f"\n\n\nNEED TO PERFORM THE SPLIT on:\n{incoming_string}")
    for start_loc in range(len(incoming_string)):
        #print(incoming_string[start_loc:start_loc + 2])
        #print((incoming_string[start_loc:start_loc + 2]).isnumeric())
        if (incoming_string[start_loc:start_loc + 2]).isnumeric():
            #found a two digit number to split!
            no_to_split = incoming_string[start_loc:start_loc + 2]
            break
    #get the full length of the number to split
    full_number_to_split = incoming_string[start_loc:].replace(",", "]").split("]")[0]
    no_to_split = full_number_to_split
    #print(f"Number to split: {no_to_split} at location {start_loc}")
    new_pair = "[" + str(int(int(no_to_split)/2)) + "," + str(round(int(no_to_split)/2 + 0.001)) + "]"
    #print(new_pair)
    new_string = incoming_string[:start_loc] + new_pair + incoming_string[start_loc + len(no_to_split):]
    #print(new_string)
    #print("done with split")
    return new_string




if __name__ == "__main__":
   aoc2021_18_2("input.txt")