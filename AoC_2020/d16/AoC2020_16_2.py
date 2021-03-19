#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 16.12.20              #
#                       #
# Day 16, Part 2        #
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
    #print("All Other Tickets: {}".format(list(otherTs)))

    # Create all of the rules into class instances
    rule_list = []
    for i in range(len(rules)):
        rule_list.append(rule(rules[i], i))

    failed_tNos = []
    valid_tickets = []
    for i in otherTs:
        myNos = list(map(int,i.split(',')))
        invalid = 0
        for j in myNos:
            valid_count = 0
            for rulecheck in rule_list:
                if rulecheck.validValue(j) == True:
                    valid_count += 1
                    continue
            if valid_count == 0:
                failed_tNos.append(j)
                invalid = 1
                #otherTs.remove(i)
        if invalid == 0:
            valid_tickets.append(i)

    print(f"Invalid Ticket Numbers: {failed_tNos}")

    #print("Other Valid Tickets: {}\n\n".format(list(valid_tickets)))

    print("Invalid tickets removed. Proceeding to find column headers.\n\n")

    #split up all valid tickes into their numbers
    tmp_tkts = []
    for i in valid_tickets:
        myNos = list(map(int,i.split(',')))
        tmp_tkts.append(myNos)
    valid_tickets = tmp_tkts
    print(len(valid_tickets))

    #for each column in the other people's VALID tickets, find if they meet one rule
    # transpose the data columns into new rows
    #  i = column, j = each consecutive ticket
    column_data = []
    for i in range(len(valid_tickets[0])):
        tmp_column_data = []
        for j in range(len(valid_tickets)):
            #print(valid_tickets[j][i])
            tmp_column_data.append(valid_tickets[j][i])
        column_data.append(tmp_column_data)
    #print(column_data)

    #loop to continuously remove columns that have been assigned:
    unassigned = 1
    completed_columns = []
    important_data = []
    loop_count = 0
    while unassigned == 1:
        unassigned = 0
        for i in range(len(column_data)):
            if i in completed_columns:
                break
            column_defined = 0
            valid_rule_IDs_all = []
            for j in column_data[i]:
                valid_count = 0
                valid_rule_IDs = []
                for rulecheck in rule_list:
                    if rulecheck.columnID == 3000:
                        if rulecheck.validValue(j) == True:
                            valid_count += 1
                            valid_rule_IDs.append(rulecheck.ID)
                #print(f"Validity Count for {j} is {valid_count}. ~~{valid_rule_IDs}~~")
                valid_rule_IDs_all.append(valid_rule_IDs)
            #print(valid_rule_IDs_all)
            elements_in_all = list(set.intersection(*map(set, valid_rule_IDs_all)))
            important_data.append([i, elements_in_all])
            if len(elements_in_all) == 1:
                rule_to_lock = elements_in_all[0]
                print(f" ^-- FOUND ONE!!! rule ID: {rule_to_lock}\n\n")
                completed_columns.append(i)
                for rulecheck in rule_list:
                    if rulecheck.ID == rule_to_lock:
                        rulecheck.columnID = column_data[i]
                        print(f"  Column Header '{rulecheck.name}' matches with the data in column {rule_to_lock}.\n\n")
            else:
                unassigned = 1
                loop_count += 1
                if loop_count >100:
                    print(f"TERMINATING - {loop_count}")

                    for k in range(len(valid_rule_IDs_all)):
                        print(f"Ticket No: {k}-- {valid_rule_IDs_all[k]}")
                    unassigned = 0


    for i in important_data:
        print(i)

    answer = 0

    print("\nAnswer is: {}".format(answer))

    print('\n\ndone')
    return answer


class rule:
    def __init__(self, infostring, rowID):
        myInfo = infostring.split(": ")
        myRuleAll = myInfo[1].split(" or ")
        myRuleMin = myRuleAll[0].split("-")
        myRuleMax = myRuleAll[1].split("-")
        self.name = myInfo[0]
        self.ID = rowID
        self.rule = [list(map(int,myRuleMin)), list(map(int,myRuleMax))]
        self.columnID = 3000#3000 meaning it has not been assigned
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