## Advent of Code 2021 ##
#########################
# Steven Small          #
#########################
# stvnsmll              #
# 08.12.21              #
#                       #
# Day 08, Part 2        #
#########################

from datetime import datetime
import functools


def aoc2021_08_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 8, Part 2\n~~ running as a test ~~")

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
    
    #or i in signals:
    #    print(signals[i])
    sum_of_messages = 0

    for i in signals:
        message = message_solver(signals[i])
        sum_of_messages += message
        print(f"FOUND MESSAGE: {message}")
    

    #sum all of the output codes

    answer = sum_of_messages
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer


def unique_chars(solution_dict, list_of_strings):
    reduced_lists = remove_knowns(solution_dict, list_of_strings)
    #rint(reduced_lists)
    if len(reduced_lists) == 2:
        unique_chars = [x for x in (set(reduced_lists[0]) ^ set(reduced_lists[1]))]
    else:
        reduced = do_task2(reduced_lists)
        unique_chars = [x for x in reduced]
    #print(unique_chars)
    return(unique_chars)


def remove_knowns(solution_dict, list_of_strings):
    known_values = []
    for key in solution_dict:
        known_values.append(solution_dict[key])
    reduced_lists = []#remove any known values from the incomming lists
    for list in list_of_strings:
        tmp_list = []
        for char in list:
            if char not in known_values:
                tmp_list.append(char)
        reduced_lists.append(tmp_list)
    return reduced_lists


def do_task2(list_of_lists):
    list_of_sets = list(map(set, list_of_lists))
    list_of_intersects = [X & Y for X in list_of_sets for Y in list_of_sets if X is not Y]
    intersects = functools.reduce(do_or, list_of_intersects)
    ors = functools.reduce(do_or, list_of_sets)
    return ors - intersects

def do_or(s1, s2):
    return s1 | s2


def message_solver(signal):
    #decrypt the letter code
    decode_list = signal[0]
    output_list = signal[1]
    #print(f"Code to decode: {decode_list}")
    length_dict = {}
    solution_dict = {} #position: letter
    #initialize the length dictionary
    for i in range(2,8):
        length_dict[i] = []
    for code in decode_list:
        #print(code)
        length_dict[len(code)] += [list(code)]
    #print(length_dict)
    pos36 = length_dict[2][0]
    #print(f"\n            Positions 3 or 6 are these: {length_dict[2][0]}")

    pos1 = unique_chars(solution_dict, [length_dict[2][0], length_dict[3][0]])[0]
    #print(f"Position # 1 is: {pos1} -- SET")
    solution_dict[1] = pos1
    pos24 = unique_chars(solution_dict, [length_dict[2][0], length_dict[4][0]])
    #print(f"            Positions 2 or 4 are these: {pos24}")
    pos345_1 = unique_chars(solution_dict, [length_dict[6][0], length_dict[6][1]])
    pos345_2 = unique_chars(solution_dict, [length_dict[6][1], length_dict[6][2]])
    pos345_3 = unique_chars(solution_dict, [length_dict[6][0], length_dict[6][2]])
    pos345 = list(set(pos345_1 + pos345_2 + pos345_3))
    #print(f"            Positions 3,4,5 are these: {pos345}")
    pos4 = list(set(pos24).intersection(pos345))[0]
    #print(f"Position # 4 is: {pos4} -- SET")
    solution_dict[4] = pos4
    pos34 = unique_chars(solution_dict, [pos345, [pos4]])
    #print(f"            Positions 3 or 4 are these: {pos34}")
    pos2 = unique_chars(solution_dict, [pos24, [pos4]])[0]
    #print(f"Position # 2 is: {pos2} -- SET")
    solution_dict[2] = pos2
    pos3 = list(set(pos34).intersection(pos36))[0]
    #print(f"Position # 3 is: {pos3} -- SET")
    solution_dict[3] = pos3
    pos6 = unique_chars(solution_dict, [pos36, [pos3]])[0]
    #print(f"Position # 6 is: {pos6} -- SET")
    solution_dict[6] = pos6
    pos5 = unique_chars(solution_dict, [pos345, [pos3, pos4]])[0]
    #print(f"Position # 5 is: {pos5} -- SET")
    solution_dict[5] = pos5
    pos7 = unique_chars(solution_dict, [length_dict[7][0], pos345, [pos2, pos1, pos6]])[0]
    #print(f"Position # 7 is: {pos7} -- SET")
    solution_dict[7] = pos7
    
    #map the digits to their letters for this case:
    number0_lst = [pos1, pos2, pos3, pos5, pos6, pos7]
    number1_lst = [pos6, pos3]
    number2_lst = [pos1, pos3, pos4, pos5, pos7]
    number3_lst = [pos1, pos3, pos4, pos6, pos7]
    number4_lst = [pos2, pos3, pos4, pos6]
    number5_lst = [pos1, pos2, pos4, pos6, pos7]
    number6_lst = [pos1, pos2, pos4, pos5, pos6, pos7]
    number7_lst = [pos1, pos3, pos6]
    number8_lst = [pos1, pos2, pos3, pos4, pos5, pos6, pos7]
    number9_lst = [pos1, pos2, pos3, pos4, pos6, pos7]
    number0_lst.sort()
    number1_lst.sort()
    number2_lst.sort()
    number3_lst.sort()
    number4_lst.sort()
    number5_lst.sort()
    number6_lst.sort()
    number7_lst.sort()
    number8_lst.sort()
    number9_lst.sort()
    number_keys = {}
    number_keys[0] = "".join(number0_lst)
    number_keys[1] = "".join(number1_lst)
    number_keys[2] = "".join(number2_lst)
    number_keys[3] = "".join(number3_lst)
    number_keys[4] = "".join(number4_lst)
    number_keys[5] = "".join(number5_lst)
    number_keys[6] = "".join(number6_lst)
    number_keys[7] = "".join(number7_lst)
    number_keys[8] = "".join(number8_lst)
    number_keys[9] = "".join(number9_lst)
     
    #read the digits of the output code
    decrypted_string = ""
    for message in output_list:
        a = list(message)
        a.sort()
        sorted_message = "".join(a)
        #print(sorted_message, end=" --> ")
        for number_key in number_keys:
            if sorted_message == number_keys[number_key]:
                #print(f"FOUND NUMBER: {number_key}")
                decrypted_string += str(number_key)
                break
    decrypted_number = int(decrypted_string)
    #print(decrypted_number)
    return decrypted_number

if __name__ == "__main__":
   aoc2021_08_2("input.txt")