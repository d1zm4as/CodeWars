#include <stdio.h>

int simple_multiplication(int number) { return number * (number % 2 == 0 ? 8 : 9);}

int main(){

int number = 5;

printf("%d\n",simple_multiplication(number));


}

