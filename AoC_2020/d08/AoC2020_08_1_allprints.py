#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 08.12.20              #
#                       #
# Day 8, Part 1         #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d08/instructions_testing.txt"
    else:
        testing = 0
        input_file = "./d08/instructions.txt"

    # Using readline()
    instructions_file = open(input_file, 'r')
    rowcount = 0

    data_dict = {}
    data_key = 0

    while True:
        # Get next line from file
        line = instructions_file.readline().strip()

        # if line is empty end of file is reached
        if not line:
            break

        print(line)
        linesplit = line.split()
        operation = linesplit[0]
        argument = linesplit[1][1:]
        arg_dir = linesplit[1][:1]
        print("Op: " + operation + ", Arg: " + argument + " (dir: " + arg_dir + ")")
        newInstructionClassName = "Instr_" + str(data_key)
        print(newInstructionClassName)
        newInstructionClassName = Instruction(newInstructionClassName, data_key, operation, argument, arg_dir)
        newInstructionClassName.printInstruction()
        print(newInstructionClassName.checkforrepeat())
        print()

        data_dict[str(data_key)] = newInstructionClassName
        data_key += 1
        rowcount += 1

    instructions_file.close()

    # All data for instrucions has been loaded into a dictionary

    data_dict['0'].printInstruction()

    current_pos = 0
    accumulator = 0
    exit = 0
    loopcount = 0
    max_count = len(data_dict)

    while exit == 0:
        print(data_dict[str(current_pos)].name)
        this_op = data_dict[str(current_pos)].operation
        print(this_op)
        #log in the Instruction class this position that it was used.
        data_dict[str(current_pos)].stepused = current_pos
        if this_op == 'acc':
            #acumulate the value
            amt_to_acc = int(data_dict[str(current_pos)].argument)
            dir_to_acc = data_dict[str(current_pos)].arg_dir
            if dir_to_acc == "+":
                accumulator += amt_to_acc
            else:
                accumulator -= amt_to_acc
            #next position to check
            next_pos = current_pos + 1
        elif this_op == 'jmp':
            amt_to_jump = int(data_dict[str(current_pos)].argument)
            dir_to_jump = data_dict[str(current_pos)].arg_dir
            if dir_to_jump == "+":
                next_pos = current_pos + amt_to_jump
            else:
                next_pos = current_pos - amt_to_jump
        else: #'nop'
            next_pos = current_pos + 1

        if data_dict[str(next_pos)].checkforrepeat():
            exit = 1
        else:
            #set the new current position if exit case not met
            current_pos = next_pos
            loopcount += 1
            if loopcount == max_count:
                exit = 1

    last_pos = current_pos + 1
    print("\nLast Position: ", str(last_pos))

    print("\nTotal Rule Count:", rowcount)

    print('\n\ndone')
    return last_pos


class Instruction:
    def __init__(self, name, pos, op, arg, arg_dir):
        self.name = name
        self.operation = op
        self.argument = arg
        self.arg_dir = arg_dir
        self.position = pos
        self.stepused = -1

    def printInstruction(self):
        combinedarg = str(self.arg_dir) + str(self.argument)
        print("Instruction {}: Operation= {}, Argument= {}".format(self.name, self.operation, combinedarg))

    def checkforrepeat(self):
        if self.stepused == -1:
            return False
        else:
            return True


def getKey(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key
    return "key doesn't exist"


'''
# Recursion Example
def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])
'''


if __name__ == "__main__":
    main("r")