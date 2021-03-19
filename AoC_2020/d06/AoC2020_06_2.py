#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 06.12.20              #
#                       #
# Day 6, Part 2         #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d06/customsans_testing.txt"
    else:
        testing = 0
        input_file = "./d06/customsans.txt"

    # Using readline()
    customsfile_file = open(input_file, 'r')
    rowcount = 0
    familycount = 0
    familymembercount = 0
    customs_responses = []
    tmpstring = ""
    master_yes_count = 0

    while True:
        rowcount += 1

        # Get next line from file
        line = customsfile_file.readline()

        # if line is empty
        # end of file is reached
        if not line:
            master_yes_count += processFamilyData(tmpstring, customs_responses, familymembercount)
            familymembercount += 1
            break

        if line == "\n":
            master_yes_count += processFamilyData(tmpstring, customs_responses, familymembercount)
            tmpstring = ""
            familycount += 1
            familymembercount = 0
            customs_responses = []
        else:
            tmpstring += (line.strip())
            customs_responses.append(list(line.strip()))

            familymembercount += 1
            # print("Passport #{}: {}".format((psportcount + 1), line.strip()))

    customsfile_file.close()

    print("\nCount of families:", (familycount + 1))
    print("Total Rows:", rowcount)
    print("\nTotal Number of Yes Responses:", master_yes_count)

    print('\n\ndone')
    return master_yes_count

def processFamilyData(customsresponses, customs_responses, familymembercount):
    #print("Customs String: {}".format(customsresponses))
    #print(customs_responses)
    unique_responses = list(set(customsresponses))
    unique_char_count = len(set(customsresponses))
    #print("Unique Characters:", unique_responses)
    #print("Unique Char Count:", unique_char_count)
    #print("Family Member Count:", familymembercount)
    shared_response_count = 0
    for i in range(unique_char_count):
        tmpyescount = 0
        resp = unique_responses[i]
        for j in range(familymembercount):
            #print(str(resp) + ", family member #" + str(j + 1))
            if resp in customs_responses[j]:
                tmpyescount += 1
                #print("one match")
        if tmpyescount == familymembercount:
            shared_response_count += 1
            #print("All people marked '{}' as yes! - count it".format(resp))

    #print(" --end of this family's customs form--")
    return shared_response_count


if __name__ == "__main__":
    main("r")