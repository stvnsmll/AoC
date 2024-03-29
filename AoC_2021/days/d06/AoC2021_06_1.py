#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 06.12.21              #
#                       #
# Day 06, Part 1        #
#########################

from datetime import datetime


def aoc2021_06_1(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 6, Part 1\n~~ running as a test ~~")

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

    starting_lfish = [int(x) for x in input_data[0].split(",")]
    print(starting_lfish)

    list_of_lfish = []
    counter = 0
    for lfish in starting_lfish:
        list_of_lfish.append(LanternFish(counter, lfish))
        counter += 1

    print("\nStarting List: ", end="")
    printFishList(list_of_lfish)

    days_to_run = 80

    for i in range(days_to_run):
        #print(f"Running Day {i}")
        for lfish_no in range(len(list_of_lfish)):
            end_action = list_of_lfish[lfish_no].progressAge()
            if end_action == "spawn":
                list_of_lfish.append(LanternFish(len(list_of_lfish)))
        #print(f"\n after {i} days: ", end="")
        #printFishList(list_of_lfish)
    
    #print(f"\n after {days_to_run} days: ", end="")
    #printFishList(list_of_lfish)

    final_lFish_count = len(list_of_lfish)
    print(f"Lantern fish count after {days_to_run} of spawning: {final_lFish_count}\n")

    answer = final_lFish_count
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer

class LanternFish:
    def __init__(self, number, start_life = 8):
        self.name = "LF" + str(number)
        self.age = start_life
    
    def progressAge(self):
        if self.age == 0:
            self.age = 6
            return "spawn"
        self.age -= 1
        return "aged"
    
    def printFish(self):
        print(f"{self.name}={self.age}", end=" ")
    

def printFishList(lof):
    for lfish in lof:
        lfish.printFish()
    print()



if __name__ == "__main__":
   aoc2021_06_1("input.txt")