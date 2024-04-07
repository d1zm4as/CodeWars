#include <stdbool.h>
#include <stddef.h>
#include <string.h>

bool alphanumeric(const char* strin) {
   
    int tam, i,a;
    tam = strlen(strin);
    if(tam==0){
      return false;
    }
    for(i = 0;i<tam;i++){
      a = (int)strin[i];
      if ( (a>=48 && a<=57) ||(a>=65 && a<=90)||(a>=97 && a<=122) ){
        ;
      }else{
        return false;
      }
    }
    return true;

}
