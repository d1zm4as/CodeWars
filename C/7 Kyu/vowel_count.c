#include <stddef.h>
#include <string.h>
size_t get_count(const char *s)
{
    size_t cont = 0;
    size_t tam  = strlen(s);
    for(size_t i = 0; i<tam; i++){
        
        if (s[i]=='a' || s[i]=='e' ||s[i]=='i' ||s[i]=='o' ||s[i]=='u' ||s[i]=='A' ||s[i]=='E' ||s[i]=='I' ||s[i]=='O' ||s[i]=='U'){
           cont++;
        }
    }
  return cont;
}