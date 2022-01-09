# AoC 2021, Day 14

Challenge Statement Summary:
  - Polymer list and insertions (part 1) [0.02 s]
  - Extend it out 40 iterations (part 2) [0.005 s]

Wow, so part 1 was quite easy, and I thought I was doing it efficient enough. But for part 2, the
string would get huge. I did get a little hint to store the counts instead of the full string, but
I was still hung up on how to know which letters would be added and which new pairs would then be 
available for the next step. The KEY was to undertand that if you know a pair and the insertion
rule, you know the letter count that is going up as well as the two new pairs that are added. I also
considered using recursion for a minute, but it would probably have gotten much too deep.

Overall it took me quite a while to figure it out.

Day Rating: 7/10
  trickey, but fun