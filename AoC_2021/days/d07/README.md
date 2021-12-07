# AoC 2021, Day 7

Challenge Statement Summary:
  - move crabs a common position that minimizes fuel spent (part 1) [0.002 seconds]
  - new fuel spending requirement (part 2) [0.3 seconds]

Part 1 was really just finding the median. I was surprised that that was how you can get the answer
really quickly. Part 2 changed how the fuel spent is calculated for each movement. I adjusted my 
distance calculation helper function, and now the answer was not so easy to find. I still started
with the median value as an initial guess, then I checked if increasing or decresing the distance
would reduce the total fuel spent. From there I just incremented the distance and it eventually 
found where fuel stopped decreasing. It's not the most optimized, but still solved in 0.3 seconds
so I don't really care too much.
No special data types or programming skills used... just loops and functions. Overall still fairly
simple especially on day 7. Fairly fun though.

Day Rating: 5/10
