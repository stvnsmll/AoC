#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 06.12.21              #
#                       #
# Day 06, Part 2        #
#########################

from datetime import datetime


def aoc2021_06_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 6, Part 2\n~~ running as a test ~~")

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

    #store fish by their age-to-spawn in a dictionary
    lfish_dict = {}
    for i in range(9):
        lfish_dict[i] = 0
    print(lfish_dict)

    for lfish in starting_lfish:
        lfish_dict[lfish] += 1
    print(lfish_dict)
    original_lfish_dict = lfish_dict

    days_to_run = 256

    for i in range(days_to_run):
        tmp_dict = {}
        for lfish_age in range(8,-1,-1):
            if lfish_age == 0:
                #this is the last one, it spawns new ones (at 8) and sets current ones to 6
                no_to_spawn = lfish_dict[0]
                tmp_dict[6] += no_to_spawn
                tmp_dict[8] = no_to_spawn
            else:
                tmp_dict[lfish_age - 1] = lfish_dict[lfish_age]
        #print(f"After day {i + 1}", end=" ---> ")
        #print(tmp_dict)
        lfish_dict = tmp_dict

    final_lFish_count = 0
    for lfish_age in lfish_dict:
        final_lFish_count += lfish_dict[lfish_age]

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
   aoc2021_06_2("input.txt")