#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 07.12.20              #
#                       #
# Day 7, Part 1         #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d07/bagrules_testingb.txt"
    else:
        testing = 0
        input_file = "./d07/bagrules.txt"

    # Using readline()
    bagrules_file = open(input_file, 'r')
    rowcount = 0
    color_list = []

    data_dict = {}
    data_parent_dict = {}
    data_child_dict = {}
    data_key = 0

    while True:
        # Get next line from file
        line = bagrules_file.readline().strip()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        line = line.replace(" bags", " bag")
        line = line.replace(".", "")
        print(line)
        fullrule = line.split(" contain ")
        parent_rule = fullrule[0]
        children_rule = fullrule[1]
        print("Parent: " + str(parent_rule) + " -- Children: " + str(children_rule))

        #Parent Info
        parent_rule_split = parent_rule.split()
        parent_color = str(parent_rule_split[0]) + str(parent_rule_split[1])
        print("Parent Color: " + str(parent_color))
        color_list = addtolist(parent_color, color_list)

        #Child Info
        child_list = []
        if children_rule == "no other bag":
            print("**No Children**\n")
            child_list.append("nochildren")
        else:
            children_rule_split = children_rule.split(",")
            childcount = len(children_rule_split)
            for child in children_rule_split:
                child_rule_split = child.split()
                child_per_parent = child_rule_split[0]
                child_color = str(child_rule_split[1]) + str(child_rule_split[2])
                print("Child Color: " + str(child_color) + " (child count: " + str(child_per_parent) + ")")
                color_list = addtolist(child_color, color_list)
                #child_list.append([child_color, child_per_parent])
                child_list.append([child_color, child_per_parent])
            #print(child_list)
            print()

        data_parent_dict[str(data_key)] = parent_color
        data_child_dict[str(data_key)] = child_list
        data_dict[str(data_key)] = {'Parent': parent_color}, {'Child': child_list}
        data_key += 1

        rowcount += 1

    bagrules_file.close()

    print("\n\n\n     *#*#*#*#*#*#*#*#*#*#*#*\n\n\n")

    final_count = 0
    for bagrule in data_parent_dict:
        print(data_parent_dict[bagrule])
        print("  Children: ", end="")
        #print(data_child_dict[bagrule])
        #if "shinygold" in data_child_dict[bagrule]:
            #print("\n  YES\n")
        found = checkforgrandkid(data_child_dict[bagrule], data_child_dict, data_parent_dict)
        print(found)
        final_count += found
        print()

    print("\n\n\n")
    print(final_count)

    print()
    print(data_parent_dict)
    print()
    print(data_child_dict)
    print()
    print(data_dict)

    print()
    #print("Adjectives: (" + str(len(adjective_list)) + ")")
    #print(adjective_list)
    print("Colors: (" + str(len(color_list)) + ")")
    print(color_list)

    print("\nTotal Rule Count:", rowcount)

    print()
    totalbags = bagcount("shinygold", 0, data_child_dict, data_parent_dict)
    print("Total Bags for Shiny Gold: " + str(totalbags))

    print('\n\ndone')
    return totalbags


def checkforgrandkid(children, data_child_dict, data_parent_dict):
    print(children)
    child_list = []
    for i in range(len(children)):
        child_list.append(children[i][0])
    print(child_list)
    if "shinygold" in child_list:
        print("FOUND ONE!")
        return 1
    elif "nochildren" in children:
        return 0
    else:
        exit = "no"
        for i in children:
            print("this is i: " + str(i))
            # get this kids' children
            parentKey = getKey(i[0], data_parent_dict)
            newchildren = data_child_dict[parentKey]
            #print(newchildren)
            childfound = checkforgrandkid(newchildren, data_child_dict, data_parent_dict)
            print("Child Found result: " + str(childfound))
            if childfound == 1:
                return 1
        return 0

def bagcount(parent, running_count, data_child_dict, data_parent_dict):
    #
    print(parent)
    print("Running Count = " + str(running_count))
    parentKey = getKey(parent, data_parent_dict)
    children = data_child_dict[parentKey]
    print(children)
    for child in range(len(children)):
        if "nochildren" in children:
            return 0
        parentbag = children[child][0]
        qty = int(children[child][1])
        print(str(parentbag) + ": " + str(qty))
        running_count += (qty + (qty * bagcount(parentbag, 0, data_child_dict, data_parent_dict)))
    return running_count

'''
def sum(list):
    if len(list) == 1:
        return list[0]
    else:
        return list[0] + sum(list[1:])
'''

def addtolist(item, listtoupdate):
    if item not in listtoupdate:
        listtoupdate.append(item)
    return listtoupdate

def getKey(val, dictionary):
    for key, value in dictionary.items():
        if val == value:
            return key
    return "key doesn't exist"

if __name__ == "__main__":
    main("r")