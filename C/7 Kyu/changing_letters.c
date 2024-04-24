#include <string.h>
#include <ctype.h>
char *capitalize_vowels (char *s)
{
    size_t tam  = strlen(s);
    for(size_t i = 0; i<tam; i++){
        
        if (s[i]=='a' || s[i]=='e' ||s[i]=='i' ||s[i]=='o' ||s[i]=='u' ||s[i]=='A' ||s[i]=='E' ||s[i]=='I' ||s[i]=='O' ||s[i]=='U'){
            s[i] =  toupper(s[i]);
        }
    }
  return s;
}