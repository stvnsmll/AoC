# AoC 2018, Day 5

Challenge Statement Summary:
  - reduce a polymer string based on adjacent opposite caps same letter pairs (part 1)
  - pull out each letter and see which is the lowest modified polymer reduction (part 2)

I thought this would be the first puzzle to use recursion, and I got it to work on the sample inputs
but the actual input was too long and caused recursion depth issues. A simple while loop ended up
working pretty well.
For part 2, I turned the while loop into a function and generated new lists with a characters removed.
I think a lot of time was spent doing list copying and removing characters. 

The solution runs in 9 seconds, and to optimize, I would have put the character to remove in the reducing
function, but that was slightly harder for my brain and I wanted to be done with the day.

Day Rating: 4/10
