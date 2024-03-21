#include <stdbool.h>
#include <stdint.h>

bool hero(uint32_t bullets, uint32_t dragons){
  return ((bullets/2)>= dragons)?true : false;
  }
