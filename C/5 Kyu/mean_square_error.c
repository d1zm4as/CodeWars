#include <stddef.h>

double mean_square_error(size_t n, const int a[n], const int b[n]) {

    double soma = 0;
    int cont = 0;
    while (n--){
      float diff = abs(a[cont]-b[cont]);
      soma += diff*diff;
      cont++;
    }
    return soma/cont;
}