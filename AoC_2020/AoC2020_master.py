#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 05.12.20              #
#                       #
# Using python3. again. #
#                       #
#  Master Running File  #
#########################

'''
How to use:
This python script takes in arguments:
    1- Day to Run; int  (i.e. 1, 2, 3.. 25)
    2- Part to Run: int (i.e. 1 or 2)
    3- (optional) "t" to run as a test
'''

import os
from sys import argv, path
from importlib import import_module
import csv
import re



def main():

    if ((len(argv) != 4) and (len(argv) != 3)):
        print("Usage: python3 AoC2020_master.py int(day to run) int(part to run) optional[str('t' to run as test)]")
        return 1

    #print('Argument List:', str(argv))

    # Check argument formats (str, int, int, opt(str))

    #NEED TO FIGURE OUT VALIDATION HERE
    #if (isinstance(argv[0], str) and argv[1].isdigit())) and argv[2].isdigit:
    #    print("Usage: python3 AoC2020_master.py int(day to run) int(part to run) optional: str('t' to run as test)\n  Check your input formats.")
    #    return 1

    day = f"{int(argv[1]):02d}"
    part = int(argv[2])
    test = "no"

    # Check if the user intended to run it as a test
    if len(argv) == 4:
        if argv[3] != "t":
            print("The final argument must be 't' if you want to run it as a test.")
            return 1
        else:
            test = "yes"
            print("\n#####################\n# RUNNING AS A TEST #\n#####################")


    if test == "yes":
        print("     ** test **")
    else:
        print("\n#####################\n##     FULL RUN    ##\n#####################")
    print("   Day: " + str(day) + ", Part:" + str(part))
    print("---------------------\n")

    path.insert(0, '/home/ubuntu/personal/AoC2020/d' + str(day))

    module = "AoC2020_" + str(day) + "_" + str(part)
    mod = import_module(module)



    print()

    print(" **** PRINTOUTS FROM DAY RAN **** \n/                                \\")
    print("|                                |\n")

    if test == "yes":
        dayrunresult = mod.main("t")
    else:
        dayrunresult = mod.main("r")

    print("\n|                                |")
    print("\                                /\n ******** END OF DAY RUN ******** \n\n")
    print("*********** Result ***********")

    # If a test, get the solution
    if test == "yes":
        answerkey_filepath =  "./d" + str(day) + "/test_result_" + str(day) + "_" + str(part) + ".txt"
        answerkey_file = open(answerkey_filepath, 'r')
        solution = answerkey_file.readline().strip()
        print("Expected: " + str(solution))
        print("Got:      " + str(dayrunresult))
        print("\nFINAL VERDICT:")
        if str(dayrunresult) == str(solution):
            print(" ---> PASS! <---")
        else:
            print(" ---> fail. <---")
    else:
        print("Final Answer: " + str(dayrunresult))

    print("******************************\n\n\nentire master run complete\n")




if __name__ == "__main__":
    main()