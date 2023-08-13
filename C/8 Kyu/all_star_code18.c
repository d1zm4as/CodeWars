#include <stddef.h>
#include <string.h>
size_t str_count(const char *str, char letter) {
  
  int cont = 0;
  
  for(int i = 0 ; i < strlen(str); i ++){
    if(str[i] == letter){
      cont++;
  }
  
}
  return cont;
}
