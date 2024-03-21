#include <stdbool.h>

bool cube_checker(int volume, int side) {
  /*  
  if(volume <=0){
      return false;
    }  
   */ 
  /*
    if((side*side*side)==volume && volume>0){
        return true ;
    }else{
      return false;
    }
*/
  return ((side*side*side)==volume && volume>0)?true : false;
}
