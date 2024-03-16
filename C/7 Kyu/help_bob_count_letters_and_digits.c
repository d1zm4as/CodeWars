#include <stddef.h>
# include <string.h>
size_t count_letters_and_digits(const char *input) {
    size_t cont, i,tam,a;    
    cont = 0;
    tam = strlen(input);
    
  for(i = 0;i<tam;i++){
    a = (int)input[i];
    if ( (a>=48 && a<=57) ||(a>=65 && a<=90)||(a>=97 && a<=122) ){
      cont++;
    }
  }
  return cont;
  
}