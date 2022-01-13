# AoC 2021, Day 18

Challenge Statement Summary:
  - Sum and reduce snailfish numbers (number pairs) (part 1) [0.52 s]
  - Find max sum of any 2 of the provided snailfish number (pairs) (part 2) [12.8 s]

Not too challenging. A lot of code, and a bit of string splicing. I just used string data structures
and it worked out pretty well (especially with the eval() function). It took a couple hours to type
all of the code and run through the examples. Taking it step by step made it pretty easy. I got a little
hung up with catching double digit and string splicing and joining at the right points with either one
or two digit numbers.
For part two, I just set up some loops that check sums and store them in a list. Max of that list was 
the solution. It only took a couple minutes to set up that loop and solve it! It took 13 seconds to
solve, wich is quite a while, but it had to calculate 9900 different additions and reductions.

Day Rating: 10/10
