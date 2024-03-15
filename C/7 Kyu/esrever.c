#include <stddef.h>

//   write results to the provided pre-allocated pointer reversed

void reverse(size_t length, const int array[length], int reversed[length]) {

    
    int idx = length-1;
    int i;
    int cont = 0;
    for(i = idx; i>=0; i--){
      reversed[cont] = array[idx];
      cont++;
      idx--;
    }
  
}