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
        input_file = "./d07/bagrules_testing.txt"
    else:
        testing = 0
        input_file = "./d07/bagrules.txt"

    # Using readline()
    bagrules_file = open(input_file, 'r')
    rowcount = 0
    adjective_list = []
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
        parent_rule_adj = parent_rule_split[0]
        parent_rule_color = parent_rule_split[1]
        print("Parent Adj: " + str(parent_rule_adj) + " -- Color: " + str(parent_rule_color))
        adjective_list = addtolist(parent_rule_adj, adjective_list)
        color_list = addtolist(parent_rule_color, color_list)

        #Child Info
        if children_rule == "no other bag":
            print("**No Children**")
        else:
            children_rule_split = children_rule.split(",")
            childcount = len(children_rule_split)
            child_list = []
            for child in children_rule_split:
                child_rule_split = child.split()
                child_per_parent = child_rule_split[0]
                child_rule_adj = child_rule_split[1]
                child_rule_color = child_rule_split[2]
                print("Child Adj: " + str(child_rule_adj) + " -- Color: " + str(child_rule_color) + " (child count: " + str(child_per_parent) + ")")
                adjective_list = addtolist(child_rule_adj, adjective_list)
                color_list = addtolist(child_rule_color, color_list)
                child_list.append([child_rule_adj, child_rule_color, child_per_parent])
            print(child_list)
            print()

        data_parent_dict[str(data_key)] = [parent_rule_adj, parent_rule_color]
        data_child_dict[str(data_key)] = child_list
        data_dict[str(data_key)] = {'Parent': [parent_rule_adj, parent_rule_color]}, {'Child': child_list}
        data_key += 1


        rowcount += 1

    bagrules_file.close()

    print()
    print(data_parent_dict)
    print()
    print(data_child_dict)
    print()
    print(data_dict["0"])

    print()
    print("Adjectives: (" + str(len(adjective_list)) + ")")
    print(adjective_list)
    print("Colors: (" + str(len(color_list)) + ")")
    print(color_list)

    print("\nTotal Rule Count:", rowcount)

    print('\n\ndone')
    return 1



def addtolist(item, listtoupdate):
    if item not in listtoupdate:
        listtoupdate.append(item)
    return listtoupdate

if __name__ == "__main__":
    main("r")