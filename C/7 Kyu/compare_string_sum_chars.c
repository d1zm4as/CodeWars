#include <stdbool.h>
#include <string.h>

int uni_total(const char *s) {
    int a,i,result;
    if(!s){
      return 0;
    }
    result = 0;
    for (i = 0; i < (int)strlen(s); ++i){
        a = (int)s[i];
        if(a>=97 && a<=122){
          a -= 32;
          result+=a;
        }else if (a>=65 && a<=90){
          result+=a;
          
        }else{
          return 0;
        }
    }

    return  result;
}


bool compare(const char *s1, const char *s2) {

    int a,b;
    
    a = uni_total(s1);
    b = uni_total(s2);
    
    if(a==b){
      return true;
    }
    return false;

}