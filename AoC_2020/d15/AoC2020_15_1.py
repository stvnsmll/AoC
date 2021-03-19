#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 15.12.20              #
#                       #
# Day 15, Part 1        #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d15/puzzle_start_testing.txt"
    else:
        testing = 0
        input_file = "./d15/puzzle_start.txt"

    # Using readline()
    puzzlestart_file = open(input_file, 'r')
    rowcount = 0
    puzzlestart_data = []

    while True:
        # Get next line from file
        line = puzzlestart_file.readline().strip()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        puzzlestart_data.append(line)
        rowcount += 1

    puzzlestart_file.close()

    start_list = list(map(int, puzzlestart_data[0].split(',')))
    #for i in start_list:
    #    print(i)

    exit = 0
    turn = 0
    global all_turns
    all_turns = {}
    static_log = []
    was_new = 1

    #populate the first set of turns:
    for i in start_list:
        all_turns[i] = turn
        static_log.append(i)
        turn += 1

    #start the game:
    '''
    Rules:
    Each turn consists of considering the most recently spoken number:
        If that was the first time the number has been spoken, the current player says 0.
        Otherwise, the number had been spoken before; the current player announces how many
        turns apart the number is from when it was previously spoken.
    '''
    while exit == 0:
        #print("\nStarting list (turn {})".format(turn))
        #print(all_turns)
        #print(static_log)
        prior_number = static_log[-1:][0]
        prior_number_key = turn - 1
        #print(static_log[:-1])
        #print("Prior number is: {} (key: {})".format(prior_number, prior_number_key))
        if prior_number not in static_log[:-1]:
            #the number is new!
            #print("New number is 0!!!")
            static_log.append(0)
            #all_turns[0] = turn
        else:
            #the number is NOT new.
            #print("{} is NOT new.".format(prior_number))
            backwards_list = (static_log[:-1])[::-1]
            #print(backwards_list)
            previous_key = (len(static_log) - backwards_list.index(prior_number) - 2)
            #print("Previous Key is: {}".format(previous_key))
            turn_diff = prior_number_key - previous_key
            #print("Value to say next (apend): {}".format(turn_diff))
            static_log.append(turn_diff)
            #all_turns[turn_diff] = previous_key


        turn += 1
        if turn > 2019:
            exit = 1

    print()
    #print(list(all_turns.values()))
    #print(list(static_log))
    #print(static_log[2019])

    answer = static_log[2019]

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


def GetKey(val):
    for key, value in all_turns.items():
        if val == value:
            return key
    return -1


if __name__ == "__main__":
    main("r")