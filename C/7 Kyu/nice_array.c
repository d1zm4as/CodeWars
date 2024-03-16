#include <stdbool.h>
#include <stddef.h>
bool find(size_t tam, const int *arr,int x){
  for(size_t i = 0; i< tam; i++){
    if(arr[i]==x){
     return true;
    }
  }
  return false;
}


bool is_nice_array (size_t length, const int array[length])
{ 
  if(length==0){
    return false;
  }
	int a;
  size_t i;
//   lista = array;
  for(i = 0; i<length;i++){
    a = array[i];
    if(!find(length,array, a+1) && !find(length,array,a-1)){
      return false;
    }
  }
    return true;

  

} 