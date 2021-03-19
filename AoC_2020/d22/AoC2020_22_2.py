#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 30.12.20              #
#                       #
# Day 22, Part 2        #
#########################


def main(test):

    if test == 't':
        testing = 1
        input_file = "./d22/startingHands_testing.txt"
    else:
        testing = 0
        input_file = "./d22/startingHands.txt"

    # Using readline()
    startingHands_file = open(input_file, 'r')
    hands_data = []

    while True:
        # Get next line from file
        line = startingHands_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        hands_data.append(line.strip())

    startingHands_file.close()

    #for i in hands_data:
    #    print(i)
    #print(hands_data)

    p1_hand = []
    p2_hand = []
    hand = 1
    #create each player's hands from the hand data
    for i in hands_data:
        if hand == 1:
            toadd = p1_hand
        else:
            toadd = p2_hand
        if i == "":
            hand = 2
        elif i.isnumeric():
            toadd.append(int(i))
        else:
            pass

    print("Starting Hands:")
    print(p1_hand)
    print(p2_hand)


    winner = runGame(p1_hand, p2_hand)

    print(winner)



    print(f"\nWinning Hand: {winner[1]}")

    #calculate the answer (the winners' score)
    answer = calcScore(winner[1])

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


def runGame(p1_hand, p2_hand):
    exit = 0
    i = 0
    p1_past_hands = []
    p2_past_hands = []
    while exit == 0:
        #print()
        #print(f"P1 hand: {p1_hand}")
        #print(f"P2 hand: {p2_hand}")
        #check the incomming hand for a winner
        winnerCheck = checkForWinner(p1_hand, p2_hand)
        if (winnerCheck == "p1") or (winnerCheck == "p2"):
            #print("Game or Sub-Game Over")
            #print(f"Winner of this game is: {winnerCheck}")
            winningHand = p1_hand
            if winnerCheck == "p2":
                winningHand = p2_hand
            returnItems = [winnerCheck, winningHand]
            #print(f"returning these items: {returnItems}")
            return returnItems
        else: #winnerCheck = "no one"
            #check the incomming hand for a duplicate of a past condition
            p1_new_score = calcScore(p1_hand)
            p2_new_score = calcScore(p2_hand)
            if (p1_new_score in p1_past_hands) and (p2_new_score in p2_past_hands):
                #infinite loop catcher
                returnItems = ['p1', p1_hand]
                return returnItems
            else:
                #log the new score into the past_hands lists for each player
                p1_past_hands.append(p1_new_score)
                p2_past_hands.append(p2_new_score)
            #get the new card that they will play:
            p1 = p1_hand[0]
            p2 = p2_hand[0]
            del p1_hand[0]
            del p2_hand[0]
            #print(f"P1's card: {p1}")
            #print(f"P2's card: {p2}")
            #check card vs deck length
            if (p1 <= len(p1_hand)) and (p2 <= len(p2_hand)):
                #RECURSE - sub-game is needed
                #print('recurse')
                subgame = runGame(p1_hand[:p1],p2_hand[:p2])
                winner = subgame[0]
                winning_hand = subgame[1]
            else:
                #get the winner with simple card compare
                #print("made it here")
                winner = "p1"
                winning_hand = p1_hand
                if p2 > p1:
                    winner = "p2"
                    winning_hand = p2_hand
                #print(f"{winner} is the winner of this round")
            #append winning hand to
            if winner == "p1":
                p1_hand.append(p1)
                p1_hand.append(p2)
            else:
                #print("Winner of round is pe")
                p2_hand.append(p2)
                p2_hand.append(p1)
        i+=1
        if i == 90000:
            exit = 1
            returnItems = ['p2', p2_hand]
            #return returnItems



def checkForWinner(p1_hand, p2_hand):
    if len(p1_hand) == 0:
        winner = "p2"
    elif len(p2_hand) == 0:
        winner = "p1"
    else:
        winner = "no one"
    #print(f"Winner is: {winner}")
    return winner

def calcScore(deck):
    deck_len = len(deck)
    total = 0
    for i in range(deck_len):
        total += (deck[i] * (deck_len - i))
    return total


def listToString(s):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for ele in s:
        str1 += ele
    # return string
    return str1





'''
    #main while loop for the entire game
    while exit == 0:
        print()
        print(p1_hand)
        print(p2_hand)
        winner = checkForWinner(p1_hand, p2_hand)
        if (winner == "p1") or (winner == "p2"):
            print("Game or Sub-Game Over")
            print(f"Winner is: {winner}")
            print(f"Turn Count: {turn}")
            exit = 1
        else: #winner = "no one"
            turn += 1
            p1 = p1_hand[0]
            p2 = p2_hand[0]
            #give the winner the cards at the bottom of their deck
            if p1 > p2:
                p1_hand.append(p1)
                p1_hand.append(p2)
            else:
                p2_hand.append(p2)
                p2_hand.append(p1)
            del p1_hand[0]
            del p2_hand[0]


    #find winner
    winner = p1_hand
    if len(p2_hand) > len(p1_hand):
        winner = p2_hand
    '''




if __name__ == "__main__":
    main("r")