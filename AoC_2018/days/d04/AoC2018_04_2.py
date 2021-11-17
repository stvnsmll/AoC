#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 16.11.21              #
#                       #
# Day 04, Part 2        #
#########################

from datetime import datetime
import numpy as np

def aoc2018_04_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 04, Part 2\n~~ running as a test ~~")

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
    
    guard_list = []
    #view the input data
    for i in input_data:
        guard_list.append(LineOfData(i))

    guard_dict = {}
    j = 0
    for entry in guard_list:
        guard_dict[entry.abstime] = entry.content
    
    #printDict(guard_dict)
    
    guard_dict_sorted = {}
    for i in sorted(guard_dict):
        guard_dict_sorted[convert_time_back(i)] = guard_dict[i]

    #print("Sorted list of Guard shifts and sleep cycles:")
    #printDict(guard_dict_sorted)

    #create GuardSchedule objects for each guard:
    list_of_guards = {}
    guardID = 0
    start_minute = 0
    for line in guard_dict_sorted:
        #the line is an initiation of a guard
        if type(guard_dict_sorted[line]) == int:
            guardID = guard_dict_sorted[line]
            #print(f"this starts guard #: {guardID}")
            if guardID not in list_of_guards:
                #print("new guard")
                #create class instance for the guard
                list_of_guards[guardID] = GuardSchedule(guardID)
            else:
                pass
                #print("add to existing")
                #don't need to create a new instance
        else: #the line is an action
            action = guard_dict_sorted[line]
            time = datetime.strptime(line, "%Y-%m-%d %H:%M").minute
            if action == "falls asleep":
                #print(f"   Guard #{guardID} falls alseep at minute {time}")
                start_minute = time
            elif action == "wakes up":
                #print(f"   Guard #{guardID} wakes up at minute {time}")
                end_minute = time
                list_of_guards[guardID].addSleepRange(start_minute, end_minute)
            else:
                print("Error 297483")
            #print(guardID)
            #print(f"      Time: {line}, Action: {action}")

    '''for guard in list_of_guards:
        list_of_guards[guard].printMyID()
        list_of_guards[guard].countAllSleeps()
        list_of_guards[guard].minuteMostAlseep()
        print()'''
    
    max_repeatminute = 0
    most_sleepy_guard = 0
    top_overlapCount = 0
    for guard in list_of_guards:
        sleep_time = list_of_guards[guard].minuteMostAlseep()
        overlapCount = list_of_guards[guard].maxOverlapCount()
        #print(overlapCount)
        if overlapCount > top_overlapCount:
            most_sleepy_guard = guard
            top_overlapCount = overlapCount

    print()
    print(most_sleepy_guard)
    minute_of_most_sleep = list_of_guards[most_sleepy_guard].minuteMostAlseep()
    print(f"The most sleepy guard is # {most_sleepy_guard}, and is usually asleep at {minute_of_most_sleep}")

    answer = most_sleepy_guard * minute_of_most_sleep

    print(f"Solution is: {answer}")
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer



class LineOfData:
    def __init__(self, line):
        line_details = line.replace("[", "").split("] ")
        self.timestamp = line_details[0]
        #if it's a guard event, just leave the guard number, else leaves the message
        if line_details[1][0] == "G":
            self.content = int(line_details[1].replace(" begins shift", "").replace("Guard #",""))
        else:
            self.content = line_details[1]
        self.abstime = convert_time_out(line_details[0])

class GuardSchedule:
    def __init__(self, guardID):
        self.name = guardID
        self.hourDict = createEmptyHourDict()
        self.sleepMinute = 0
    
    def printMyID(self):
        print(self.name)
    
    def addSleepMinute(self, minute):
        #print(f"adding a minute of sleep to minute # {minute}")
        self.hourDict[minute] += 1
    
    def addSleepRange(self, start, end):
        #print(f"do the range thing: {start} to {end}")
        for i in range(start, end):
            self.addSleepMinute(i)
        #print(self.hourDict)
    
    def countAllSleeps(self):
        sum = 0
        for i in self.hourDict:
            sum += self.hourDict[i]
        #print(sum)
        return sum
    
    def minuteMostAlseep(self):
        #print(max(self.hourDict, key=self.hourDict.get))
        self.sleepMinute = max(self.hourDict, key=self.hourDict.get)
        return self.sleepMinute
    
    def maxOverlapCount(self):
        return max(self.hourDict.values())
        


#helper functions
def convert_time_out(stamp):
    d = datetime.strptime(stamp, "%Y-%m-%d %H:%M")
    return int(d.timestamp())

def convert_time_back(stamp):
    stamp2 = datetime.fromtimestamp(stamp)
    d = datetime.strftime(stamp2, "%Y-%m-%d %H:%M")
    return (d)

def printDict(dictionary):
    for pair in dictionary:
        print(f"Time: {pair}, Message: {dictionary[pair]}")

def createEmptyHourDict():
    empty_hour_dict = {}
    for i in range(60):
        empty_hour_dict[i] = 0
    return empty_hour_dict

if __name__ == "__main__":
   aoc2018_04_2("input.txt")