# AoC 2021, Day 15

Challenge Statement Summary:
  - Find the least costly path through a maze (part 1) [0.06 s]
  - maze gets 5x larger (part 2) [13 s]

Instead of using a path finding script, I created a checker that looks at each neighbor
to find which neighbor has the lowest risk to get to that point. I iterate through the 
map from the top left corner to the bottom right (incrementing the Manhattan distance)
by 1 each loop. This solved fine for part 1, and the algorythm was fast/efficient enough
to solve the larger 5x size map.
The problem with part 2 though is that it could not find if the lowest risk path was to
go back upward or leftward. I thought about extra calculations once a new "low risk"
location was found, but I decided to re-calcualte the risk-map using the solved risk-map
and do it at least 10 times to catch up or left direction paths.
Part 2 was fun to use the remainder % thing while generating the larger map.

It took a long time to solve, but really I was just busy with family and holiday. Overall
not too tough of a day, but a nice mental challenge. The programming didn't take too long,
but I spent a while trying to figure out how to approach the problem.

Day Rating: 9/10