#include <stdbool.h>

bool am_i_wilson(unsigned n) {
  if(n==5 || n==13|| n==563){
    return true;
  }
  return false;
}