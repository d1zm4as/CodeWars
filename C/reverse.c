#include <stddef.h>

//   write results to the provided pre-allocated pointer reversed

void reverse(size_t length, const int array[length], int reversed[length]) {

    while (length--)
      *reversed++ = array[length];

}