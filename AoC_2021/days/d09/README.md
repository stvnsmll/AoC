# AoC 2021, Day 9

Challenge Statement Summary:
  - find local minimums in a 2d array (part 1) [0.03 s]
  - find the size of the basins of each local minimum (part 2) [0.06 s]

Yay, got to use recursion to grow the map in part 2! It was fairly simpe recursion, but I think using a global
variable for the map was key. I really like days like this one: maps, recursion, etc. I used dictionaries, lists,
functions (no OOP), for loops. I solved it early on December 10th, because I didn't get much time to work the 
problem on the 9th.
They both ran fast enough to not need any additional optimization. I was stuck in a recursion loop, as I made
the program go back over places already marked as "in the basin". That was one little area I was hung up on for
a few minutes.

Day Rating: 9/10