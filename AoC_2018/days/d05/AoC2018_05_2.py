#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 17.11.21              #
#                       #
# Day 05, Part 2        #
#########################

from datetime import datetime
import numpy as np
import string

def aoc2018_05_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 05, Part 2\n~~ running as a test ~~")

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

    input_data = input_data[0]
    #print(f"\n{input_data}")
    #print("0000000000111111")
    #print("0123456789012345")

    polymer_string = list(input_data)
    #print(polymer_string)

    #recursion exceeded depth
    #reduced_polymer = checkForPair(polymer_string, 0)
    
    charRemovedDict = dict.fromkeys(string.ascii_lowercase, 12000)
    for char in charRemovedDict:
        #print(char)
        reducedString = [x for x in polymer_string if x.lower() != char]
        #print(reducedString)
        charRemovedDict[char] = getMinLength(reducedString)

    #print(charRemovedDict)
    
    print(min(charRemovedDict.values()))

    answer = min(charRemovedDict.values())
    #print(f"The most sleepy guard is # {most_sleepy_guard}, and is usually asleep at {minute_of_most_sleep}")

    print(f"Solution is: {answer}")
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer

#recursion that went too deep
def checkForPair(string, startingindex):
    #print(string)
    index = startingindex
    nextindex = index + 1
    if index == (len(string)-1):
        return string
    #print(f"{string[index]} --compared with -- {string[nextindex]}")
    if (string[index].lower() == string[nextindex].lower()) and (string[index] != string[nextindex]):
        #print("found a pair")
        #print(f"{string[index]} --compared with -- {string[nextindex]}")
        string.pop(index)
        string.pop(index)
        checkForPair(string, (index - 1))
    else:
        checkForPair(string, nextindex)
    return string

    
def getMinLength(polymer_string):
    index = 0
    exit = 0
    while exit == 0:
        nextindex = index + 1
        #print(f"comparing {index} and {nextindex} ({polymer_string[index]} and {polymer_string[nextindex]})")
        if (polymer_string[index].lower() == polymer_string[nextindex].lower()) and (polymer_string[index] != polymer_string[nextindex]):
            #print("found a pair")
            #print(f"{polymer_string[index]} --compared with -- {polymer_string[nextindex]}")
            polymer_string.pop(index)
            polymer_string.pop(index)
            #print("newly reduced polymer string:")
            #print(polymer_string)
            #print()
            index -= 2
        if index == (len(polymer_string) - 2):
            exit = 1
        else:
            index += 1
    return len(polymer_string)


def printDict(dictionary):
    for pair in dictionary:
        print(f"Time: {pair}, Message: {dictionary[pair]}")


if __name__ == "__main__":
   aoc2018_05_2("input.txt")