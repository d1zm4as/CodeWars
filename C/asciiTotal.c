#include <stdio.h>
#include <string.h>


int uni_total(const char *s) {
    int result = 0;
    for (int i = 0; i < (int)strlen(s); ++i)
        result += (int)s[i];

    return  result;
}




int main(){

    char s[] = "GGG";
  
    

    printf("%d\n",uni_total(s));
    return 0;
}