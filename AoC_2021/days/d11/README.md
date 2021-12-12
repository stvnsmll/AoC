# AoC 2021, Day 11

Challenge Statement Summary:
  - iterate through octopus flashes and energy levels (part 1) [0.25 s]
  - find when all of the octopus flash together (part 2) [0.53 s]

It took me a while to figure out the rules for each step, specifically when the flashes happen vs when
the values are each incremented. I also had an error with my exit clause where it would exit even when
there were a few flashes that still had to happen. I spent a couple hours on this one, but it was fun.
I ended up finishing it on the 12th because of how busy the Saturday was with the fam. I propbably
could have used recursion to keep propogating the flashes, but I just re-drew the map every time. It
probably wasn't the most efficient solution method, but it got the job done, and still took < 1 second
to solve.
Part 2 was actually quite quick for me, as they way I set it up, I could just keep bumping my max
iteration count higher until the full map flash count was 100.

Day Rating: 8/10