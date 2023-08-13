#include <iso646.h>

enum tool {ROCK, PAPER, SCISSORS};
enum outcome {P1_WON, P2_WON, DRAW};

enum outcome rps(enum tool p1, enum tool p2)
{
  if (p1 == p2)
      return DRAW;
  if (p1 == SCISSORS and p2 == PAPER
          or p1 == PAPER and p2 == ROCK
          or p1 == ROCK and p2 == SCISSORS)
      return P1_WON;
  return P2_WON;
}
