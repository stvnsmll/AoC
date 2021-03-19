#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 16.12.20              #
#                       #
# Day 15, Part 2        #
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
    for i in range(len(start_list) - 1):
        all_turns[start_list[i]] = turn
        static_log.append(start_list[i])
        turn += 1
    static_log.append(start_list[-1:][0])

    #start the game:
    '''
    Rules:
    Each turn consists of considering the most recently spoken number:
        If that was the first time the number has been spoken, the current player says 0.
        Otherwise, the number had been spoken before; the current player announces how many
        turns apart the number is from when it was previously spoken.
    '''
    while exit == 0:
        if turn%1000000 == 0:
            print("Starting list (turn {})".format(turn))
        #print(all_turns)
        #print(static_log)
        prior_number = static_log[-1:][0]
        prior_number_key = turn
        #print("Prior number is: {} (key: {})".format(prior_number, prior_number_key))
        if prior_number in all_turns:
            #the number is NOT new.
            #print("{} is NOT new.".format(prior_number))
            previous_key = all_turns[prior_number]
            #print("Previous Key is: {}".format(previous_key))
            turn_diff = turn - previous_key
            #print("Value to say next (apend): {}".format(turn_diff))
            static_log.append(turn_diff)
            all_turns[prior_number] = prior_number_key

        else:
            #the number is new!
            #print("New number is 0!!!")
            static_log.append(0)
            all_turns[prior_number] = turn
        static_log.pop(0)

        #print(static_log)
        #print()
        turn += 1
        if turn > 30000000:
            exit = 1

    #print("\n\n\n\n\n\n")
    #print(list(all_turns.keys()))
    #print(static_log)
    print("\n\n")
    print(static_log)

    answer = static_log[-3]

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


def getKey(val):
    for key, value in all_turns.items():
        if val == value:
            return key
    return -1


if __name__ == "__main__":
    main("r")