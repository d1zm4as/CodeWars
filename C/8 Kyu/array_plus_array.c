#include <stddef.h>

long arr_plus_arr(const int *a,  const int *b, size_t na, size_t nb)
{
  
  long total = 0;
  long total2 = 0;
  for(size_t i = 0; i< na; i++){
   
      total+=a[i];
   
  }
  for(size_t i = 0; i< nb; i++){
    
      total2+=b[i];
   
  }
    return total+total2;
}
