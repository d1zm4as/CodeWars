#include <stdio.h>


int divisors(int n) {int cont = 0;for(int i=1;i<=n;i++){if(n%i==0){cont++;}}return cont;}







int main(){


    printf("%d\n",divisors(5));

    return 0;

}