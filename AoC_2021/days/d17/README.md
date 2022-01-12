# AoC 2021, Day 17

Challenge Statement Summary:
  - Find the maximum height of a projectile launch to still touch a target area (part 1) [2.05 s --> 0.3 s]
  - Count the total possible number of solutions (part 2) [18 min --> 10s --> 0.7 s]

Some people used a clever equation to solve part 1, but I (doing this later) saw that part 2
would require some sort of brute force, so I started part 1 with that approach. Part 1 was fairly
easy, and it was all about guessing proper bounds.
Based on how I set it up, I was able to solve it fairly quickly (solution in 2 seconds). For
part 2, the solution kept growing as I increased my bounds. The problem with my solution was that
it would cycle through the full number of points for each path (regardless of if it passed the
zone or not). Once I had the path calculation stop if the current path was past the zone (in X or
in Y), the solution times dropped siginificantly. My part 1 solution solves in 0.3s and part 2 in
0.7 seconds. Those have both been optimized a little to have realistic bounds for all of the variables.
Overall, it took me a couple hours to solve these. Pretty fun, only basic functions and loops. I 
used while loops so that it's easy to break out if needed.

Day Rating: 9/10
