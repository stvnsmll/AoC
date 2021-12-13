# AoC 2021, Day 12

Challenge Statement Summary:
  - Find all of the possible paths through the caves (part 1) [0.04 s]
  - Rules allow for one small cave to be passed through twice (part 2) [~30 minutes!!]

Wow, so part 2 could be optimized. I also struggled in part 1 with the recursion. The completed path string kept getting
appended to instead of a new one starting where the recursion left off. I eventually got it, but it was a bit of 
troubleshooting. Part 2 had some other issues with it like "end" not being the last one that got tested. I'm not sure how
I could get it to solve faster. Maybe fewer lists and more sets or dictionaries. I didn't solve this one until the end of 
the 13th, so it actually took quite a while.

I think it would run faster if I modified the code to check for the double occurance of ONE small cave before checking 
at the very end. But the recursion was still taking a while.

Day Rating: 5/10