#########################
## Advent of Code 2018 ##
#########################
# Steven Small          #
# stvnsmll              #
# 29.11.21              #
#                       #
# Day 07, Part 2        #
#########################

from datetime import datetime

worker_count = 5
minute_offset = 60

def aoc2018_07_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2018, Day 07, Part 2\n~~ running as a test ~~")
        global worker_count
        global minute_offset
        worker_count = 2
        minute_offset = 0

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

    dict_of_letters = {}
    for line in input_data:
        letter = line[5]
        if letter in dict_of_letters:
            dict_of_letters[letter].add_beforeStep(line)
        else:
            dict_of_letters[letter] = AsmStep(line)
        #print(f"   {line}, letter: {letter}")
    
    #print(dict_of_letters.keys())

    list_of_inputs = []
    list_of_outputs = []
    for item in dict_of_letters:
        list_of_inputs.append(dict_of_letters[item].letter)
        for beforeStep in dict_of_letters[item].beforeStep:
            if beforeStep not in list_of_outputs:
                list_of_outputs.append(beforeStep)
    
    #print(sorted(list_of_inputs))
    #print(sorted(list_of_outputs))

    exit = 0
    possible_starts = []
    while exit == 0:
        for letter in list_of_inputs:
            if letter not in list_of_outputs:
                #exit = 1
                starting_letter = letter
                #break
                possible_starts.append(letter)
        exit = 1
    exit = 0
    while exit == 0:
        for letter in list_of_outputs:
            if letter not in list_of_inputs:
                exit = 1
                ending_letter = letter
                break
    
    #print(f"starging letters: {possible_starts}\nending letter: {ending_letter}")

    dict_of_letters[ending_letter] = AsmStep(f"     {ending_letter}")

    #add the prerequesites
    for item in dict_of_letters:
        #print(item)
        for beforeStep in dict_of_letters[item].beforeStep:
            #print(f"  {beforeStep}")
            dict_of_letters[beforeStep].add_prerequesite(item)
        #print()

    #print("\n\n\n\n\n")
    #for item in sorted(dict_of_letters):
    #    dict_of_letters[item].printDeetz()
    
    #print(f"\nTotal Instruction Count = {len(list_of_inputs) + 1}")

    asm_order = []
    remaining_letters = list_of_inputs.copy()
    #print(remaining_letters)
    remaining_letters.sort()
    #print(remaining_letters)


    asm_order = []
    #print(f"Initial assembly order: {asm_order}")
    available = possible_starts.copy()
    available.sort()
    #print(f"  Starting list of available: {available}\n\n")
    exit = 0
    while exit == 0:
        if len(available) == 0:
            exit = 1
            break
        do_next = available[0]
        #print(f"Adding step: {do_next}")
        asm_order.append(do_next)
        available.remove(do_next)
        #print(f"assembly order: {asm_order}")
        # add to the available list IF all of the prerequesets are met
        for next_step in dict_of_letters[do_next].beforeStep:
            #print(f"  {next_step} has prerequesites: {dict_of_letters[next_step].prerequesites}")
            add_yes = True
            for prereq in dict_of_letters[next_step].prerequesites:
                if prereq not in asm_order:
                    add_yes = False
            if add_yes == True:
                available.append(next_step)
                #print(f"         AvailList = {available}")
        available.sort()
        #print(f"     New list of available: {available}")
        #print("\n\n")
    #print(asm_order)

    time = 0
    exit = 0
    list_of_workers = {}
    completed_steps = []
    available_workers = []
    available_steps = possible_starts.copy()
    waiting_prerex = []
    available_steps.sort()
    #create the worker objects
    for i in range(worker_count):
        worker_name = "W" + str(i + 1)
        list_of_workers[worker_name] = Worker(worker_name)

    #print("\n****** STARTING THE TIME LOOP ******")
    while exit == 0:
        
        #check worker statuses
        #  update any completed steps
        #  count how many workers are available
        for worker in list_of_workers:
            status = list_of_workers[worker].checkStatus(time)
            if status == "available":
                #print(f"{worker} is {status}")
                available_workers.append(worker)
            elif status == "working":
                #print(f"{worker} is working on {list_of_workers[worker].activeStep}")
                pass
            else:#status is a letter of a completed task
                #print(f"{worker} just finished step: {status}")
                available_workers.append(worker)
                completed_steps.append(status)
                #add all of the newly added "beforeSteps" if their prerequesites are in the
                #     completed steps list (add it into the available_steps list and sort it)
                for next_step in dict_of_letters[status].beforeStep:
                    #print(f"  {next_step} has prerequesites: {dict_of_letters[next_step].prerequesites}")
                    waiting_prerex.append(next_step)
                waiting_prerex = removeDuplicatesInList(waiting_prerex)
                #print(f"Steps awaiting prerequesites: {waiting_prerex}")
                remove_from_prerex = []
                for step in waiting_prerex:
                    #print(f"checking step letter: {step}")
                    add_yes = True
                    for prereq in dict_of_letters[step].prerequesites:
                        if prereq not in completed_steps:
                            add_yes = False
                    if add_yes == True:
                        available_steps.append(step)
                        remove_from_prerex.append(step)
                for step in remove_from_prerex:
                    waiting_prerex.remove(step)
                available_steps = removeDuplicatesInList(available_steps)
                
        #show the log for this loop
        #print(f"\nStarting new loop at time: {time}")
        #print(f"  available steps to work: {available_steps}")
        #print(f"  completed steps: {completed_steps}")
        #print(f"  list of waiting prerequesites: {waiting_prerex}")

        #assign all available workers to any steps that are ready to be worked
        for ready_worker in available_workers:
            if len(available_steps) != 0:
                step_to_start = available_steps[0]
                available_steps.pop(0)
                #print(f"  Worker: {ready_worker} starts step: {step_to_start}")
                list_of_workers[ready_worker].startWorking(step_to_start, time)
            else:
                #print(f"     no more steps for worker {ready_worker} to work on...")
                break

        #reset the list of available workers:
        available_workers = []
        #increment the time, then loop
        if len(completed_steps) == (len(list_of_inputs) + 1):
            exit = 1
        time += 1
        #print()
        if time > 4000000:
            print("\n\n\nError! Loop timeout\n\n\n")
            exit = 1
        
    
    print(time - 1)
    answer = time - 1
    
    #print("\n\n\n")
    #print(remaining_letters)
    #print(asm_order)

    print(f"\nThe time it takes for all the helpers to assemble the sleigh is: {answer}")
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer


