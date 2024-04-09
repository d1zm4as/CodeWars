#include <stddef.h>

int positive_sum(const int *values, size_t count){
  if(count==0){
    return 0;
    
  }
  
  int total = 0;
  for(size_t i = 0; i< count; i++){
    if(values[i]>=0){
      total+=values[i];
    }
  }
  return total;
}