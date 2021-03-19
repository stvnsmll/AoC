#########################
## Advent of Code 2020 ##
#########################
# Steven Small          #
# stvnsmll              #
# 04.12.20              #
#                       #
# Day 4, Part 2         #
#########################

import csv, re


def main(test):
    if test == 't':
        testing = 1
        input_file = "./d04/psportbash_testing2.txt"
    else:
        testing = 0
        input_file = "./d04/psportbash.txt"

    # Using readline()
    psportbash_file = open(input_file, 'r')
    rowcount = 0
    psportcount = 0
    passports = []
    tmpstring = ""
    validpassportcount = 0

    while True:
        rowcount += 1

        # Get next line from file
        line = psportbash_file.readline()

        # if line is empty
        # end of file is reached
        if not line:
            validpassportcount += processPassportData(tmpstring)
            break

        if line == "\n":
            validpassportcount += processPassportData(tmpstring)
            tmpstring = ""
            psportcount += 1
        else:
            tmpstring += (line.strip() + " ")
            # print("Passport #{}: {}".format((psportcount + 1), line.strip()))

    psportbash_file.close()

    print("\nCount of passports:", (psportcount + 1))
    print("Total Rows:", rowcount)
    print("\nValid Passports:", validpassportcount)

    print('\n\ndone')
    return validpassportcount


def processPassportData(passportdata):
    #print("Passport: {}".format(passportdata))
    fieldcount = 0
    validpassport = 0
    for i in passportdata:
        if i == ':':
            fieldcount += 1
    #print(fieldcount)
    if 'cid:' in passportdata:
        #print("has a country code")
        fieldcount -= 1
    else:
        #print("no country code")
        pass
    #print(fieldcount)
    if fieldcount == 7:
        # now we need to check the data in each field before we can say it is valid
        validpassport = 1 - checkPsPfields(passportdata)
    #print(" --end of passport--")
    return validpassport


def checkPsPfields(passportdata):
    # Parse the data into its various fields
    alldata = passportdata.split()
    for field in alldata:
        thisdata = field.split(":")
        category = thisdata[0]
        data = thisdata[1]
        if category == "cid":
            pass
        else:
            # print(category, "-->", data)
            s = switchSelect()
            validruleanddata = (s.switch(category, data))
            if validruleanddata == 1:
                # print(category, "-->", data)
                return 1
    return 0


class switchSelect:
    def switch(self, rule, data):
        if rule not in "byr iyr eyr hgt hcl ecl pid cid":
            print("invalid rule *************************")
            return 1
        return getattr(self, 'case_' + str(rule))(data)

    # Need to check all of the rules
    '''
    New Rules:
        byr (Birth Year) - four digits; at least 1920 and at most 2002.
        iyr (Issue Year) - four digits; at least 2010 and at most 2020.
        eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
        hgt (Height) - a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
        ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
        pid (Passport ID) - a nine-digit number, including leading zeroes.
        cid (Country ID) - ignored, missing or not.
    '''
    def case_byr(self, data):
        if data.isdigit():
            if 1920 <= int(data) <= 2002:
                # print("byr is valid")
                return 0
        # print("byr INVALID*************************")
        return 1

    def case_iyr(self, data):
        if data.isdigit():
            if 2010 <= int(data) <= 2020:
                # print("iyr is valid")
                return 0
        # print("iyr INVALID*************************")
        return 1

    def case_eyr(self, data):
        if data.isdigit():
            if 2020 <= int(data) <= 2030:
                # print("eyr is valid")
                return 0
        # print("eyr INVALID*************************")
        return 1

    def case_hgt(self, data):
        units = data[-2:]
        measure = int(data[:-2])
        if units == "cm":
            if 150 <= measure <= 193:
                # print("hgt is valid")
                return 0
        else:
            if 59 <= measure <= 76:
                # print("hgt is valid")
                return 0
        # print("hgt INVALID*************************")
        return 1

    def case_hcl(self, data):
        regex = "^#([a-f0-9]{6})$"
        if re.match(regex, data):
            # print("hcl is valid")
            return 0
        # print("hcl INVALID*************************")
        return 1

    def case_ecl(self, data):
        key = "amb blu brn gry grn hzl oth"
        if data in key:
            # print("ecl is valid")
            return 0
        # print("ecl INVALID*************************")
        return 1

    def case_pid(self, data):
        if data.isdigit():
            if len(data) == 9:
                # print("pid is valid")
                return 0
        # print("pid INVALID*************************")
        return 1

    def case_cid(self, data):
        # print(data + " for cid is ignored...")
        return 0



if __name__ == "__main__":
    main("r")