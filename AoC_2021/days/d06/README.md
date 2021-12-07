# AoC 2021, Day 6

Challenge Statement Summary:
  - count the spawning of lanternfish based on a starting string (part 1)
  - count for many more days (millions of fish) (part 2)

Part 1 was quick and easy. I used OOP to create a new object for each fish. It took 2.4 seconds to solve, so
when I saw part 2 exponentially increases that, I knew it wouldn't work. This is classic AoC. Instead of using
objects, I just created a dictionary to store the number of each fish at a certain age. I iterated each day
shifting the fish count down one and the ones that were at day 0 became day 6 and new ones started at day 8.
It was actually much quicker to program part 2 than part 1, but it was a fun little mental challenge. I loved
part 1 with OOP, and part 2 was quick and fun. In the end, my part 2 ran in 0.002 seconds!

Day Rating: 9/10
