
myList = ["A","B","C","D","B","B","A","G"]

prior_key = (len(myList) - myList[::-1].index("A") - 1)

print(index_value)



        '''
        15/12/2020 stuff...
        print("Starting list (turn {})".format(turn))
        print(list(all_turns.values()))
        prior_number = all_turns[(turn - 1)]
        prior_number_key = GetKey(prior_number)
        print("Prior number is: {} (key: {})".format(prior_number, prior_number_key))
        print(static_log[:-1])
        if prior_number in static_log[:-1]:
            print("that was already in the static log")
            turn_dif = turn - prior_number_key - 1
            print("Turn Difference is: {}".format(turn_dif))
            #delete any prior instance of the turn_diff
            all_turns[prior_number_key] = "x"

            all_turns[turn] = turn_dif
            static_log.append(turn_dif)
        else:
            print("that was new!")
            if all_turns[GetKey(0)] != -1:
                all_turns[GetKey(0)] = "X"
                was_new = 0
            all_turns[turn] = 0
            static_log.append(0)
            was_new = 1
        print(list(all_turns.values()))
        print(list(static_log))
        print()
        '''


'''
Given the starting numbers 1,3,2, the 2020th number spoken is 1.
Given the starting numbers 2,1,3, the 2020th number spoken is 10.
Given the starting numbers 1,2,3, the 2020th number spoken is 27.
Given the starting numbers 2,3,1, the 2020th number spoken is 78.
Given the starting numbers 3,2,1, the 2020th number spoken is 438.
Given the starting numbers 3,1,2, the 2020th number spoken is 1836.
'''