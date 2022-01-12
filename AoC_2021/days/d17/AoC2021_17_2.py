#########################
## Advent of Code 2021 ##
#########################
# Steven Small          #
# stvnsmll              #
# 12.01.22              #
#                       #
# Day 17, Part 2        #
#########################

from datetime import datetime

tz_minx = tz_maxx = tz_miny = tz_maxy = 0


def aoc2021_17_2(filename):
    if __name__ != "__main__":
        print("\nAoC 2021, Day 17, Part 2\n~~ running as a test ~~")

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
    print()
    x_values = input_data[0].split(" ")[2][2:-1]
    y_values = input_data[0].split(" ")[3][2:]
    #print(x_values)
    #print(y_values)

    #tz = target zone
    global tz_minx, tz_maxx, tz_miny, tz_maxy
    tz_minx = int(x_values.split("..")[0])
    tz_maxx = int(x_values.split("..")[1])
    tz_miny = int(y_values.split("..")[0])
    tz_maxy = int(y_values.split("..")[1])

    print(f"Target Zone:\n  x range = {tz_minx} to {tz_maxx}\n  y range = {tz_miny} to {tz_maxy}\n")
    # function "check_in_target([x,y])" checks if a coordinate is in the target zone
    #   it returns True if it is in the zone, otherwise False
    
    #starting coordinate is always [0,0]

    #iv = initial velocity [x_vel, y_vel]
    iv_x = 6
    iv_y = 9
    points_to_check = 300

    """ found = calc_path(iv_x, iv_y, points_to_check)
    print("\n")
    if found[0]:
        print(f"The traj [{iv_x}, {iv_y}] lands in the zone, with max height of {found[3]}!")
    else:
        print("No landing in zone, or not enough points to check") """

    #values for testing (the smaller closer target zone)
    iv_x_min = 1
    iv_x_max = 35
    iv_y_min = -20
    iv_y_max = 140

    if __name__ == "__main__":
        #values for official run (the full puzzle target zone)
        iv_x_min = 1
        iv_x_max = 181
        iv_y_min = -120
        iv_y_max = 120

    print(f"Running through x range: [{iv_x_min}, {iv_x_max}], y range: [{iv_y_min}, {iv_y_max}]")

    solns = []

    for xvel in range(iv_x_min, iv_x_max):
        for yvel in range(iv_y_min, iv_y_max):
            found = calc_path(xvel, yvel, points_to_check)
            if found[0]:
                solns.append(found)
        if xvel%5 == 0:
            print(xvel)
    
    print()
    #print(solns)
    
    max_of_solns = 0
    for soln in solns:
        if soln[3] > max_of_solns:
            max_of_solns = soln[3]
    
    print(f"Number of solutions: {len(solns)}")
    
    answer = len(solns)
        
    print(f"\nSolution: {answer}")
    
    print(f"Runtime Duration: {(datetime.now() - startTime)}\n")
    return answer


def check_in_target(coord):
    #  target zone is defined by the global varaibles
    #  the input coord is a list of format: [x, y]
    #  returns True if the input coord is within the target zone, otherwise False
    #print(f"Checking Coordinage [x,y] = {coord}")
    if (coord[0] in range(tz_minx, tz_maxx + 1)) and (coord[1] in range(tz_miny, tz_maxy + 1)):
        return True
    #otherwise
    return False

def calc_path(iv_x, iv_y, points_to_check):
    found_in_zone = [False]
    exit = 0
    loop_count = 0
    current_x = 0
    current_y = 0
    max_y = 0
    while exit == 0:
        #do the trajectory calculations here
        #print(f"Path point #{loop_count + 1}")
        #print(f"  start poistion [x,y] = [{current_x}, {current_y}]")
        current_x += iv_x
        current_y += iv_y
        if iv_x > 0:
            iv_x -= 1
        iv_y -= 1
        if current_y > max_y:
            max_y = current_y
        #print(f"  end poistion [x,y] =   [{current_x}, {current_y}]")
        if check_in_target([current_x, current_y]):
            exit = 1
            #print(f"\n FOUND A POINT IN THE ZONE!!\n   [{current_x}, {current_y}]")
            found_in_zone = [True, current_x, current_y, max_y]
            """         else:
            if (current_x > (tz_maxx + 100)) or (current_y < (tz_maxy - 100)):
                return [False] """
        loop_count += 1
        if loop_count == points_to_check:
            exit = 1
    return found_in_zone

if __name__ == "__main__":
   aoc2021_17_2("input.txt")