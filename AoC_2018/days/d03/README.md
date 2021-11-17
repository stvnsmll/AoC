# AoC 2018, Day 3

Challenge Statement Summary:
  - count how many overlapping areas of fabric there are from all of the fabric requests  (part 1)
  - find the only fabric request that has no overlaps (part 2)

Starting to get fun. Used OOP to create a class for each fabric map. It made part 2 easy, because
I could use a tracker parameter in the object to check if it was an overlap.
This puzzle also is the first to get into the 2d map concept that is so common in AoC.

The solution runs in 1.1 seconds, so I didn't try to optimize it much. I ended up looping through 
each of the fabric maps twice for part 2.

Day Rating: 6/10
