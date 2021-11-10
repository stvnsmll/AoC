# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 12:57:56 2019

@author: jz981
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 13:33:07 2019

@author: jz981
"""



'''
Advent of Code 2019
10.2
Steven Small
Python
20191210
'''


import operator

def resetmaptodefault():
    j = 0
    newdictionary = {}
    for i in asteroidmap_raw:
        newdictionary[j] = i
        j += 1
    return newdictionary

def printvariablemap(maplistdata,global_width):
    #print(len(maplistdata))
    i = 0
    while True:
        printline = ""
        for j in range((global_width)):
            printline += str(maplistdata[(i+j)])
        
        print(printline)
        i += (global_width + 1)
        if i > (len(maplistdata)-global_width):
            break

#asteroidmap_variable[int(refpos[0])][int(refpos[1])] = "O" #<-- show the relative center of the map for the reference position
def countvisibleasteroids(refpos):
    refmap = {}
    for i in asteroid_dict:
        dx = asteroid_dict[i][0] - refpos[0]
        dy = asteroid_dict[i][1] - refpos[1]
        distance = abs(dx) + abs(dy)
        slope = ""
        if dy < 0:
            side = "U"#up
        else:
            side = "D"#down
        if dx < 0:
            side = side + "L"#left
        else:
            side = side + "R"#right
        if dy == 0:
            side = "horiz"
            if dx > 0:
                slope = "right"
            else:
                slope = "left"
            if dx == 0:
                side = "me"
                slope = "me"
        else:
            if dx == 0:
                side = "vert"
                if dy > 0:
                    slope = "down"
                else:
                    slope = "up"      
        if slope == "":
            slope = dy / dx
        refmap[i] = [dx, dy, side, slope, distance, i]
    print("Relative Mapping:")
    print(refpos)
    
    #print a "O" at the new reference center of the map:
    maplocation = refpos[0] + (refpos[1]*(global_width + 1))
    asteroidmap_variable = resetmaptodefault()
    asteroidmap_variable[maplocation] = "O"
    printvariablemap(asteroidmap_variable, global_width)
    asteroidmap_variable = resetmaptodefault()
    
    print("New relative location of all of the asteroids: ([x,y,direction,slope,distance,global#])")
    print(refmap)
    
    visiblitydict = {}
    for i in refmap:
        #print(i)
        a = str(refmap[i][2]) + str(refmap[i][3])
        #print(a)
        visiblitydict[a] = 0
        
    '''
    #create a dictionary for each quadrant, with the center of the map being the reference position
    #   A = "UR" - upper right quadrant
    #   B = "DR" - lower right quadrant
    #   C = "DL" - lower left quadrant
    #   D = "UL" - upper left quadrant
    #   
    #     D  |  A
    #   -----+-----
    #     C  |  B
    #   
    #   Each dictionary is organized by key = slope, a number between 0 and 1, and the value as an array of all asteroids at that same slope (ordered farthest to nearest)
    #       Example: dictionary A may look like this  the array of each value for each key is [(absolute_asteroid_#),(distance(abs(x)+abs(y)) from the ref)]
    #                       Aquad = {0.2: [[4,15],[5,8],[56,7],[72,2]], 0.5:[[6,22],[15,10]], 0.66:[[37,5]]}
    #                       Meaning: in quadrant A, there are 4 asteroids with slope 0.2 (asteroids 4,5,56, and 72)
    #                                               there are 2 asteroids with slope 0.5, and only one asteroid with slope 0.66
    '''
    Aquad = {}
    Bquad = {}
    Cquad = {}
    Dquad = {}
    Upaxis = {}
    Rightaxis = {}
    Downaxis = {}
    Leftaxis = {}
    #i is the count of each asteroid in the reference map
    for i in refmap:
        #refmap[i][2] is the direction of the referenced asteroid from the center reference
        if refmap[i][2] == "UR":
            #print("i is: " + str(i))
            #j is the slope of this referenced asteroid from the center reference
            j = (refmap[i][3])
            #print("j is: " + str(j))
            #print("Asteroid # " + str(refmap[i][5]) + " is in quadrant A, with a slope of " + str(j) + " and distance of " + str(refmap[i][4]))
            if j in Aquad:
                #append to the end
                #print("\nDOUBLE FOUND\n")
                #print(Aquad[j])
                #k = len(Aquad[j])
                #print(k)
                Aquad[j].append([refmap[i][5], refmap[i][4]])
                #Aquad[refmap[i][3]].append([refmap[i][5], refmap[i][4]])
            else:
                #create new key
                Aquad[j] = [[refmap[i][5], refmap[i][4]]]
            #print("Aquad is now: " + str(Aquad))
        if refmap[i][2] == "DR":
            j = (refmap[i][3])
            if j in Bquad:
                #append to the end
                Bquad[j].append([refmap[i][5], refmap[i][4]])
            else:
                #create new key
                Bquad[j] = [[refmap[i][5], refmap[i][4]]]
        if refmap[i][2] == "DL":
            j = (refmap[i][3])
            if j in Cquad:
                #append to the end
                Cquad[j].append([refmap[i][5], refmap[i][4]])
            else:
                #create new key
                Cquad[j] = [[refmap[i][5], refmap[i][4]]]
        if refmap[i][2] == "UL":
            j = (refmap[i][3])
            if j in Dquad:
                #append to the end
                Dquad[j].append([refmap[i][5], refmap[i][4]])
            else:
                #create new key
                Dquad[j] = [[refmap[i][5], refmap[i][4]]]
        if refmap[i][3] == "up":
            j = (refmap[i][3])
            if j in Upaxis:
                #append to the end
                Upaxis[j].append([refmap[i][5], refmap[i][4]])
            else:
                #create new key
                Upaxis[j] = [[refmap[i][5], refmap[i][4]]]
        if refmap[i][3] == "right":
            j = (refmap[i][3])
            if j in Rightaxis:
                #append to the end
                Rightaxis[j].append([refmap[i][5], refmap[i][4]])
            else:
                #create new key
                Rightaxis[j] = [[refmap[i][5], refmap[i][4]]]
        if refmap[i][3] == "down":
            j = (refmap[i][3])
            if j in Downaxis:
                #append to the end
                Downaxis[j].append([refmap[i][5], refmap[i][4]])
            else:
                #create new key
                Downaxis[j] = [[refmap[i][5], refmap[i][4]]]
        if refmap[i][3] == "left":
            j = (refmap[i][3])
            if j in Leftaxis:
                #append to the end
                Leftaxis[j].append([refmap[i][5], refmap[i][4]])
            else:
                #create new key
                Leftaxis[j] = [[refmap[i][5], refmap[i][4]]]
                
    '''print("\n key is the slope, value is [(absolute_asteroid_#),(distance(abs(x)+abs(y)) from the ref)])")
    print("Final Aquad = " + str(Aquad))
    print("Final Bquad = " + str(Bquad))
    print("Final Cquad = " + str(Cquad))
    print("Final Dquad = " + str(Dquad))'''
            
            
            
    
    #print(visiblitydict)
    #print("Number of visible asteroids from " + str(refpos) + " is: " + str(len(visiblitydict) - 1))
    return [(len(visiblitydict) - 1),refmap,visiblitydict,Aquad,Bquad,Cquad,Dquad,Upaxis,Rightaxis,Downaxis,Leftaxis]

        
        
asteroidmap_raw = '''#...##.####.#.......#.##..##.#.
#.##.#..#..#...##..##.##.#.....
#..#####.#......#..#....#.###.#
...#.#.#...#..#.....#..#..#.#..
.#.....##..#...#..#.#...##.....
##.....#..........##..#......##
.##..##.#.#....##..##.......#..
#.##.##....###..#...##...##....
##.#.#............##..#...##..#
###..##.###.....#.##...####....
...##..#...##...##..#.#..#...#.
..#.#.##.#.#.#####.#....####.#.
#......###.##....#...#...#...##
.....#...#.#.#.#....#...#......
#..#.#.#..#....#..#...#..#..##.
#.....#..##.....#...###..#..#.#
.....####.#..#...##..#..#..#..#
..#.....#.#........#.#.##..####
.#.....##..#.##.....#...###....
###.###....#..#..#.....#####...
#..##.##..##.#.#....#.#......#.
.#....#.##..#.#.#.......##.....
##.##...#...#....###.#....#....
.....#.######.#.#..#..#.#.....#
.#..#.##.#....#.##..#.#...##..#
.##.###..#..#..#.###...#####.#.
#...#...........#.....#.......#
#....##.#.#..##...#..####...#..
#.####......#####.....#.##..#..
.#...#....#...##..##.#.#......#
#..###.....##.#.......#.##...##'''


'''.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....#...###..
..#.#.....#....##'''

totasteroidcount = asteroidmap_raw.count('#')
print(str(totasteroidcount) + " asteroids.")

#Map Dimensions:
global_height = asteroidmap_raw.count('\n') + 1
global_width = int((len(asteroidmap_raw) - asteroidmap_raw.count('\n')) / global_height)
print("Full map is " + str(global_width) + " wide by " + str(global_height) + " tall.")
print()

asteroidmap_variable = {}
        
#this line resets the map to default
asteroidmap_variable = resetmaptodefault()

printvariablemap(asteroidmap_variable, global_width)
print()

#How to access/change a single location in the map:
# call location by: asteroidmap_variable[x pos][y pos]

#Create dictionary with a key for each asteroid
x = 0
y = 0
j = 0
asteroid_dict = {}
 # Dict format[ast#: global x, glob y]
for i in asteroidmap_raw:
    if i == "#":
        asteroid_dict[j] = [x,y]
        j += 1
    x += 1
    if i == "\n":
        y += 1
        x = 0
print("Absolute Position of each asteroid:")
print(asteroid_dict)
print()

#Position Testing
#Reference position, refpos = [x,y]
refpos = [17,22] #[8,3]

#countvisibleasteroids(refpos)


#this code loops though and finds the location with the best asteroid visibility count:
'''
dict_of_visibilities = {}
for i in asteroid_dict:
    a = ([(asteroid_dict[i][0]), (asteroid_dict[i][1])])
    dict_of_visibilities[i] = countvisibleasteroids(a)

print(dict_of_visibilities)

maxvisibility = max(dict_of_visibilities, key=lambda k: dict_of_visibilities[k])
print()
print("Max visible planets seen at " + str(asteroid_dict[maxvisibility]) + " with a total of " + str(dict_of_visibilities[maxvisibility]) + " seen.")
'''

print("\n\n\n")
print("Reference Positions from: " + str(refpos))
a = countvisibleasteroids(refpos)

print("\n\n\n")

print(str(a[0]) + " visible asteroids from global " + str(refpos))
print()
for i in a:
    print(i)
    print()
    
Aquad = a[3]
Bquad = a[4]
Cquad = a[5]
Dquad = a[6]
Upaxis = a[7]
Rightaxis = a[8]
Downaxis = a[9]
Leftaxis = a[10]



def deleteone(array,loc):
    return array.pop(loc)
    
    
print(Aquad)
print(sorted(Aquad))
print()
print(Bquad)
print(sorted(Bquad))
print()
print(Cquad)
print(sorted(Cquad))
print()
print(Dquad)
print(sorted(Dquad))
print()

'''
Example Map
0..|1|234   <---0-4
.5.|6|78.   <---5-8
.90|.|123   <---10-13
---------
45.|O|.78   <---14-18
---------
9.0|.|12.   <---19-22
34.|5|.6.   <---23-26
78.|9|.01   <---27-31


built from:
#..####
.#.###.
.##.###
##.#.##
#.#.##.
##.#.#.
##.##.#
'''

#deleteone for quadrant D needs to be in reverse order (Delete from the back forward)
#deleteone for up axis needs to be in reverse order
#delete one for left needs to be in reverse order



#atmp = sorted(Aquad)
SortedA = {}
SortedB = {}
SortedC = {}
SortedD = {}
for i in sorted(Aquad):
    SortedA[i] = Aquad[i]
for i in sorted(Bquad):
    SortedB[i] = Bquad[i]
for i in sorted(Cquad):
    SortedC[i] = Cquad[i]
for i in sorted(Dquad):
    SortedD[i] = Dquad[i]    
print(SortedA)
print(SortedB)
print(SortedC)
print(SortedD)



print("\n\n\n\n")

mastercount = 0
loopcount = 0
asteroidpoporder = []

while True:
    mastercounttmp = mastercount
    for i in Upaxis:
        if len(Upaxis[i]) != 0:
            asteroidpoporder.append(Upaxis[i][((len(Upaxis[i])) - 1)][0])
            deleteone(Upaxis[i],((len(Upaxis[i])) - 1))
            mastercount += 1
    for i in SortedA:
        #print(i)
        #print(SortedA[i])
        #print(len(SortedA[i]))
        if len(SortedA[i]) != 0:
            #cannot delete a key mid loop, otherwise could have used: del SortedA[i]
            asteroidpoporder.append(SortedA[i][((len(SortedA[i])) - 1)][0])
            deleteone(SortedA[i],((len(SortedA[i])) - 1))
            mastercount += 1
    for i in Rightaxis:
        if len(Rightaxis[i]) != 0:
            asteroidpoporder.append(Rightaxis[i][0][0])
            deleteone(Rightaxis[i],0)
            mastercount += 1
    for i in SortedB:
        if len(SortedB[i]) != 0:
            asteroidpoporder.append(SortedB[i][0][0])
            deleteone(SortedB[i],0)
            mastercount += 1
    for i in Downaxis:
        if len(Downaxis[i]) != 0:
            asteroidpoporder.append(Downaxis[i][0][0])
            deleteone(Downaxis[i],0)
            mastercount += 1
    for i in SortedC:
        if len(SortedC[i]) != 0:
            asteroidpoporder.append(SortedC[i][0][0])
            deleteone(SortedC[i],0)
            mastercount += 1
    for i in Leftaxis:
        if len(Leftaxis[i]) != 0:
            asteroidpoporder.append(Leftaxis[i][((len(Leftaxis[i])) - 1)][0])
            deleteone(Leftaxis[i],((len(Leftaxis[i])) - 1))
            mastercount += 1
    for i in SortedD:
        if len(SortedD[i]) != 0:
            asteroidpoporder.append(SortedD[i][((len(SortedD[i])) - 1)][0])
            deleteone(SortedD[i],((len(SortedD[i])) - 1))
            mastercount += 1
    if mastercounttmp == mastercount:
        break
    loopcount += 1
    #print("naxt")
print(SortedA)
print(SortedB)
print(SortedC)
print(SortedD)

print(mastercount)
print(loopcount)
print(asteroidpoporder)

twohundredth = asteroidpoporder[199]
twohund_coordx = asteroid_dict[twohundredth][0]
twohund_coordy = asteroid_dict[twohundredth][1]

answer = (twohund_coordx * 100) + twohund_coordy

print(twohundredth)
print("[" + str(twohund_coordx) + ", " + str(twohund_coordy) + "]")
#200th asteroid:
print("The 200th asteroid is global #" + str(twohundredth) + ", and the puzzle answer is: " + str(answer))

















