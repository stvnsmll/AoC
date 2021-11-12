# AoC 2018, Day 1

Challenge Statement Summary:
  - Sum the numbers in a provided list (part 1)
  - Find if that sum has ever been seen before, and keep repeating until there is a duplicate (part 2)

Simple introduction to programming fundamentals.
Used for loop to loop through all of the numbers in part 1.
Nested the for loop inside a while loop to keep looking for part 2.

For part 2, I stored the interim totals in a list, and kept looking over a list for matches.
It solved, but took 2 minutes and 19 seconds. I re-implemented the interim solution list using
a numpy array, and it now solves in 18 seconds.

I was surprised to see a challenge this early that makes you question datatypes. Overall a fun easy day,
and a good chance to get the testing scripts all up and running. It took a couple of hours to do this one
but that's because most of the time was spent trying to figure out how to structure a python project with
the unittest framework.


Day Rating: 4/10
  (low because quite easy, but still sort of fun)