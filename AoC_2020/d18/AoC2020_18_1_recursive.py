#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 18.12.20              #
#                       #
# Day 18, Part 1        #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d18/mathrows_testing.txt"
    else:
        testing = 0
        input_file = "./d18/mathrows.txt"

    # Using readline()
    mathrows_file = open(input_file, 'r')
    rowcount = 0
    math_data = []

    while True:
        # Get next line from file
        line = mathrows_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        math_data.append(line.strip())
        rowcount += 1

    mathrows_file.close()

    for i in math_data:
        test_string = i.replace(" ", "")
        #if test_string[0] == "(":
        #    test_string = "0+" + test_string
        t = solveMath(test_string)[0]

    answer = t

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


def solveMath(split_list):
    print(f"Incomming List: {split_list}")
    #get the first character and start appropriately...
    first_value = 30303030#new value instead of int(split_list[0])
    operator = 0#unassigned to start with
    skip_count = 1
    step_count = 0
    i = 0
    while i in range(len(split_list)):
        print(f"\nPrior Value: {first_value}")
        print(f"Step #{i}")
        print(f"Current Char: {split_list[i]}")
        print(f"Remaining String: {split_list[i:]}")
        print(f"Skip Count: {skip_count}")
        if split_list[i] == "+":
            operator = "+"
        elif split_list[i] == "*":
            operator = "*"
        elif split_list[i] == "(":
            #find the end of the string and eval?
            i += 1
            returned_val = solveMath(split_list[(i):])
            print(f"Returned value = {returned_val}")
            sub_answer = returned_val[0]
            to_skip = returned_val[1]
            i += to_skip - 2
            print(f"Sub answer is: {sub_answer}")
            if first_value == 30303030:
                first_value = sub_answer
            else:
                first_value = eval(str(first_value) + operator + str(sub_answer))
        elif split_list[i] == ")":
            print(f"Close parenth. Returning: {first_value}.")
            i = 5000000#to_return = [first_value, skip_count]
            #return to_return
        elif first_value == 30303030:
            first_value = int(split_list[i])
        elif operator == 0:
            pass
        else:
            print(f"First value {first_value}, OP: {operator}, remaining String is: {split_list[i:]}")
            first_value = eval(str(first_value) + operator + split_list[i])
            print(f"Ending Value: {first_value}")
        step_count += 1
        skip_count += 1
        i += 1
        print(step_count)
        print(i)
    to_return = [first_value, skip_count]
    return to_return


if __name__ == "__main__":
    main("r")