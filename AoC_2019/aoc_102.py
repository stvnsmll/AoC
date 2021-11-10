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
    #                       Meaning: in quadrant A, there are 4 asteroids with slope 0.2 (asteroids 4,5,56, and 722)
    #                                               there are 2 asteroids with slope 0.5, and only one asteroid with slope 0.66
    '''
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
    
    Aquad = {}
    Bquad = {}
    Cquad = {}
    Dquad = {}
    for i in refmap:
        if refmap[i][2] == "UR":
            coord = "Aquad"
            Aquad.append()
            
            
    
    #print(visiblitydict)
    #print("Number of visible asteroids from " + str(refpos) + " is: " + str(len(visiblitydict) - 1))
    return [(len(visiblitydict) - 1),refmap,visiblitydict]

        
        
asteroidmap_raw = '''.#....#####...#..
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
 # Dict format[ast#: global x, glob y, rel x, rel y, visible asteroid count]
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
refpos = [8,3]

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
print(a[1])
print()
print(a[2])




