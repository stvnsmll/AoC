#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 16.12.20              #
#                       #
# Day 16, Part 1        #
#########################


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d16/tickets_testing.txt"
    else:
        testing = 0
        input_file = "./d16/tickets.txt"

    # Using readline()
    tickets_file = open(input_file, 'r')
    rowcount = 0
    ticket_data = []

    while True:
        # Get next line from file
        line = tickets_file.readline()

        # if line is empty end of file is reached
        if not line:
            break

        #print(line)
        ticket_data.append(line.strip())
        rowcount += 1

    tickets_file.close()

    section = 0
    rules = []
    yourT = []
    otherTs = []

    for i in ticket_data:
        if i == "":
            section += 1
        else:
            if section == 0:
                rules.append(i)
            elif section == 1:
                yourT.append(i)
            else:
                otherTs.append(i)

    yourT = yourT[1]
    otherTs = otherTs[1:]

    print("The Rules: {}".format(list(rules)))
    print("Your Ticket: {}".format(yourT))
    print("Others' Tickets: {}".format(list(otherTs)))

    # Create all of the rules into class instances
    rule_list = []
    for i in rules:
        rule_list.append(rule(i))

    failed_tNos = []
    for i in otherTs:
        myNos = list(map(int,i.split(',')))
        for j in myNos:
            valid_count = 0
            for rulecheck in rule_list:
                if rulecheck.validValue(j) == True:
                    valid_count += 1
                    continue
            if valid_count == 0:
                failed_tNos.append(j)

    print(failed_tNos)


    answer = sum(failed_tNos)

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


class rule:
    def __init__(self, infostring):
        myInfo = infostring.split(": ")
        myRuleAll = myInfo[1].split(" or ")
        myRuleMin = myRuleAll[0].split("-")
        myRuleMax = myRuleAll[1].split("-")
        self.name = myInfo[0]
        self.rule = [list(map(int,myRuleMin)), list(map(int,myRuleMax))]
        #print(self.name)
        #print(self.rule)

    def validValue(self, value):
        #if value meets the rule, return true else false
        if self.rule[0][0] <= value <= self.rule[0][1]:
            #that number is valid
            return True
        if self.rule[1][0] <= value <= self.rule[1][1]:
            #that number is valid
            return True
        #that number is NOT valid
        return False


if __name__ == "__main__":
    main("r")