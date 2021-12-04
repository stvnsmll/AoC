#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 04.12.21              #
#                       #
# Day 04, Part 2        #
#########################

from datetime import datetime


def aoc2021_04_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 04, Part 2\n~~ running as a test ~~")

    startTime = datetime.now()

    # Using readline()
    input_data_file = open(filename, 'r')
    input_data = {}
    input_data[0] = []
    group_count = 0
    while True:
        # Get next line from file
        line = input_data_file.readline()
        # if line is empty end of file is reached
        if not line:
            break
        if line == "\n":#blank line
            group_count += 1
            input_data[group_count] = []
        else:
            input_data[group_count] = input_data[group_count] + [line.strip()]

    input_data_file.close()

    #for i in input_data:
        #print(i)
        #print(input_data[i])
    
    bingo_commands = [int(x) for x in input_data[0][0].split(",")]
    print("\nData Loaded")
    #print(f"  Bingo commands: {bingo_commands}\n")

    bingo_board = {}
    for bingo_board_count in range(len(input_data) - 1):
        bingo_board[bingo_board_count] = BingoBoard(bingo_board_count, input_data[bingo_board_count + 1])
        #bingo_board[bingo_board_count].printBoard("number")# "number" or "score"
    
    print("\nStarting the Game\n")

    exit = 0
    rounds = 0
    winning_boards = []
    for number in bingo_commands:
        rounds += 1
        for board in bingo_board:
            bingo_board[board].check_for_value(number)
            if board not in winning_boards:
                result = bingo_board[board].check_for_win()
                if result != "no win":
                    winning_boards.append(result)
                    #print(f"Winning Board: {result}")
                    #print(f"Last number: {number}")
                    #bingo_board[result].printBoard("number")
                    #print()
                    #bingo_board[result].printBoard("score")
                    board_score = bingo_board[result].getFinalScore()
                    answer = number * board_score
                    #exit = 1
                    #break
        if exit == 1:
            pass#break
    
    print(winning_boards)

    print(rounds)
    #answer = 0
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer


class BingoBoard():
    def __init__(self, number, board_data):
        #print(f"Making Board #{number}")
        self.boardnumber = number
        self.numberboard = []
        self.scoreboard = []
        for row in board_data:
            row_int = [int(x) for x in row.replace("  "," ").split(" ")]
            self.numberboard = self.numberboard + [row_int]
            self.scoreboard = self.scoreboard + [[0, 0, 0, 0, 0]]
        #Board is a list of lists, where you call a position by self.board[row][column] (zero index)
    
    def check_for_value(self, value):
        for row in range(5):
            for column in range(5):
                if self.numberboard[row][column] == value:
                    self.scoreboard[row][column] = 1
                    return "found it!"
        return "not found"

    def check_for_win(self):
        for row in self.scoreboard:
            if sum(row) == 5:

                return self.boardnumber
        for column in range(5):
            tmp_sum = 0
            for row in range(5):
                tmp_sum += self.scoreboard[row][column]
            if tmp_sum == 5:
                return self.boardnumber
        return "no win"
    
    def getFinalScore(self):
        unmarked_value = 0
        for row in range(5):
            for column in range(5):
                unmarked_value += (-(self.scoreboard[row][column] - 1) * self.numberboard[row][column])
        return unmarked_value
    
    def printBoard(self, boardtype):
        #board_type can be "number" or "score"
        if boardtype == "number":
            self.print_board_internal(self.numberboard)
        elif boardtype == "score":
            self.print_board_internal(self.scoreboard)    
    
    
    def print_board_internal(self, board):
        print(f"Printing Board #{self.boardnumber}")
        for row in board:
            print("   ", end="")
            for char in row:
                if len(str(char)) == 1:
                    char = str(" " + str(char))
                print(char, end="  ")
            print()

if __name__ == "__main__":
   aoc2021_04_2("input.txt")