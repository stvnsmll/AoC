#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 13.12.20              #
#                       #
# Day 13, Part 2        #
#########################


def main(test):
    import numpy as np

    if test == 't':
        testing = 1
        input_file = "./d13/bus_notes_testing2.txt"
    else:
        testing = 0
        input_file = "./d13/bus_notes.txt"

    # Using readline()
    bus_notes_file = open(input_file, 'r')
    rowcount = 0
    bus_notes_data = []

    while True:
        # Get next line from file
        line = bus_notes_file.readline().strip()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        bus_notes_data.append(line)
        rowcount += 1

    bus_notes_file.close()

    #not needed for part 2.
    #target_departure = int(bus_notes_data[0])
    tmp_list = bus_notes_data[1].replace('x','1')
    bus_list = list(map(int, tmp_list.split(",")))

    #bus_list = [1789,37,47,1889]


    step_size = bus_list[0]
    step_list = [bus_list[0],1]
    counter = bus_list[0]
    exit = 0
    log = 1000000
    while exit == 0:
        for i in range(len(bus_list)):
            #print("Integer {} at Counter: {}, and Step Size: {}, position {}".format(bus_list[i], counter, step_size, i))
            #modulo = (counter + i) % bus_list[i]
            #print(modulo)
            if (counter + i) % bus_list[i] == 0:
                if (counter != 0) and (bus_list[i] not in step_list):
                    print("orig Step size: {}, bus #: {}".format(step_size, bus_list[i]))
                    step_list.append(bus_list[i])
                    step_size *= bus_list[i]
                    print("New step size: {}".format(step_size))
                #exit check: terminate the while loop if the last character validated the check
                if i == (len(bus_list) - 1):
                    print("Integer {} at Counter: {}, and Step Size: {}, position {}".format(bus_list[i], counter, step_size, i))
                    print("Answer Found --^")
                    exit = 1
                    break
                #counter += step_size
            else:
                #print("  Modulo != 0 NEXT!")
                #step_size = bus_list[0]
                counter += step_size
                break
            #print("Ref Point A: counter = {}".format(counter))
        #print("Ref Point B: counter = {}".format(counter))
        #if counter > log:
        #    print(counter)
        #    log = counter + 1000000
        if counter > 410900000000000000000:
            exit = 2

    answer = counter
    print(answer)


    '''
    #13.1 solution:
    print("You want to leave at {}, and the bus list is:\n  {}".format(target_departure, bus_list))

    min_departure_after_target = 0
    current_wait = 100000000
    quickest_bus = 0
    for i in bus_list:
        #this tells how many minutes after the last bus you'd have to wait
        minutes_to_wait = int(i) - (target_departure % int(i))
        if minutes_to_wait < current_wait:
            quickest_bus = int(i)
            current_wait = int(minutes_to_wait)

    print("\n The quickest bus is: {}, with only a {} minute wait.".format(quickest_bus, minutes_to_wait))
    '''

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer



if __name__ == "__main__":
    main("r")