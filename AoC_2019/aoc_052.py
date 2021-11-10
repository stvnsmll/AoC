# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:08:29 2019

@author: jz981
"""

#Advent of Code, 2019
#Challenge 05.2
#20191205

#noun = 0 to 99 (originally 12)
#verb = 0 to 99 (originally 2)

noun = 225
verb = 1
inpt = 5

def address0finder(noun, verb, integerinput):
    #intlist = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    #intlist = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    intlist = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,48,82,225,102,59,84,224,1001,224,-944,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1101,92,58,224,101,-150,224,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1102,10,89,224,101,-890,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1101,29,16,225,101,23,110,224,1001,224,-95,224,4,224,102,8,223,223,1001,224,3,224,1,223,224,223,1102,75,72,225,1102,51,8,225,1102,26,16,225,1102,8,49,225,1001,122,64,224,1001,224,-113,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1102,55,72,225,1002,174,28,224,101,-896,224,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1102,57,32,225,2,113,117,224,101,-1326,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1,148,13,224,101,-120,224,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,677,226,224,102,2,223,223,1006,224,329,101,1,223,223,107,677,677,224,1002,223,2,223,1006,224,344,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,359,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,374,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,404,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,434,1001,223,1,223,1008,677,226,224,1002,223,2,223,1006,224,449,1001,223,1,223,7,226,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,479,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,494,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,1007,226,677,224,1002,223,2,223,1006,224,524,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,539,101,1,223,223,1107,677,226,224,102,2,223,223,1005,224,554,1001,223,1,223,108,677,226,224,1002,223,2,223,1006,224,569,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,1008,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,7,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,1008,677,677,224,102,2,223,223,1005,224,644,101,1,223,223,7,677,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]
    
    #intlist = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,5,19,23,1,23,5,27,1,27,13,31,1,31,5,35,1,9,35,39,2,13,39,43,1,43,10,47,1,47,13,51,2,10,51,55,1,55,5,59,1,59,5,63,1,63,13,67,1,13,67,71,1,71,10,75,1,6,75,79,1,6,79,83,2,10,83,87,1,87,5,91,1,5,91,95,2,95,10,99,1,9,99,103,1,103,13,107,2,10,107,111,2,13,111,115,1,6,115,119,1,119,10,123,2,9,123,127,2,127,9,131,1,131,10,135,1,135,2,139,1,10,139,0,99,2,0,14,0]
    #intlist[1] = noun
    #intlist[2] = verb
    newstart = 0
    outputval = []
    while True:
        #if newstart > (listlen-4):#does 4 really protect agains invalid lengths???
        # print("Error: list length")
        # break
        #else:
        #print(intlist)
        raw_opcode = intlist[newstart]
        formatted_opcode = str(raw_opcode).zfill(5)
        opcode = int(formatted_opcode[3:])
        param_mode1 = int(formatted_opcode[2])#third to left digit of formatted opcode
        param_mode2 = int(formatted_opcode[1])#second to left digit of formatted opcode
        param_mode3 = int(formatted_opcode[0])#leftmost digit of the formatted opcode
        print("Opcode: " + str(opcode))
        #print("Parameter Mode 1: " + str(param_mode1) + "\nParameter Mode 2: " + str(param_mode2)+ "\nParameter Mode 3: " + str(param_mode3))
        
        #validity checking
        if not ((1 <= opcode <= 8) or (opcode == 99)):
            #error found - terminate the function
            print("Nonvalid opcode: " + str(opcode))
            print(raw_opcode)
            outputval = 404
            break
        if not (0 <= param_mode1 <=1) or not (0 <= param_mode2 <=1) or not (0 <= param_mode3 <=1):
            #error found - terminate function
            print("Nonvalid parameter mode(s) ->> " + str(param_mode1) + ":" + str(param_mode2) + ":" + str(param_mode3))
            outputval = 404
            break
        
        if opcode == 99:
            #made it to the end of the string! good job.
            break
        
        #process opcode commands
        num1 = intlist[newstart + 1]
        if opcode == 1:
            num2 = intlist[newstart + 2]
            overridepos = intlist[newstart + 3]
            if param_mode1 == 0:
                temp_1 = intlist[num1]
            else:
                temp_1 = num1
            if param_mode2 == 0:
                temp_2 = intlist[num2]
            else:
                temp_2 = num2
            newval = temp_1 + temp_2
            print(str(newstart) + "[" + str(raw_opcode) + "," + str(temp_1) + "," + str(temp_2) + "]--> position " + str(overridepos) + " set to: " + str(newval))
            intlist[overridepos] = newval
            newstart += 4
        if opcode == 2:
            num2 = intlist[newstart + 2]
            overridepos = intlist[newstart + 3]
            if param_mode1 == 0:
                temp_1 = intlist[num1]
            else:
                temp_1 = num1
            if param_mode2 == 0:
                temp_2 = intlist[num2]
            else:
                temp_2 = num2
            newval = temp_1 * temp_2
            print(str(newstart) + "[" + str(raw_opcode) + "," + str(temp_1) + "," + str(temp_2) + "]--> position " + str(overridepos) + " set to: " + str(newval))
            intlist[overridepos] = newval
            newstart += 4
        if opcode == 3:
            overridepos = num1
            newval = int(integerinput)
            print(str(newstart) + "[" + str(raw_opcode) + "," + str(num1) + "]-->" + str(overridepos) + " position set to: " + str(newval))
            intlist[overridepos] = newval
            newstart += 2
        if opcode == 4:
            if param_mode1 == 0:
                temp_1 = intlist[num1]
            else:
                temp_1 = num1
            outputval.append(temp_1)
            print(str(newstart) + "[" + str(raw_opcode) + "," + str(num1) + "] output set to-->" + str(outputval))
            newstart += 2
        
        if opcode == 5:
            num2 = intlist[newstart + 2]
            if param_mode1 == 0:
                temp_1 = intlist[num1]
            else:
                temp_1 = num1
            if param_mode2 == 0:
                temp_2 = intlist[num2]
            else:
                temp_2 = num2
            
            if temp_1 != 0:
                newstart = temp_2
            else:
                newstart += 3
            print(str(newstart) + "[" + str(raw_opcode) + "," + str(temp_1) + "," + str(temp_2) + "]")
        if opcode == 6:
            num2 = intlist[newstart + 2]
            if param_mode1 == 0:
                temp_1 = intlist[num1]
            else:
                temp_1 = num1
            if param_mode2 == 0:
                temp_2 = intlist[num2]
            else:
                temp_2 = num2
            if temp_1 == 0:
                newstart = temp_2
            else:
                newstart += 3
            print(str(newstart) + "[" + str(raw_opcode) + "," + str(temp_1) + "," + str(temp_2) + "]")
        if opcode == 7:
            num2 = intlist[newstart + 2]
            num3 = intlist[newstart + 3]
            if param_mode1 == 0:
                temp_1 = intlist[num1]
            else:
                temp_1 = num1
            if param_mode2 == 0:
                temp_2 = intlist[num2]
            else:
                temp_2 = num2
            if param_mode3 == 0:
                temp_3 = intlist[num3]
            else:
                temp_3 = num3
            
            if temp_1 < temp_2:
                #store 1 in the position given by the third parameter
                newval = 1
                overridepos = num3
                intlist[overridepos] = newval
                newstart += 4
            else:
                #store 0 in the position given by the third parameter
                newval = 0
                overridepos = num3
                intlist[overridepos] = newval
                newstart += 4
            print(str(newstart) + "[" + str(raw_opcode) + "," + str(temp_1) + "," + str(temp_2) + "," + str(num3) + "]--> position " + str(overridepos) + " set to: " + str(newval))
        if opcode == 8:
            num2 = intlist[newstart + 2]
            num3 = intlist[newstart + 3]
            if param_mode1 == 0:
                temp_1 = intlist[num1]
            else:
                temp_1 = num1
            if param_mode2 == 0:
                temp_2 = intlist[num2]
            else:
                temp_2 = num2
            if param_mode3 == 0:
                temp_3 = intlist[num3]
            else:
                temp_3 = num3
            
            if temp_1 == temp_2:
                #store 1 in the position given by the third parameter
                newval = 1
                overridepos = num3
                intlist[overridepos] = newval
                newstart += 4
            else:
                #store 0 in the position given by the third parameter
                newval = 0
                overridepos = num3
                intlist[overridepos] = newval
                newstart += 4
            print(str(newstart) + "[" + str(raw_opcode) + "," + str(temp_1) + "," + str(temp_2) + "," + str(num3) + "]--> position " + str(overridepos) + " set to: " + str(newval))
        
        print(str(outputval) + "\n")
        #override/rewrite code now happens inside each opcode if command
    return outputval #used to return: intlist[0]

print()
print(address0finder(noun,verb,inpt))


'''

aoc_022_answer = 0

for noun in range(0,99):
    for verb in range(0,99):
        outputval = address0finder(noun, verb, integerinput)
        if outputval == 19690720:
            aoc_022_answer = (100 * noun) + verb
            print("Found the answer!")
            print(" Noun: " + str(noun))
            print(" Verb: " + str(verb))
            print("Puzzle Answer: " + str(aoc_022_answer))

if aoc_022_answer == 0:
    print("no match found in this range...")

'''
