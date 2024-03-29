#include <math.h>

unsigned long long next_smaller_pronic(unsigned long long number) {
  unsigned long long x = round(sqrt(number)) - 1;
  return x * (x + 1);
}