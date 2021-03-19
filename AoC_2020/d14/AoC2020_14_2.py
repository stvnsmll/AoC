#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 15.12.20              #
#                       #
# Day 14, Part 2        #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d14/docking_param_testing2.txt"
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
            value = int(i.split()[2])
            mem_loc = int(i.split("]")[0].split("[")[1])
            mem_bin = list(str(bin(mem_loc)[2:])[::-1])
            #print("Memory Location {} will be assigned {} (mem binary: {})".format(mem_loc, value, mem_bin))
            #print("   but first I must mask the memory location binary!")
            #mask the binary of the value to assing
            for mask_char in range(len(active_mask)):
                if mask_char >= len(mem_bin):
                    mem_bin.append("0")
                if active_mask[mask_char] == "0":
                    continue
                else:
                    mem_bin[mask_char] = active_mask[mask_char]
            #print("Masked binary: {}\n".format(listToString(mem_bin)))
            #convert masked bin back into decimal
            masked_bin = listToString(mem_bin)[::-1]
            addresses_to_write = mem_list(masked_bin)
            for i in addresses_to_write:
                memory[i] = value
            #Need to create all permutations of Xs and swap them with 1s and 0s.
            #then iterate through them all assigning "value" to that decimal address.
            #masked_mem = int(masked_bin, 2)
            #memory[masked_mem] = val_dec


    print()

    #for i in docking_data:
    #    print(i)

    #print(memory)

    answer = sum(memory.values())

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


def mem_list(masked_binary_address):
    #return a (decimal) list of all possible memories for a given binary address with "X" placeholders
    #print(masked_binary_address)
    num_of_Xs = masked_binary_address.count("X")
    permutations = 2**num_of_Xs
    #print("X Count: {}\n         |--> Number of permutations: {}\n\n".format(num_of_Xs, permutations))
    perms = []
    for i in range(permutations):
        x_formatter = "{:0" + str(num_of_Xs) + "d}"
        one_perm = x_formatter.format(int(bin(i)[2:]))
        #print(one_perm)
        perms.append(list(one_perm))#make a list?
    #print(perms)
    dec_adr_list = []
    for j in range(len(perms)):
        stepper = 0
        new_address = []
        for i in range(len(masked_binary_address)):
            if masked_binary_address[i] == "X":
                new_address.append(perms[j][stepper])
                stepper += 1
            else:
                new_address.append(masked_binary_address[i])
        int_address = int((listToString(new_address)), 2)
        dec_adr_list.append(int_address)
    #print(dec_adr_list)
    return dec_adr_list


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