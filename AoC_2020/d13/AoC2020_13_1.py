#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 13.12.20              #
#                       #
# Day 13, Part 1        #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d13/bus_notes_testing.txt"
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

    target_departure = int(bus_notes_data[0])
    tmp_bus_list = bus_notes_data[1].split(",")
    #remove the x values here...
    bus_list = [i for i in tmp_bus_list if i != 'x']

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

    answer = quickest_bus * current_wait

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer



if __name__ == "__main__":
    main("r")