class AsmStep:
    def __init__(self, input_string):
        self.letter = input_string[5]
        if len(input_string) > 15:
            self.beforeStep = [input_string[36]]
        else:
            self.beforeStep = []
        self.prerequesites = []

    def add_beforeStep(self, input_string):
        self.beforeStep.append(input_string[36])
        self.beforeStep.sort()
    
    def add_prerequesite(self, letter):
        self.prerequesites.append(letter)
        self.prerequesites.sort()

    def printDeetz(self):
        poststep = str(self.beforeStep)
        prereqs = str(self.prerequesites)
        print(f"{self.letter} must be finished before step(s) {poststep}\n    Prerequesites are: {prereqs}")


class Worker:
    def __init__(self, name):
        self.name = name
        self.state = "available"
        self.activeStep = ""
        self.availableOn = 0#second number that they will be available on again
        print(f"Created Worker: {self.name}")
    
    def startWorking(self, stepLetter, startTime):
        global minute_offset
        self.activeStep = stepLetter
        letterTime = ord(stepLetter) - 64
        end_time = startTime + minute_offset + letterTime
        #set object state!
        self.state = "working"
        self.activeStep = stepLetter
        self.availableOn = end_time
    
    def checkStatus(self, current_time):
        #function either returns:
        #   "available" if the worker is ready for a job
        #   "working" if the worker is currently still on a step
        #   {letter} if the worker just completed a step and is now ready for a new one
        returnMessage = "available"
        if current_time >= self.availableOn:
            #if was working, but just finished:
            if self.state == "working":
                #return the letter that just finished the job.
                returnMessage = self.activeStep
            self.state = "available"
            self.activeStep = ""
            self.availableOn = 0
        else:
            returnMessage = "working"
        return returnMessage


def removeDuplicatesInList(incomminglist):
    #remove duplicates and then sort
    new_list = list(dict.fromkeys(incomminglist))
    new_list.sort()
    return new_list


if __name__ == "__main__":
   aoc2018_07_2("input.txt")