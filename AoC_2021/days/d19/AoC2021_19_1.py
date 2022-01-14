#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 14.01.22              #
#                       #
# Day 19, Part 1        #
#########################

from datetime import datetime
import numpy as np


def aoc2021_19_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 19, Part 1\n~~ running as a test ~~")

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

    '''
    (0, 1) --> rotates into the screen
    (1, 0) --> rotates forward out of the screen
    (0, 2) --> rotates left
    (2, 0) --> rotates right
    (1, 2) --> rotates counterclockwise
    (2, 1) --> rotates clockwise
    '''
    
    arr1 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
    print(arr1)
    for i in range(3):
        b = np.rot90(arr1, (i + 1), (2, 1))
        print(f"After rotating arr ({i +1} times):\n",b)
    print()


    
    answer = 0
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



if __name__ == "__main__":
   aoc2021_19_1("input.txt")