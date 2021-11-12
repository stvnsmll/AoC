# AoC 2018, Day 2

Challenge Statement Summary:
  - count how many times a string has a repeated (of 2 or 3) characters  (part 1)
  - find the two strings that only differ by one character (part 2)

Still just using functional programming and some loops. No OOP yet.
For part 2, I initially thought I'd create a new list, removing the one I checked each time,
but I decided to just use list slicing to keep looking only forwards in the list.

The solution runs in 0.1 seconds, so there was no need to think too hard about data types and
optimizations.

Day Rating: 5/10