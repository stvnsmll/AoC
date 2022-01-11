# AoC 2021, Day 16

Challenge Statement Summary:
  - Decode bit-wise packets and count the version sum (part 1) [2.22 s, 0.003s with no prints]
  - Decode the packets and solve using all of the operators (part 2) [0.1 s, 0.007s with no prints]

Serious use of recursion, lots of loops and tracking string parsing. You have to track
where you are in the message, what's been done, what's still to do, etc. The part that 
I always get hung up on is the amount of offset that has to be passed foward and backward
through the recursion. Overall, getting it to work wasn't too challenging, but understanding
the input was probably the hardest part for me. The "extra zeros" was really throwing me off
at the beginning.
This was all functional programming, but heavy use of recursion. I was stuck for a while (a 
couple days off and on), so I started my recursion function over after I fully understood 
the puzzle input. That went a lot quicker. Overall, it was kind of fun, but in the middle of
it all it was quite confusing and at times frustrating.

Day Rating: 8/10