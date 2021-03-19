#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 19.12.20              #
#                       #
# Day 19, Part 1        #
#########################
import re
#import sys

def main(test):
    import re
    #import sys
    #print(sys.getrecursionlimit())
    #sys.setrecursionlimit(25000)
    from datetime import datetime
    startTime = datetime.now()

    if test == 't':
        testing = 1
        input_file = "./d19/satellite_data_testing.txt"
    else:
        testing = 0
        input_file = "./d19/satellite_data.txt"

    # Using readline()
    satellite_file = open(input_file, 'r')
    rowcount = 0
    satellite_data = []

    while True:
        # Get next line from file
        line = satellite_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        satellite_data.append(line.strip())
        rowcount += 1

    satellite_file.close()

    section = 0
    rules = []
    messages = []

    for i in satellite_data:
        if i == "":
            section += 1
        else:
            if section == 0:
                rules.append(i)
            else:#section == 1:
                messages.append(i)

    #print("The Rules: {}".format(list(rules)))
    #print("The Messages: {}".format(messages))
    global rule_dict
    rule_dict = {}
    for i in rules:
        info = i.split(": ")
        ruleID = int(info[0])
        print(info[1])
        content_a = info[1].replace("\"","")
        content = list(content_a.split())
        print(content)
        if not(content[0] == 'a' or content[0] == 'b'):
            #don't add pareenthesees around single a's or b's
            content.append(")")
            content.insert(0, "(")
        #print(content)
        '''content = []
        for j in all_content:
            content.append(list(j.split()))
        '''
        #print(f"Rule ID = {ruleID}, ", end="")
        #print(f"Content = {content}")
        rule_dict[ruleID] = content



    for i in range(len(rule_dict)):
        print(f"Rule ID = {i}, ", end="")
        print(f"Content = {rule_dict[i]}")
        #print(f"  content length: {len(rule_dict[i])}")
        #if len(rule_dict[i]) == 1:
        #    print("    This is an A or B!!! --^")

    print()

    exit = 0
    parent_list = rule_dict[0]
    counter = 0
    while exit == 0:
        parent_list_asString = listToString(parent_list)
        #print(parent_list)
        #print(parent_list_asString)
        if re.search("\d",parent_list_asString):
            #there is stll a digit in the parent list
            for i in range(len(parent_list)):
                if re.search("\d",parent_list[i]):
                    #this char os a digit:
                    #print(f"digit found: {parent_list[i]}")
                    intAtI = int(parent_list[i])
                    #print(intAtI)
                    child_rule = rule_dict[intAtI]
                    #print(f" The chid rule is: {rule_dict[intAtI]}")
                    tmp_list = parent_list[:int(i)] + child_rule + parent_list[(int(i)+ 1):]
                    parent_list = tmp_list
                    break
                else:
                    #not a digit
                    pass
                    #print(f"...not a digit: {parent_list[i]}")
        else:
            #no more digits in the upper-most level rule (all a's and b's)
            exit = 1
        counter += 1
        if counter > 50000:
            print("\n\nLOOP ERROR\n\n")
            exit = 1

    '''  Recursion Method that got too big...
    #get the parent regex:
    tmp_regex = ["\A"]
    tmp_regex.append(make_one_regex(rule_dict[0]))
    tmp_regex.append("\Z")
    parent_regex = listToString(tmp_regex)
    print(parent_regex)
    '''

    print()

    #parent_regex = "\A((a)((aa|bb)(ab|ba)|(ab|ba)(aa|bb))(b))\Z"
                  #"\A((a)((aa|bb)(ab|ba)|(ab|ba)(aa|bb))(b))\Z"
                    #\A(a((aa)|(bb)(ab)|(ba))|((ab)|(ba)(aa)|(bb))b)\Z
                    #\A(a((aa)|(bb)(ab)|(ba))|((ab)|(ba)(aa)|(bb))b)\Z
    parent_regex = "\A" + listToString(parent_list) + "\Z"
    print(parent_regex)

    total_valid = 0
    for i in messages:
        #messages can be broken into 8-bit sets
        if re.search(parent_regex, i):
            total_valid += 1

    answer = total_valid

    print(f"Runtime Duration: {(datetime.now() - startTime)}")
    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


def make_one_regex(incomming):
    #print(incomming)

    if len(incomming) == 1:
        #print("Found the end!")
        #this is an "a" or a "b"
        return incomming[0]

    #NOT an "a" or "b"
    return_regex = ["("]
    #print(return_regex)
    for i in incomming:
        #print(i)
        if i == '|':
            return_regex.append(")")
            return_regex.append("|")
            return_regex.append("(")
        else:
            return_regex.append("(")
            return_regex.append(make_one_regex(rule_dict[int(i)]))
            return_regex.append(")")
    return_regex.append(")")
    final_regex = listToString(return_regex)
    #print(final_regex)
    return final_regex


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1


if __name__ == "__main__":
    main("r")