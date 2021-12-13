#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 13.12.21              #
#                       #
# Day 12, Part 2        #
#########################

from datetime import datetime

valid_paths = []
cave_dict = {}

def aoc2021_12_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 12, Part 2\n~~ running as a test ~~")

    startTime = datetime.now()

    # Using readline()
    input_data_file = open(filename, 'r')
    input_data = []
    while True:
        # Get next line from file
        line = input_data_file.readline()
        # if line is empty end of file is reached
        if not line:
            break
        #print(line)
        input_data.append(line.strip())
    input_data_file.close()

    print(input_data)
    list_of_all_caves = []
    for i in input_data:
        for j in i.split("-"):
            if j not in list_of_all_caves:
                list_of_all_caves.append(j)
    list_of_all_caves.remove("start")
    list_of_all_caves.remove("end")
    print(list_of_all_caves)

    global cave_dict
    cave_dict = {}
    cave_count = 0
    for i in list_of_all_caves:
        cave_dict[i] = Cave(cave_count, i)
        cave_count += 1

    #populate the connections
    starting_caves = []
    for i in input_data:
        [a, b] = i.split("-")
        if a == "start":
            starting_caves.append(b)
        elif b == "start":
            starting_caves.append(a)
        else:
            for cave in cave_dict:
                cave_dict[cave].add_connection(i)
    
    printCaves(cave_dict, "conn")
    print(f"Starting cave list: {starting_caves}")

    #print(cave_dict["A"].conn)

    global valid_paths
    valid_paths = []
    #recurs this:
    visited_caves = ["start"]
    next_cave_list = starting_caves.copy()
    print("\n\nStarting Recursion:\n")
    pick_route2(visited_caves, next_cave_list)
    
    #print("\n\nList of possible paths (not final):")
    #logger = 0
    #for path in valid_paths:
    #    logger += 1
    #    print(f"{logger:02d}: {path}")
    #print()
    #print(len(valid_paths))

    print("still need to eliminate paths that have more than one double lowercase letter\n")
    #['start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end'] --fail
    #['start', 'A', 'b', 'A', 'b', 'end'] --pass
    #check = check_valid_rule(['start', 'A', 'b', 'A', 'b', 'end'])
    #print(check)
    count_valid = 0
    actual_valid = []
    for path in valid_paths:
        spath = path.split(",")
        check = check_valid_rule(spath)
        if check == 1:
            count_valid += 1
            actual_valid.append(path)
        #print(spath)

    answer = count_valid
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer

def check_valid_rule(path):#return 1 if valid, 0 if invalid
    lower_counts = {}
    for i in path:
        if i.islower():
            if i in lower_counts:
                lower_counts[i] += 1
            else:
                lower_counts[i] = 1
    counts_above_1 = 0
    for cave in lower_counts:
        if lower_counts[cave] > 1:
            counts_above_1 += 1
    #print(counts_above_1)
    if counts_above_1 < 2:
        return 1
    return 0

def pick_route2(visited_cv, next_cv):
    global valid_paths
    #print(f"Starting Loop. Visited: {visited_cv}, Next List: {next_cv}")
    #remove impossible next_caves
    ok_next_cv = []
    for cave in next_cv:
        if cave == "end" and cave in visited_cv:
            #do not add it to ok list of caves
            pass
        elif cave.islower() and visited_cv.count(cave) > 1:
            #do not add it to ok list of caves
            pass
        else:
            ok_next_cv.append(cave)
    
    ok_next_cv.sort()
    #move "end" to the end... just because
    if "end" in ok_next_cv:
        ok_next_cv.append(ok_next_cv.pop(ok_next_cv.index("end")))
    
    #print(f"   List of OK caves: {ok_next_cv}")
    for ok_cave in ok_next_cv:
        #print(f"   Looping through {ok_next_cv}, working on {ok_cave} now.")
        if ok_cave == "end":
            visited_cv.append(ok_cave)
            valid_paths.append(",".join(visited_cv))
            #print(f"      Added to valid paths: {','.join(visited_cv)}")
            return visited_cv
        #visited_cv.append(ok_cave)
        next_options = pick_route2((visited_cv + [ok_cave]), cave_dict[ok_cave].conn)
        #print(f"Complete List: {next_options}", end="\n\n")

    # if all that is left is "end", don't propogate but add to "valid_paths"
    
    #for each valid cave cycle throuh
    # append to the end of the cave list the new picked route 

    pass


def pick_route(visited_caves, next_cave_list):
    print(next_cave_list)
    stepper = 0
    for cave in next_cave_list:
        stepper += 1
        print(f"step {stepper}, cave {cave} from {next_cave_list}")
        if cave == "end":
            visited_caves.append("end")
            valid_paths.append(",".join(visited_caves))
            print("valid paths updated: ")
            print(valid_paths)
            print("\n")
            visited_caves = []
            return 0
        else:
            if cave.islower():
                if cave in visited_caves:
                    print(f"  Already been to cave: {cave}")
                    #terminate this branch of the recursion tree
                    return 1
                else:
                    print(f"  Cave {cave} added to the list.")
                    visited_caves.append(cave)
                    next_caves = cave_dict[cave].conn
                    pick_route(visited_caves, next_caves)
            else:#cave is uppercase
                print(f"  Cave {cave} added to the list.")
                visited_caves.append(cave)
                next_caves = cave_dict[cave].conn
                pick_route(visited_caves, next_caves)
    print(f"  Visited Caves: {visited_caves}, finished {next_cave_list}")
    print()


class Cave:
    def __init__(self, number, name):
        self.name = name
        self.number = number
        self.conn = []
    
    def add_connection(self, connection):
        [a, b] = connection.split("-")
        if a != self.name:
            if b != self.name:
                return 2#nothing to add
            else:
                #b is the name, so add a to conn list
                self.conn.append(a)
        else:
            self.conn.append(b)
        return 0

def printCaves(cavelist, type='name'):
    if type == 'name':
        for i in cavelist:
            print(cavelist[i].name)
    elif type == 'conn':
        for i in cavelist:
            print(f"{cavelist[i].name}: {cavelist[i].conn}")
    


if __name__ == "__main__":
   aoc2021_12_2("input.txt")