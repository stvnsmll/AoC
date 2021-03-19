#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 15.12.20              #
#                       #
# Day 14, Part 1        #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d14/docking_param_testing.txt"
    else:
        testing = 0
        input_file = "./d14/docking_param.txt"

    # Using readline()
    dockingdata_file = open(input_file, 'r')
    rowcount = 0
    docking_data = []

    while True:
        # Get next line from file
        line = dockingdata_file.readline().strip()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        docking_data.append(line)
        rowcount += 1

    dockingdata_file.close()

    active_mask = []
    memory = {}

    for i in docking_data:
        if i.split()[0] == "mask":
            active_mask = i.split()[2][::-1]
            #print("Active mask is: {}\n".format(active_mask))
        else:
            #assign the appropriate memory value
            mem_loc = int(i.split("]")[0].split("[")[1])
            val_dec = int(i.split()[2])
            val_bin = list(str(bin(val_dec)[2:])[::-1])
            #print("Memory Location {} will be assigned {} (binary: {})".format(mem_loc, val_dec, val_bin))
            #print("   but first I must mask it!")
            #mask the binary of the value to assing
            for mask_char in range(len(active_mask)):
                if mask_char >= len(val_bin):
                    val_bin.append("0")
                if active_mask[mask_char] == "X":
                    continue
                else:
                    val_bin[mask_char] = active_mask[mask_char]
            #print("Masked binary: {}".format(listToString(val_bin)))
            #convert masked bin back into decimal
            masked_bin = listToString(val_bin)[::-1]
            masked_val = int(masked_bin, 2)
            memory[mem_loc] = masked_val


    print()

    for i in docking_data:
        print(i)

    print(memory)

    answer = sum(memory.values())

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

if __name__ == "__main__":
    main("r")